const storage = require("../../utils/storage");
const format = require("../../utils/format");

const GENDERS = ["男", "女"];

Page({
  data: {
    step: 1,
    genders: GENDERS,
    genderIndex: 0,
    selectedGender: GENDERS[0],
    phone: "",
    birthDate: "",
    birthDateText: "请选择出生日期",
    today: format.getCurrentDate(),
    timeOptions: format.getTimeOptions(),
    timeOptionIndex: 6,
    selectedTimeLabel: format.getTimeOptions()[6].label,
    profileName: "本人",
    isAddMode: false,
    modal: {
      visible: false,
      icon: "",
      title: "",
      message: "",
      buttons: [],
    },
  },

  onLoad(options) {
    const currentUser = storage.getCurrentUser();
    const hasProfiles = storage.getProfiles().length > 0;
    const isAddMode = options && options.mode === "add";

    if (currentUser && hasProfiles && !isAddMode) {
      wx.redirectTo({ url: "/pages/home/index" });
      return;
    }

    const gender = currentUser && currentUser.gender ? currentUser.gender : "男";
    const genderIndex = Math.max(GENDERS.indexOf(gender), 0);

    this.setData({
      isAddMode,
      phone: currentUser && currentUser.phone ? currentUser.phone : "",
      genderIndex,
      selectedGender: GENDERS[genderIndex],
      profileName: isAddMode ? "" : "本人",
    });
  },

  handlePhoneInput(event) {
    this.setData({ phone: event.detail.value });
  },

  handleGenderChange(event) {
    const genderIndex = Number(event.detail.value);
    this.setData({
      genderIndex,
      selectedGender: GENDERS[genderIndex],
    });
  },

  handleDateChange(event) {
    this.setData({
      birthDate: event.detail.value,
      birthDateText: event.detail.value,
    });
  },

  handleTimeChange(event) {
    const timeOptionIndex = Number(event.detail.value);
    this.setData({
      timeOptionIndex,
      selectedTimeLabel: this.data.timeOptions[timeOptionIndex].label,
    });
  },

  handleProfileNameInput(event) {
    this.setData({ profileName: event.detail.value });
  },

  goToStep(event) {
    const step = Number(event.currentTarget.dataset.step);
    this.setData({ step });
  },

  handleNextStep() {
    if (!this.data.phone.trim()) {
      this.showModal("!", "信息不完整", "请输入手机号码", [
        { text: "确定", action: "close", primary: true },
      ]);
      return;
    }

    this.setData({ step: 2 });
  },

  completeRegistration() {
    const { birthDate, timeOptions, timeOptionIndex, profileName, phone, genders, genderIndex, isAddMode } = this.data;
    const timeOption = timeOptions[timeOptionIndex];
    const name = (profileName || "").trim() || "本人";
    const gender = genders[genderIndex] || "男";

    if (!birthDate || !timeOption) {
      this.showModal("!", "信息不完整", "请选择出生日期和出生时辰", [
        { text: "确定", action: "close", primary: true },
      ]);
      return;
    }

    const currentUser = storage.getCurrentUser();
    const user = storage.saveCurrentUser({
      id: currentUser && currentUser.id ? currentUser.id : storage.genId("user"),
      phone: phone.trim(),
      gender,
      registeredAt: currentUser && currentUser.registeredAt ? currentUser.registeredAt : format.getCurrentDate(),
    });

    storage.addProfile({
      name,
      gender,
      birthDate,
      timeIndex: timeOption.timeIndex,
      timeLabel: timeOption.label,
      userId: user.id,
      calibrationStatus: "pending",
      accuracy: 0,
      chartKey: "",
      chartData: null,
    });

    this.showModal("✨", isAddMode ? "档案已添加" : "注册成功", "现在通过两道生活化问题验证命盘", [
      { text: "开始校准", action: "startCalibration", primary: true },
    ]);
  },

  showModal(icon, title, message, buttons) {
    this.setData({
      modal: { visible: true, icon, title, message, buttons },
    });
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
});
