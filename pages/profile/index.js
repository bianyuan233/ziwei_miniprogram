const storage = require("../../utils/storage");

Page({
  data: {
    profile: {},
    isPaid: false,
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
    });
  },

  handleUpgrade() {
    storage.setPaid(true);
    storage.saveProfile({
      memberType: "月度会员",
      memberExpireAt: "2026-04-11",
    });
    this.refreshPage();

    wx.showToast({
      title: "升级成功",
      icon: "success",
    });
  },

  handlePolicy() {
    wx.showModal({
      title: "隐私政策",
      content: "当前为原型工程版，后续可补充正式隐私政策页面与用户授权说明。",
      showCancel: false,
    });
  },

  handleContact() {
    wx.showModal({
      title: "联系我们",
      content: "如需继续开发，可补充客服入口、反馈表单、企业微信或公众号联动。",
      showCancel: false,
    });
  },

  handleReset() {
    wx.showModal({
      title: "清空所有数据",
      content: "将重置生辰录入、命盘校准、解锁状态，是否继续？",
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
  },
});
