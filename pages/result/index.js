const storage = require("../../utils/storage");
const { CHART_PALACES } = require("../../utils/mock");

Page({
  data: {
    score: 98,
    yesCount: 3,
    palaces: CHART_PALACES,
    ruleText: "因你确认了成长突破、情感节点与事业进阶，系统已排除偏差时辰，锁定午时命盘模型。迁移宫与官禄宫的信号更清晰，说明换环境与承担责任常常一起出现。",
  },

  onLoad(options) {
    this.setData({
      score: Number(options.score) || 98,
      yesCount: Number(options.yesCount) || 3,
    });
  },

  handleComplete() {
    const profile = storage.getProfile();
    storage.setVerified(true);
    storage.appendHistory({
      type: "命盘校准",
      date: new Date().toISOString().slice(0, 10),
      summary: `${profile.birthDate || "未填写"} ${profile.shichen || "午时"} 命盘校准完成`,
    });

    wx.showToast({
      title: "验盘完成",
      icon: "success",
    });

    setTimeout(() => {
      wx.switchTab({
        url: "/pages/home/index",
      });
    }, 500);
  },

  handleRetry() {
    wx.redirectTo({
      url: "/pages/welcome/index",
    });
  },
});
