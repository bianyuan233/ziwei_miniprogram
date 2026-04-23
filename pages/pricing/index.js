const storage = require("../../utils/storage");

const PLANS = [
  {
    key: "trial",
    title: "试用卡",
    price: "¥9.9",
    period: "3天有效期",
    durationDays: 3,
    features: ["3次深度问答", "每日运势播报", "优先客服支持"],
  },
  {
    key: "monthly",
    title: "月卡",
    badge: "推荐",
    price: "¥29.9",
    period: "30天有效期",
    durationDays: 30,
    highlighted: true,
    features: ["无限深度问答", "每日运势播报", "周度运势分析", "优先客服支持"],
  },
  {
    key: "annual",
    title: "年卡",
    price: "¥199",
    period: "365天有效期",
    durationDays: 365,
    features: ["无限所有服务", "私密顾问通道", "月度深度分析", "优先客服支持"],
  },
];

function formatDate(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

Page({
  data: {
    plans: PLANS,
    selectedPlan: "",
    modal: {
      visible: false,
      icon: "",
      title: "",
      message: "",
      buttons: [],
    },
  },

  goBack() {
    wx.navigateBack({
      fail() {
        wx.redirectTo({ url: "/pages/home/index" });
      },
    });
  },

  selectPlan(event) {
    this.setData({ selectedPlan: event.currentTarget.dataset.key });
  },

  processPay() {
    const plan = PLANS.find(item => item.key === this.data.selectedPlan);
    if (!plan) {
      this.showModal("!", "请选择一个套餐", "", [
        { text: "确定", action: "close", primary: true },
      ]);
      return;
    }

    this.showModal("💳", "确认支付", `即将支付：${plan.title}（${plan.price} / ${plan.period}）`, [
      { text: "支付宝支付", action: "paySuccess", primary: true },
      { text: "微信支付", action: "paySuccess", primary: true },
      { text: "取消", action: "close" },
    ]);
  },

  paymentSuccess() {
    const plan = PLANS.find(item => item.key === this.data.selectedPlan);
    if (!plan) return;

    const today = new Date();
    const expiryDate = new Date(today.getTime() + plan.durationDays * 24 * 60 * 60 * 1000);
    const record = {
      plan: plan.key,
      purchaseDate: formatDate(today),
      expiryDate: formatDate(expiryDate),
    };

    storage.setSubscription(record);
    storage.addPaymentRecord(record);

    this.showModal("✓", "支付成功", "感谢你的支持！现在可以使用会员功能。", [
      { text: "返回", action: "returnBack", primary: true },
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

    if (action === "paySuccess") {
      this.paymentSuccess();
    } else if (action === "returnBack") {
      this.goBack();
    }
  },
});
