const storage = require("../../utils/storage");
const chartService = require("../../utils/chartService");

function starNames(stars) {
  if (!Array.isArray(stars) || !stars.length) return "无";
  return stars.slice(0, 4).map(star => {
    const brightness = star.brightness ? `(${star.brightness})` : "";
    return `${star.name}${brightness}`;
  }).join("、");
}

function formatPillar(raw, key) {
  const pair = raw && raw.chineseDate && raw.chineseDate[key];
  if (!Array.isArray(pair) || pair.length < 2) return "-";
  return `${pair[0]}${pair[1]}`;
}

function prepareChartView(chart) {
  const bySolar = chart.bySolar || {};
  const rawDates = bySolar.rawDates || {};

  return {
    summary: {
      name: bySolar.chineseDate || "-",
      solarDate: bySolar.solarDate || "-",
      lunarDate: bySolar.lunarDate || "-",
      time: bySolar.time || "-",
      zodiac: bySolar.zodiac || "-",
      sign: bySolar.sign || "-",
      soul: bySolar.soul || "-",
      body: bySolar.body || "-",
      fiveElementsClass: bySolar.fiveElementsClass || "-",
    },
    pillars: [
      { label: "年", value: formatPillar(rawDates, "yearly") },
      { label: "月", value: formatPillar(rawDates, "monthly") },
      { label: "日", value: formatPillar(rawDates, "daily") },
      { label: "时", value: formatPillar(rawDates, "hourly") },
    ],
    palaces: (bySolar.palaces || []).map(palace => ({
      index: palace.index,
      name: palace.name,
      branch: `${palace.heavenlyStem || ""}${palace.earthlyBranch || ""}`,
      mainStars: starNames(palace.majorStars),
      minorStars: starNames(palace.minorStars),
      tags: [
        palace.isOriginalPalace ? "命宫" : "",
        palace.isBodyPalace ? "身宫" : "",
      ].filter(Boolean).join(" · "),
    })),
    majorPeriodItems: (chart.majorPeriods || []).slice(0, 4).map(period => ({
      rangeText: Array.isArray(period.range) ? `${period.range[0]}-${period.range[1]}岁` : "-",
      palaceText: (period.palaces || []).slice(0, 4).map(item => item.name).join("、") || "-",
    })),
    yearlyPeriodItems: (chart.yearlyPeriods || []).slice(0, 4).map(period => ({
      ageText: period.age ? `${period.age}岁` : "-",
      palaceText: (period.palaces || []).slice(0, 4).map(item => `${item.month || "-"}月${item.name}`).join("、") || "-",
    })),
  };
}

Page({
  data: {
    profile: null,
    pageState: "loading",
    errorMessage: "",
    summary: null,
    pillars: [],
    palaces: [],
    majorPeriodItems: [],
    yearlyPeriodItems: [],
    modal: {
      visible: false,
      icon: "",
      title: "",
      message: "",
      buttons: [],
    },
  },

  onLoad() {
    const profile = storage.getSelectedProfile();
    if (!profile) {
      wx.redirectTo({ url: "/pages/register/index" });
      return;
    }

    this.setData({ profile });

    if (profile.calibrationStatus !== "success") {
      this.showModal("!", "命盘未校准", "请先完成命盘校准，才能查看详细分析", [
        { text: "开始校准", action: "startCalibration", primary: true },
      ]);
      return;
    }

    this.loadChart();
  },

  loadChart() {
    const profile = storage.getSelectedProfile();
    const chartKey = chartService.getChartKey(profile);
    this.setData({ pageState: "loading", errorMessage: "" });

    if (profile.chartData && profile.chartKey === chartKey) {
      this.renderChart(profile.chartData);
      return;
    }

    chartService.fetchChart(profile).then(chart => {
      storage.saveChartForProfile(profile.id, chart, chartKey);
      this.renderChart(chart);
    }).catch(err => {
      this.setData({
        pageState: "error",
        errorMessage: err.message || "命盘加载失败，请重试",
      });
    });
  },

  renderChart(chart) {
    const view = prepareChartView(chart);
    this.setData({
      pageState: "ready",
      summary: view.summary,
      pillars: view.pillars,
      palaces: view.palaces,
      majorPeriodItems: view.majorPeriodItems,
      yearlyPeriodItems: view.yearlyPeriodItems,
    });
  },

  goBack() {
    wx.navigateBack({
      fail() {
        wx.redirectTo({ url: "/pages/home/index" });
      },
    });
  },

  goToQA() {
    wx.navigateTo({ url: "/pages/qa/index" });
  },

  retry() {
    this.loadChart();
  },

  showTimelineTip() {
    wx.showToast({ title: "可使用右上角菜单分享到朋友圈", icon: "none" });
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
    const profile = this.data.profile || {};
    return {
      title: `分享${profile.name || "我"}的命盘分析`,
      path: "/pages/home/index",
    };
  },

  onShareTimeline() {
    const profile = this.data.profile || {};
    return {
      title: `分享${profile.name || "我"}的命盘分析`,
      query: "",
    };
  },
});
