const storage = require("../../utils/storage");
const chartService = require("../../utils/chartService");
const { genSessionId, startAgentStream } = require("../../utils/agentStreamService");
const { markdownToNodes } = require("../../utils/markdown");

const TYPEWRITER_INTERVAL_MS = 30;
const TYPEWRITER_BATCH_SIZE = 2;

function createAssistantMessage(content, streaming) {
  return {
    id: `a_${Date.now()}_${Math.random().toString(36).slice(2, 6)}`,
    role: "assistant",
    content: content || "",
    nodes: markdownToNodes(content || ""),
    streaming: !!streaming,
    statusText: streaming ? "正在连接分析引擎..." : "",
    waitingSeconds: 0,
    renderMode: streaming ? "text" : "markdown",
  };
}

Page({
  data: {
    profile: null,
    currentUser: null,
    pageState: "loadingChart",
    errorMessage: "",
    sessionId: "",
    messages: [],
    inputText: "",
    inputDisabled: false,
    modal: {
      visible: false,
      icon: "",
      title: "",
      message: "",
      buttons: [],
    },
  },

  _stream: null,
  _pendingQuestion: "",
  _typewriterBuffer: "",
  _typewriterTimer: null,
  _typewriterDonePending: false,
  _waitingTimer: null,
  _streamStartedAt: 0,
  _latestProgressText: "",
  _hasReceivedDelta: false,
  _streamFinishedCounted: false,

  onLoad(options) {
    this._pendingQuestion = options && options.question ? decodeURIComponent(options.question) : "";

    const profile = storage.getSelectedProfile();
    const currentUser = storage.getCurrentUser();
    if (!profile || !currentUser) {
      wx.redirectTo({ url: "/pages/register/index" });
      return;
    }

    this.setData({ profile, currentUser, sessionId: genSessionId() });

    if (profile.calibrationStatus !== "success") {
      this.showModal("!", "命盘未校准", "请先完成命盘校准，才能使用问答功能", [
        { text: "开始校准", action: "startCalibration", primary: true },
      ]);
      return;
    }

    this.prepareChart();
  },

  prepareChart() {
    const profile = storage.getSelectedProfile();
    const chartKey = chartService.getChartKey(profile);

    if (profile.chartData && profile.chartKey === chartKey) {
      this.enterReadyState();
      return;
    }

    this.setData({ pageState: "loadingChart", errorMessage: "" });
    chartService.fetchChart(profile).then(chart => {
      storage.saveChartForProfile(profile.id, chart, chartKey);
      this.enterReadyState();
    }).catch(err => {
      this.setData({
        pageState: "error",
        errorMessage: err.message || "命盘加载失败，请重试",
      });
    });
  },

  enterReadyState() {
    const greeting = createAssistantMessage("你好，我已经了解了你的命盘。关于事业、感情、家庭或财运，你想知道什么？", false);
    this.setData({
      pageState: "ready",
      inputDisabled: false,
      messages: [greeting],
      errorMessage: "",
    });

    if (this._pendingQuestion) {
      const question = this._pendingQuestion;
      this._pendingQuestion = "";
      setTimeout(() => {
        this.sendQuestion(question);
      }, 80);
    }
  },

  handleInput(event) {
    this.setData({ inputText: event.detail.value });
  },

  onSend() {
    const question = (this.data.inputText || "").trim();
    if (!question) return;
    this.sendQuestion(question);
  },

  sendQuestion(question) {
    if (this.data.pageState !== "ready" || this.data.inputDisabled) return;

    const profile = storage.getSelectedProfile();
    const currentUser = storage.getCurrentUser();
    const userMessage = {
      id: `u_${Date.now()}`,
      role: "user",
      content: question,
      nodes: [],
      streaming: false,
    };
    const assistantMessage = createAssistantMessage("", true);

    this.setData({
      messages: this.data.messages.concat([userMessage, assistantMessage]),
      inputText: "",
      inputDisabled: true,
      pageState: "streaming",
      errorMessage: "",
    });

    this.startWaitingTimer("正在连接分析引擎...");

    this._stream = startAgentStream({
      birthDate: profile.birthDate,
      timeIndex: profile.timeIndex,
      gender: profile.gender,
      occupation: profile.profession || "",
      userId: currentUser.id,
      sessionId: this.data.sessionId,
      question,
      onMeta: event => this.handleStreamMeta(event),
      onProgress: event => this.handleStreamProgress(event),
      onPing: event => this.handleStreamPing(event),
      onDelta: content => this.appendAssistantDelta(content),
      onDone: () => this.finishStream(),
      onError: message => this.failStream(message),
    });
  },

  handleStreamMeta() {
    this.updateStreamProgress("连接已建立，正在准备分析...");
  },

  handleStreamProgress(event) {
    this.updateStreamProgress(event.message || "正在分析命盘...");
  },

  handleStreamPing() {
    this.updateWaitingStatus();
  },

  updateStreamProgress(text) {
    this._latestProgressText = text || this._latestProgressText;
    this.updateWaitingStatus();
  },

  startWaitingTimer(initialText) {
    this.clearWaitingTimer();
    this.clearTypewriterTimer();
    this._typewriterBuffer = "";
    this._typewriterDonePending = false;
    this._streamStartedAt = Date.now();
    this._latestProgressText = initialText || "正在连接分析引擎...";
    this._hasReceivedDelta = false;
    this._streamFinishedCounted = false;
    this.updateWaitingStatus();
    this._waitingTimer = setInterval(() => {
      this.updateWaitingStatus();
    }, 1000);
  },

  getWaitingStatus(elapsedSeconds) {
    if (elapsedSeconds >= 60) {
      return "仍在深度分析，可继续等待或停止生成";
    }
    if (elapsedSeconds >= 30) {
      return `分析还在继续，已等待 ${elapsedSeconds}s`;
    }
    if (elapsedSeconds >= 10) {
      return "正在推演命盘，可能还需要一些时间...";
    }
    return this._latestProgressText || "正在连接分析引擎...";
  },

  updateWaitingStatus() {
    if (this._hasReceivedDelta || this.data.pageState !== "streaming") return;
    const elapsedSeconds = this._streamStartedAt
      ? Math.max(0, Math.floor((Date.now() - this._streamStartedAt) / 1000))
      : 0;
    this.updateStreamingAssistant({
      statusText: this.getWaitingStatus(elapsedSeconds),
      waitingSeconds: elapsedSeconds,
    });
  },

  appendAssistantDelta(delta) {
    if (!delta) return;
    this._hasReceivedDelta = true;
    this.clearWaitingTimer();
    this._typewriterBuffer += delta;
    this.updateStreamingAssistant({
      statusText: "正在生成回答...",
      renderMode: "text",
    });
    this.ensureTypewriterTimer();
  },

  finishStream() {
    this._stream = null;
    this.clearWaitingTimer();
    this._typewriterDonePending = true;
    if (!this._typewriterBuffer) {
      this.completeAssistantMessage(true);
    }
  },

  failStream(message) {
    this._stream = null;
    this.clearWaitingTimer();
    this.flushTypewriterBuffer();
    this.clearTypewriterTimer();
    const messages = this.data.messages.map((item, index) => {
      if (index !== this.data.messages.length - 1 || !item.streaming) return item;
      const content = item.content || "[响应出错]";
      return Object.assign({}, item, {
        content,
        nodes: markdownToNodes(content),
        streaming: false,
        statusText: "",
        renderMode: "markdown",
      });
    });
    this.setData({
      messages,
      pageState: "ready",
      inputDisabled: false,
      errorMessage: message || "问答请求失败",
    });
  },

  ensureTypewriterTimer() {
    if (this._typewriterTimer) return;
    this._typewriterTimer = setInterval(() => {
      this.drainTypewriterBuffer();
    }, TYPEWRITER_INTERVAL_MS);
    this.drainTypewriterBuffer();
  },

  drainTypewriterBuffer() {
    if (!this._typewriterBuffer) {
      this.clearTypewriterTimer();
      if (this._typewriterDonePending) {
        this.completeAssistantMessage(true);
      }
      return;
    }

    const chars = Array.from(this._typewriterBuffer);
    const nextText = chars.slice(0, TYPEWRITER_BATCH_SIZE).join("");
    this._typewriterBuffer = chars.slice(TYPEWRITER_BATCH_SIZE).join("");
    this.appendAssistantText(nextText);
  },

  appendAssistantText(text) {
    if (!text) return;
    const messages = this.data.messages.map((item, index) => {
      if (index !== this.data.messages.length - 1 || !item.streaming) return item;
      return Object.assign({}, item, {
        content: item.content + text,
        statusText: "",
        renderMode: "text",
      });
    });
    this.setData({ messages });
  },

  flushTypewriterBuffer() {
    if (!this._typewriterBuffer) return;
    const remaining = this._typewriterBuffer;
    this._typewriterBuffer = "";
    this.appendAssistantText(remaining);
  },

  completeAssistantMessage(countQa) {
    this.clearWaitingTimer();
    this.clearTypewriterTimer();
    this._typewriterDonePending = false;
    const messages = this.data.messages.map((item, index) => {
      if (index !== this.data.messages.length - 1 || !item.streaming) return item;
      return Object.assign({}, item, {
        nodes: markdownToNodes(item.content || ""),
        streaming: false,
        statusText: "",
        renderMode: "markdown",
      });
    });
    if (countQa && !this._streamFinishedCounted) {
      storage.incrementQaCount();
      this._streamFinishedCounted = true;
    }
    this.setData({ messages, pageState: "ready", inputDisabled: false });
  },

  updateStreamingAssistant(patch) {
    const messages = this.data.messages.map((item, index) => {
      if (index !== this.data.messages.length - 1 || !item.streaming) return item;
      return Object.assign({}, item, patch);
    });
    this.setData({ messages });
  },

  clearWaitingTimer() {
    if (this._waitingTimer) {
      clearInterval(this._waitingTimer);
      this._waitingTimer = null;
    }
  },

  clearTypewriterTimer() {
    if (this._typewriterTimer) {
      clearInterval(this._typewriterTimer);
      this._typewriterTimer = null;
    }
  },

  stopStream() {
    if (this._stream) {
      this._stream.abort();
      this._stream = null;
    }
    this.clearWaitingTimer();
    this.flushTypewriterBuffer();
    this.clearTypewriterTimer();
    const messages = this.data.messages.map((item, index) => {
      if (index !== this.data.messages.length - 1 || !item.streaming) return item;
      const content = item.content || "已停止生成。";
      return Object.assign({}, item, {
        content,
        nodes: markdownToNodes(content),
        streaming: false,
        statusText: "",
        renderMode: "markdown",
      });
    });
    this._typewriterBuffer = "";
    this._typewriterDonePending = false;
    this.setData({ messages, pageState: "ready", inputDisabled: false });
  },

  dismissError() {
    this.setData({ errorMessage: "" });
  },

  retryChart() {
    this.prepareChart();
  },

  goBack() {
    wx.navigateBack({
      fail() {
        wx.redirectTo({ url: "/pages/home/index" });
      },
    });
  },

  goToAccount() {
    wx.navigateTo({ url: "/pages/account/index" });
  },

  goToPricing() {
    wx.navigateTo({ url: "/pages/pricing/index" });
  },

  onUnload() {
    if (this._stream) {
      this._stream.abort();
      this._stream = null;
    }
    this.clearWaitingTimer();
    this.clearTypewriterTimer();
  },

  showModal(icon, title, message, buttons) {
    this.setData({ modal: { visible: true, icon, title, message, buttons } });
  },

  closeModal() {
    this.setData({ "modal.visible": false });
  },

  onModalAction(event) {
    const action = event.detail.action;
    this.closeModal();
    if (action === "startCalibration") {
      wx.redirectTo({ url: "/pages/calibration/index" });
    }
  },

  onShareAppMessage() {
    return {
      title: "顺顺尼命理问答",
      path: "/pages/home/index",
    };
  },

  onShareTimeline() {
    return {
      title: "顺顺尼命理问答",
      query: "",
    };
  },
});
