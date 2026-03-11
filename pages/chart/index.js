const storage = require("../../utils/storage");
const { CHART_PALACES, CHART_DETAILS } = require("../../utils/mock");

Page({
  data: {
    profile: {},
    palaces: CHART_PALACES,
    details: CHART_DETAILS,
  },

  onShow() {
    if (!storage.isVerified()) {
      wx.reLaunch({
        url: "/pages/welcome/index",
      });
      return;
    }

    this.setData({
      profile: storage.getProfile(),
    });
  },
});
