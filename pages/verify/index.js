const { QUESTIONS } = require("../../utils/mock");

Page({
  data: {
    questions: QUESTIONS,
    currentIndex: 0,
    total: QUESTIONS.length,
    progress: 0,
    currentQuestion: QUESTIONS[0],
    answers: [],
    loading: false,
  },

  updateQuestion(index) {
    const total = this.data.total;
    this.setData({
      currentIndex: index,
      currentQuestion: QUESTIONS[index],
      progress: Math.round((index / total) * 100),
    });
  },

  handleAnswer(event) {
    if (this.data.loading) {
      return;
    }

    const value = event.currentTarget.dataset.value === "true";
    const answers = [...this.data.answers, value];
    const nextIndex = this.data.currentIndex + 1;

    this.setData({
      loading: true,
      answers,
    });

    setTimeout(() => {
      if (nextIndex < this.data.total) {
        this.updateQuestion(nextIndex);
        this.setData({ loading: false });
        return;
      }

      const yesCount = answers.filter(Boolean).length;
      const score = 92 + yesCount * 2;
      wx.redirectTo({
        url: `/pages/result/index?score=${score}&yesCount=${yesCount}`,
      });
    }, 400);
  },
});
