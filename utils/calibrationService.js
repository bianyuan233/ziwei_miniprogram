const QUESTIONS = [
  {
    question: "你通常如何面对工作中的压力？",
    options: [
      "主动解决，喜欢控制全局",
      "会焦虑，但还是会坚持",
      "倾向于寻求帮助或逃避",
      "很难说，随情况而定",
    ],
  },
  {
    question: "在重大决策前，你会怎样做？",
    options: [
      "迅速判断，相信直觉",
      "充分调查，理性分析",
      "征求意见，听别人建议",
      "犹豫不决，容易受影响",
    ],
  },
];

function clone(value) {
  return JSON.parse(JSON.stringify(value));
}

function getQuestions() {
  return clone(QUESTIONS);
}

function submitAnswers() {
  return Promise.resolve({
    status: "success",
    accuracy: 95,
  });
}

module.exports = {
  getQuestions,
  submitAnswers,
};
