const BASE_URL = "https://bianyuan.art";

function getChartKey(profile) {
  if (!profile) return "";
  return [profile.birthDate, profile.timeIndex, profile.gender].join("|");
}

function buildPayload(profile) {
  return {
    birthDate: profile.birthDate,
    timeIndex: Number(profile.timeIndex),
    gender: profile.gender || "男",
  };
}

function normalizeChartResponse(res) {
  const responseData = res && res.data && (res.data.data || res.data);
  if (!responseData || !responseData.bySolar) {
    throw new Error("命盘数据为空");
  }
  return {
    bySolar: responseData.bySolar,
    majorPeriods: responseData.majorPeriods || [],
    yearlyPeriods: responseData.yearlyPeriods || [],
  };
}

function fetchChart(profile) {
  const payload = buildPayload(profile);
  return new Promise((resolve, reject) => {
    wx.request({
      url: `${BASE_URL}/api/aiData`,
      method: "POST",
      timeout: 60000,
      header: { "Content-Type": "application/json" },
      data: payload,
      success(res) {
        if (res.statusCode !== 200) {
          reject(new Error(`命盘接口异常：${res.statusCode}`));
          return;
        }

        try {
          resolve(normalizeChartResponse(res));
        } catch (err) {
          reject(err);
        }
      },
      fail(err) {
        reject(new Error(err.errMsg || "命盘请求失败"));
      },
    });
  });
}

module.exports = {
  BASE_URL,
  getChartKey,
  buildPayload,
  fetchChart,
};
