const storage = require("../../utils/storage");

function getSubscriptionStatus(subscription) {
  if (!subscription || !subscription.expiryDate) {
    return { isActive: false, daysRemaining: 0, showExpiry: false, text: "" };
  }

  const today = new Date();
  const expiryDate = new Date(subscription.expiryDate);
  const daysRemaining = Math.ceil((expiryDate - today) / (1000 * 60 * 60 * 24));
  return {
    isActive: daysRemaining > 0,
    daysRemaining,
    showExpiry: daysRemaining > 0 && daysRemaining <= 7,
    text: `会员还剩 ${daysRemaining} 天到期`,
  };
}

Page({
  data: {
    currentUser: null,
    userDisplayName: "有缘人",
    profiles: [],
    profileCount: 0,
    selectedProfileId: "",
    selectedProfile: null,
    quickInput: "",
    qaCount: 0,
    subscriptionStatus: getSubscriptionStatus(null),
    modal: {
      visible: false,
      icon: "",
      title: "",
      message: "",
      buttons: [],
    },
  },

  onShow() {
    if (!storage.isRegistered() || storage.getProfiles().length === 0) {
      wx.redirectTo({ url: "/pages/register/index" });
      return;
    }

    this.refreshPage();
  },

  refreshPage() {
    const rawProfiles = storage.getProfiles();
    let selectedProfile = storage.getSelectedProfile();

    if (!selectedProfile && rawProfiles.length) {
      selectedProfile = rawProfiles[0];
      storage.setSelectedProfile(selectedProfile.id);
    }

    const currentUser = storage.getCurrentUser() || {};
    const profiles = rawProfiles.map(profile => Object.assign({}, profile, {
      avatarText: (profile.name || "?").slice(0, 1),
    }));

    this.setData({
      currentUser,
      userDisplayName: currentUser.phone || "有缘人",
      profiles,
      profileCount: profiles.length,
      selectedProfileId: selectedProfile ? selectedProfile.id : "",
      selectedProfile,
      qaCount: storage.getQaCount(),
      subscriptionStatus: getSubscriptionStatus(storage.getSubscription()),
    });
  },

  selectProfile(event) {
    const profileId = event.currentTarget.dataset.id;
    storage.setSelectedProfile(profileId);
    this.refreshPage();
  },

  handleQuickInput(event) {
    this.setData({ quickInput: event.detail.value });
  },

  submitQuickQA() {
    const question = (this.data.quickInput || "").trim();
    if (!question) {
      wx.showToast({ title: "请输入问题", icon: "none" });
      return;
    }
    this.goToQAWithQuestion(question);
  },

  quickAsk(event) {
    this.goToQAWithQuestion(event.currentTarget.dataset.question);
  },

  goToQAWithQuestion(question) {
    if (!this.ensureReadyProfile("qa")) return;
    wx.navigateTo({ url: `/pages/qa/index?question=${encodeURIComponent(question)}` });
  },

  addProfile() {
    this.showModal("+", "添加新档案", "请为家人录入八字信息", [
      { text: "取消", action: "close" },
      { text: "开始录入", action: "newProfile", primary: true },
    ]);
  },

  goToQA() {
    if (!this.ensureReadyProfile("qa")) return;
    wx.navigateTo({ url: "/pages/qa/index" });
  },

  viewChart() {
    if (!this.ensureReadyProfile("chart")) return;
    wx.navigateTo({ url: "/pages/chart/index" });
  },

  ensureReadyProfile(target) {
    const profile = this.data.selectedProfile;
    if (!profile) {
      this.showModal("!", "请先选择档案", "", [
        { text: "确定", action: "close", primary: true },
      ]);
      return false;
    }

    if (profile.calibrationStatus !== "success") {
      this.showModal("!", "命盘未校准", target === "chart" ? "请先完成命盘校准，才能查看详细分析" : "请先完成命盘校准，才能使用问答功能", [
        { text: "开始校准", action: "startCalibration", primary: true },
      ]);
      return false;
    }

    return true;
  },

  goToAccount() {
    wx.navigateTo({ url: "/pages/account/index" });
  },

  goToPricing() {
    wx.navigateTo({ url: "/pages/pricing/index" });
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

    if (action === "newProfile") {
      wx.navigateTo({ url: "/pages/register/index?mode=add" });
    } else if (action === "startCalibration") {
      wx.navigateTo({ url: "/pages/calibration/index" });
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
