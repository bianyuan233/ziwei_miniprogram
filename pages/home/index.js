const storage = require("../../utils/storage");
const {
  DAILY_FORTUNE,
  SERVICE_MENU,
  CONTENT_DETAILS,
  YEARLY_RECORDS,
  PAYMENT_OPTIONS,
} = require("../../utils/mock");

Page({
  data: {
    profile: {},
    dailyFortune: DAILY_FORTUNE,
    serviceMenu: SERVICE_MENU,
    isPaid: false,
    showSheet: false,
    sheetMode: "",
    sheetTitle: "",
    selectedPlan: "single",
    activeService: "",
    paymentOptions: PAYMENT_OPTIONS,
    contentDetail: null,
    yearlyRecords: YEARLY_RECORDS,
    historyRecords: [],
  },

  onShow() {
    if (!storage.isVerified()) {
      wx.reLaunch({
        url: "/pages/welcome/index",
      });
      return;
    }

    this.refreshPage();
  },

  refreshPage() {
    this.setData({
      profile: storage.getProfile(),
      isPaid: storage.isPaid(),
      historyRecords: storage.getHistory(),
    });
  },

  handleServiceTap(event) {
    const key = event.currentTarget.dataset.key;

    if (key === "api") {
      wx.navigateTo({
        url: "/pages/api-result/index",
      });
      return;
    }

    if (key === "reset") {
      wx.showModal({
        title: "重新验盘",
        content: "这会清空当前命盘校准记录，是否继续？",
        success: ({ confirm }) => {
          if (!confirm) {
            return;
          }

          storage.clearAll();
          wx.reLaunch({
            url: "/pages/welcome/index",
          });
        },
      });
      return;
    }

    if (key === "yearly") {
      this.setData({
        showSheet: true,
        sheetMode: "yearly",
        sheetTitle: "流年运势记录",
      });
      return;
    }

    if (key === "history") {
      this.setData({
        showSheet: true,
        sheetMode: "history",
        sheetTitle: "历史解读记录",
      });
      return;
    }

    if (!this.data.isPaid) {
      this.setData({
        showSheet: true,
        sheetMode: "payment",
        sheetTitle: "选择解读方案",
        activeService: key,
      });
      return;
    }

    this.openContentSheet(key);
  },

  openContentSheet(key) {
    const contentDetail = CONTENT_DETAILS[key];
    if (!contentDetail) {
      return;
    }

    this.setData({
      showSheet: true,
      sheetMode: "content",
      sheetTitle: contentDetail.title,
      contentDetail,
      activeService: key,
    });
  },

  handleSelectPlan(event) {
    this.setData({
      selectedPlan: event.currentTarget.dataset.key,
    });
  },

  handlePayConfirm() {
    storage.setPaid(true);

    if (this.data.selectedPlan === "member") {
      storage.saveProfile({
        memberType: "月度会员",
        memberExpireAt: "2026-04-11",
      });
    }

    storage.appendHistory({
      type: "解读解锁",
      date: new Date().toISOString().slice(0, 10),
      summary: `${this.data.activeService || "深度分析"} 已解锁`,
    });

    this.refreshPage();
    wx.showToast({
      title: "解锁成功",
      icon: "success",
    });

    setTimeout(() => {
      this.openContentSheet(this.data.activeService || "deep");
    }, 300);
  },

  noop() {},

  closeSheet() {
    this.setData({
      showSheet: false,
      sheetMode: "",
      sheetTitle: "",
      contentDetail: null,
    });
  },
});