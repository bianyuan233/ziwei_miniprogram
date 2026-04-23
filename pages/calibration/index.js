const storage = require("../../utils/storage");
const calibrationService = require("../../utils/calibrationService");

Page({
  data: {
    profile: null,
    questions: [],
    currentIndex: 0,
    currentQuestion: null,
    answers: [],
    selectedOption: -1,
    progress: 0,
    loading: false,
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

    const questions = calibrationService.getQuestions();
    this.setData({
      profile,
      questions,
      currentQuestion: questions[0],
      progress: Math.round((1 / questions.length) * 100),
    });
  },

  updateQuestion(index) {
    const answers = this.data.answers;
    const selectedOption = typeof answers[index] === "number" ? answers[index] : -1;
    this.setData({
      currentIndex: index,
      currentQuestion: this.data.questions[index],
      selectedOption,
      progress: Math.round(((index + 1) / this.data.questions.length) * 100),
    });
  },

  selectOption(event) {
    if (this.data.loading) return;
    const optionIndex = Number(event.currentTarget.dataset.index);
    const answers = this.data.answers.slice();
    answers[this.data.currentIndex] = optionIndex;
    this.setData({ answers, selectedOption: optionIndex });
  },

  nextQuestion() {
    if (this.data.selectedOption < 0) {
      this.showModal("!", "请选择一个选项", "", [
        { text: "确定", action: "close", primary: true },
      ]);
      return;
    }

    if (this.data.currentIndex < this.data.questions.length - 1) {
      this.updateQuestion(this.data.currentIndex + 1);
      return;
    }

    this.completeCalibration();
  },

  prevQuestion() {
    if (this.data.currentIndex <= 0) return;
    this.updateQuestion(this.data.currentIndex - 1);
  },

  completeCalibration() {
    this.setData({ loading: true });
    calibrationService.submitAnswers(this.data.answers).then(result => {
      storage.updateProfile(this.data.profile.id, {
        calibrationStatus: result.status,
        accuracy: result.accuracy,
      });
      this.setData({ loading: false });
      this.showModal("✓", "命盘校准成功", `准确度 ${result.accuracy}% ，现在可以开始问答。`, [
        { text: "开始问答", action: "startQA", primary: true },
      ]);
    }).catch(err => {
      this.setData({ loading: false });
      this.showModal("!", "校准失败", err.message || "请稍后重试", [
        { text: "确定", action: "close", primary: true },
      ]);
    });
  },

  goBack() {
    wx.redirectTo({ url: "/pages/home/index" });
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

    if (action === "startQA") {
      wx.redirectTo({ url: "/pages/qa/index" });
    }
  },
});
