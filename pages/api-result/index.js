const storage = require("../../utils/storage");
const format = require("../../utils/format");

Page({
  data: {
    loading: true,
    error: "",
    resultText: "",
    requestPayload: null,
    displayProfile: null,
  },

  onLoad() {
    if (!storage.isVerified()) {
      wx.reLaunch({
        url: "/pages/welcome/index",
      });
      return;
    }

    const profile = storage.getProfile();
    const birthHour = Number(profile.birthHour);
    const backendTimeIndex = format.getBackendTimeIndex(birthHour);
    const requestPayload = {
      birthDate: profile.birthDate,
      timeIndex: backendTimeIndex,
      gender: profile.gender,
      profession: profile.profession,
      birthHour,
      birthTimeLabel: profile.shichen,
    };

    this.setData({
      requestPayload,
      displayProfile: {
        gender: profile.gender,
        birthDate: profile.birthDate,
        timeText: format.getTimeLabel(birthHour),
        profession: profile.profession,
        backendTimeIndex,
      },
    });

    this.fetchApiResult(requestPayload);
  },

  fetchApiResult(requestPayload) {
    this.setData({
      loading: true,
      error: "",
      resultText: "",
    });

    wx.request({
      url: "https://bianyuan.art/api/aiData",
      method: "POST",
      timeout: 60000,
      header: {
        "Content-Type": "application/json",
      },
      data: requestPayload,
      success: (res) => {
        const resultText = this.normalizeResponse(res.data);

        if (!resultText) {
          this.setData({
            loading: false,
            error: "接口已返回，但没有可显示的文本内容。",
          });
          return;
        }

        storage.appendHistory({
          type: "接口返回",
          date: new Date().toISOString().slice(0, 10),
          summary: `接口分析已返回：${resultText.slice(0, 24)}${resultText.length > 24 ? "..." : ""}`,
        });

        this.setData({
          loading: false,
          resultText,
        });
      },
      fail: (error) => {
        const errorMessage = error && error.errMsg ? error.errMsg : "请求失败，请稍后重试。";
        this.setData({
          loading: false,
          error: errorMessage,
        });
      },
    });
  },

  normalizeResponse(data) {
    if (!data) {
      return "";
    }

    if (typeof data === "string") {
      return data;
    }

    if (typeof data.text === "string") {
      return data.text;
    }

    if (typeof data.content === "string") {
      return data.content;
    }

    if (typeof data.message === "string") {
      return data.message;
    }

    if (typeof data.result === "string") {
      return data.result;
    }

    if (data.data && typeof data.data === "string") {
      return data.data;
    }

    if (data.data && typeof data.data.text === "string") {
      return data.data.text;
    }

    if (data.data && typeof data.data.content === "string") {
      return data.data.content;
    }

    try {
      return JSON.stringify(data, null, 2);
    } catch (error) {
      return "";
    }
  },

  handleRetry() {
    if (!this.data.requestPayload) {
      return;
    }

    this.fetchApiResult(this.data.requestPayload);
  },
});