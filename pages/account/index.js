const storage = require("../../utils/storage");

const PLAN_INFO = {
  trial: { name: "试用卡", price: "¥9.9" },
  monthly: { name: "月卡", price: "¥29.9" },
  annual: { name: "年卡", price: "¥199" },
};

const FEEDBACK_TYPES = ["功能问题", "功能建议", "投诉建议", "其他"];

function getSubscriptionView(subscription) {
  if (!subscription || !subscription.plan) {
    return {
      planName: "免费用户",
      statusText: "未激活",
      detail: "升级会员，解锁更多深度洞察功能",
      expired: false,
    };
  }

  const today = new Date();
  const expiryDate = new Date(subscription.expiryDate);
  const daysRemaining = Math.ceil((expiryDate - today) / (1000 * 60 * 60 * 24));
  const isActive = daysRemaining > 0;
  const planInfo = PLAN_INFO[subscription.plan] || { name: "-" };

  return {
    planName: planInfo.name,
    statusText: isActive ? "活跃中" : "已过期",
    detail: `有效期至：${subscription.expiryDate} · 剩余 ${Math.max(daysRemaining, 0)} 天`,
    expired: !isActive,
  };
}

Page({
  data: {
    currentUser: null,
    phoneText: "-",
    genderText: "-",
    registeredAtText: "-",
    profileCount: 0,
    subscriptionView: getSubscriptionView(null),
    paymentRecords: [],
    hasPaymentRecords: false,
    feedbackTypes: FEEDBACK_TYPES,
    feedbackTypeIndex: -1,
    feedbackTypeText: "请选择",
    feedbackContent: "",
    feedbackContact: "",
    showFeedback: false,
    modal: {
      visible: false,
      icon: "",
      title: "",
      message: "",
      buttons: [],
    },
  },

  onShow() {
    if (!storage.isRegistered()) {
      wx.redirectTo({ url: "/pages/register/index" });
      return;
    }
    this.refreshPage();
  },

  refreshPage() {
    const paymentRecords = storage.getPaymentHistory().map(record => ({
      planName: PLAN_INFO[record.plan] ? PLAN_INFO[record.plan].name : "-",
      amount: PLAN_INFO[record.plan] ? PLAN_INFO[record.plan].price : "-",
      purchaseDate: record.purchaseDate,
      expiryDate: record.expiryDate,
    }));

    const currentUser = storage.getCurrentUser() || {};

    this.setData({
      currentUser,
      phoneText: currentUser.phone || "-",
      genderText: currentUser.gender || "-",
      registeredAtText: currentUser.registeredAt || "-",
      profileCount: storage.getProfiles().length,
      subscriptionView: getSubscriptionView(storage.getSubscription()),
      paymentRecords,
      hasPaymentRecords: paymentRecords.length > 0,
    });
  },

  goBack() {
    wx.navigateBack({
      fail() {
        wx.redirectTo({ url: "/pages/home/index" });
      },
    });
  },

  goToPricing() {
    wx.navigateTo({ url: "/pages/pricing/index" });
  },

  goToPolicy() {
    wx.navigateTo({ url: "/pages/policy/index" });
  },

  showServiceCenter() {
    this.showModal("☎", "客服中心", "请选择需要的服务", [
      { text: "在线客服", action: "onlineService", primary: true },
      { text: "提交反馈", action: "submitFeedback", primary: true },
      { text: "常见问题", action: "commonQuestions" },
    ]);
  },

  showFeedbackForm() {
    this.setData({
      showFeedback: true,
      feedbackTypeIndex: -1,
      feedbackTypeText: "请选择",
      feedbackContent: "",
      feedbackContact: "",
    });
  },

  closeFeedback() {
    this.setData({ showFeedback: false });
  },

  handleFeedbackTypeChange(event) {
    const feedbackTypeIndex = Number(event.detail.value);
    this.setData({
      feedbackTypeIndex,
      feedbackTypeText: FEEDBACK_TYPES[feedbackTypeIndex],
    });
  },

  handleFeedbackContent(event) {
    this.setData({ feedbackContent: event.detail.value });
  },

  handleFeedbackContact(event) {
    this.setData({ feedbackContact: event.detail.value });
  },

  submitFeedback() {
    if (this.data.feedbackTypeIndex < 0 || !this.data.feedbackContent.trim()) {
      wx.showToast({ title: "请填写必填项", icon: "none" });
      return;
    }

    this.setData({ showFeedback: false });
    this.showModal("✓", "反馈已提交", "感谢你的反馈！我们会认真审阅并持续改进。", [
      { text: "确定", action: "close", primary: true },
    ]);
  },

  noop() {},

  handleReset() {
    this.showModal("!", "清空本地数据", "将重置注册、档案、会员和本机统计，是否继续？", [
      { text: "取消", action: "close" },
      { text: "清空", action: "resetAll", primary: true },
    ]);
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

    if (action === "onlineService") {
      this.showModal("☎", "在线客服", "客服微信：fortune_life_2024\n工作时间：9:00-21:00", [
        { text: "复制微信号", action: "copyWechatId", primary: true },
        { text: "关闭", action: "close" },
      ]);
    } else if (action === "copyWechatId") {
      wx.setClipboardData({ data: "fortune_life_2024" });
    } else if (action === "submitFeedback") {
      this.showFeedbackForm();
    } else if (action === "commonQuestions") {
      this.showModal("?", "常见问题", "Q: 如何确保出生时间准确？\nA: 建议查询出生证明或询问家人。\n\nQ: 命理分析有科学依据吗？\nA: 本服务仅供参考，不构成投资、医疗或法律建议。\n\nQ: 如何修改档案？\nA: 当前版本可新增档案；编辑能力后续补充。", [
        { text: "确定", action: "close", primary: true },
      ]);
    } else if (action === "resetAll") {
      storage.clearAll();
      wx.redirectTo({ url: "/pages/register/index" });
    }
  },
});
