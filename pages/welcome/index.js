const storage = require("../../utils/storage");
const format = require("../../utils/format");

const GENDERS = ["男", "女"];
const PROFESSIONS = [
  "互联网/软件",
  "产品/运营",
  "设计/创意",
  "市场/销售",
  "行政/人事",
  "财务/会计",
  "教师/培训",
  "医生/护士",
  "律师/法务",
  "公务员/事业单位",
  "制造业/工厂",
  "建筑/工程",
  "电商/客服",
  "媒体/自媒体",
  "餐饮/服务业",
  "学生",
  "自由职业",
  "个体经营/创业",
  "退休",
  "其他",
];

Page({
  data: {
    genders: GENDERS,
    genderIndex: 0,
    professions: PROFESSIONS,
    professionIndex: 0,
    birthDate: "",
    birthHour: 12,
    timeLabel: format.getTimeLabel(12),
    today: format.getCurrentDate(),
  },

  onLoad() {
    const profile = storage.getProfile();
    const birthDate = profile.birthDate || format.getCurrentDate();
    const birthHour = typeof profile.birthHour === "number" ? profile.birthHour : 12;
    const gender = profile.gender || GENDERS[0];
    const profession = profile.profession || PROFESSIONS[0];
    const genderIndex = Math.max(GENDERS.indexOf(gender), 0);
    const professionIndex = Math.max(PROFESSIONS.indexOf(profession), 0);

    this.setData({
      birthDate,
      birthHour,
      genderIndex,
      professionIndex,
      timeLabel: format.getTimeLabel(birthHour),
    });
  },

  onShow() {
    if (storage.isVerified()) {
      wx.switchTab({
        url: "/pages/home/index",
      });
    }
  },

  handleGenderChange(event) {
    this.setData({
      genderIndex: Number(event.detail.value),
    });
  },

  handleDateChange(event) {
    this.setData({
      birthDate: event.detail.value,
    });
  },

  updateHour(hour) {
    const birthHour = Number(hour);
    this.setData({
      birthHour,
      timeLabel: format.getTimeLabel(birthHour),
    });
  },

  handleHourChanging(event) {
    this.updateHour(event.detail.value);
  },

  handleHourChange(event) {
    this.updateHour(event.detail.value);
  },

  handleProfessionChange(event) {
    this.setData({
      professionIndex: Number(event.detail.value),
    });
  },

  handleStart() {
    const { birthDate, birthHour, genders, genderIndex, professions, professionIndex } = this.data;

    if (!birthDate) {
      wx.showToast({
        title: "请选择出生日期",
        icon: "none",
      });
      return;
    }

    storage.saveProfile({
      gender: genders[genderIndex],
      profession: professions[professionIndex],
      birthDate,
      birthHour,
      shichen: format.getShichenByHour(birthHour),
    });

    wx.navigateTo({
      url: "/pages/verify/index",
    });
  },
});