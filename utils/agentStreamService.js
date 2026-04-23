const { BASE_URL } = require("./chartService");

function genSessionId() {
  return `sess_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
}

function createUtf8StreamDecoder() {
  let pending = [];

  function getBytes(input) {
    if (typeof input === "string") return null;
    if (input instanceof ArrayBuffer) return new Uint8Array(input);
    if (input && input.buffer instanceof ArrayBuffer) {
      return new Uint8Array(input.buffer, input.byteOffset || 0, input.byteLength);
    }
    return null;
  }

  function decode(input) {
    if (typeof input === "string") return input;

    const incoming = getBytes(input);
    if (!incoming) return "";

    let bytes = incoming;
    if (pending.length) {
      bytes = new Uint8Array(pending.length + incoming.length);
      bytes.set(pending, 0);
      bytes.set(incoming, pending.length);
      pending = [];
    }

    let output = "";
    let i = 0;
    while (i < bytes.length) {
      const first = bytes[i];
      if (first < 0x80) {
        output += String.fromCharCode(first);
        i += 1;
        continue;
      }

      let needed = 0;
      let codePoint = 0;
      if ((first & 0xe0) === 0xc0) {
        needed = 2;
        codePoint = first & 0x1f;
      } else if ((first & 0xf0) === 0xe0) {
        needed = 3;
        codePoint = first & 0x0f;
      } else if ((first & 0xf8) === 0xf0) {
        needed = 4;
        codePoint = first & 0x07;
      } else {
        output += "\ufffd";
        i += 1;
        continue;
      }

      if (i + needed > bytes.length) {
        pending = Array.prototype.slice.call(bytes, i);
        break;
      }

      let valid = true;
      for (let j = 1; j < needed; j++) {
        const next = bytes[i + j];
        if ((next & 0xc0) !== 0x80) {
          valid = false;
          break;
        }
        codePoint = (codePoint << 6) | (next & 0x3f);
      }

      if (!valid) {
        output += "\ufffd";
        i += 1;
        continue;
      }

      if (codePoint <= 0xffff) {
        output += String.fromCharCode(codePoint);
      } else {
        codePoint -= 0x10000;
        output += String.fromCharCode(0xd800 + (codePoint >> 10), 0xdc00 + (codePoint & 0x3ff));
      }
      i += needed;
    }

    return output;
  }

  return { decode };
}

function startAgentStream(options) {
  const decoder = createUtf8StreamDecoder();
  let buffer = "";
  let done = false;
  let receivedDelta = false;

  function emitError(message) {
    if (done) return;
    done = true;
    if (options.onError) options.onError(message);
  }

  function handleEvent(event) {
    if (event.type === "meta") {
      if (options.onMeta) options.onMeta(event);
      return;
    }

    if (event.type === "ping") {
      if (options.onPing) options.onPing(event);
      return;
    }

    if (event.type === "progress") {
      if (options.onProgress) options.onProgress(event);
      return;
    }

    if (event.type === "delta") {
      receivedDelta = true;
      if (options.onDelta) options.onDelta(event.content || "");
      return;
    }

    if (event.type === "done") {
      done = true;
      if (options.onDone) options.onDone(event);
      return;
    }

    if (event.type === "error") {
      emitError(event.message || "流式响应出错");
    }
  }

  function processText(text) {
    buffer += text;
    const lines = buffer.split("\n");
    buffer = lines.pop() || "";

    lines.forEach(rawLine => {
      const line = rawLine.replace(/\r$/, "");
      if (!line.startsWith("data: ")) return;
      const jsonStr = line.slice(6).trim();
      if (!jsonStr) return;

      try {
        handleEvent(JSON.parse(jsonStr));
      } catch (err) {
        // Ignore incomplete or malformed SSE lines.
      }
    });
  }

  const task = wx.request({
    url: `${BASE_URL}/api/agent/stream`,
    method: "POST",
    enableChunked: true,
    timeout: 180000,
    header: {
      "Content-Type": "application/json",
      Accept: "text/event-stream",
    },
    data: {
      birthDate: options.birthDate,
      timeIndex: Number(options.timeIndex),
      gender: options.gender,
      occupation: options.occupation || "",
      userId: options.userId,
      sessionId: options.sessionId,
      question: options.question,
    },
    success() {},
    fail(err) {
      const errMsg = (err && err.errMsg) || "";
      if (done || (receivedDelta && errMsg.indexOf("canceled") !== -1)) return;
      emitError(errMsg ? `网络错误：${errMsg}` : "网络请求失败");
    },
  });

  if (task && task.onChunkReceived) {
    task.onChunkReceived(response => {
      processText(decoder.decode(response.data));
    });
  } else {
    emitError("当前微信基础库不支持流式响应");
  }

  return {
    abort() {
      done = true;
      if (task && task.abort) task.abort();
    },
  };
}

module.exports = {
  genSessionId,
  startAgentStream,
};
