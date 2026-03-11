const QUESTIONS = [
  {
    icon: "学",
    title: "23-25 岁期间",
    desc: "学业或技能有突破性进展，可能伴随异地机会或环境变化。",
  },
  {
    icon: "缘",
    title: "28 岁前后",
    desc: "人际关系重组，重要合作或情感节点出现，可能伴随分合变化。",
  },
  {
    icon: "业",
    title: "32 岁左右",
    desc: "事业压力增大但机会并存，出现职位晋升或责任加重的迹象。",
  },
];

const CHART_PALACES = [
  { name: "兄弟", star: "天机" },
  { name: "夫妻", star: "紫微" },
  { name: "子女", star: "贪狼" },
  { name: "命宫", star: "太阴", main: true },
  { name: "财帛", star: "廉贞" },
  { name: "疾厄", star: "巨门" },
  { name: "迁移", star: "天同" },
  { name: "交友", star: "武曲" },
  { name: "官禄", star: "太阳" },
  { name: "田宅", star: "破军" },
  { name: "福德", star: "天梁" },
  { name: "父母", star: "七杀" },
];

const CHART_DETAILS = [
  {
    palace: "命宫",
    star: "太阴",
    summary: "性格温和，善于规划，适合稳中求进的成长路径。",
  },
  {
    palace: "财帛",
    star: "廉贞",
    summary: "财运波动中见机会，宜长期积累专业能力。",
  },
  {
    palace: "官禄",
    star: "太阳",
    summary: "事业发展较明朗，适合公共服务、传播、管理岗位。",
  },
  {
    palace: "迁移",
    star: "天同",
    summary: "外出易遇贵人，换环境时往往带来新福气。",
  },
];

const DAILY_FORTUNE = {
  heading: "宜沟通协作，忌独自决策",
  summary: "事业宫有贵人信号，多听取团队意见，更容易放大优势。",
  tags: ["贵人运", "协作顺", "适合复盘"],
};

const SERVICE_MENU = [
  { key: "deep", icon: "深", title: "深度分析" },
  { key: "yearly", icon: "年", title: "流年运势" },
  { key: "history", icon: "史", title: "历史记录" },
  { key: "career", icon: "业", title: "事业专项" },
  { key: "love", icon: "缘", title: "感情专项" },
  { key: "api", icon: "接", title: "接口返回" },
  { key: "reset", icon: "重", title: "重新验盘" },
];

const CONTENT_DETAILS = {
  deep: {
    title: "深度命理分析",
    paragraphs: [
      "今年整体运势呈上升趋势，命宫稳定，适合通过节奏化投入建立长期成果。",
      "若你正在做转岗、转型或副业布局，第二季度到第三季度更容易出现关键窗口。",
    ],
    advice: "本周适合主动沟通、整理计划，并把重要判断放在上午完成。",
  },
  career: {
    title: "事业专项推演",
    paragraphs: [
      "官禄宫太阳星明亮，说明事业上的曝光度和责任感都会增强。",
      "适合承担对外表达、项目统筹、用户沟通类工作，做事越公开越有助力。",
    ],
    advice: "优先处理团队协作、汇报表达、方案对齐类任务。",
  },
  love: {
    title: "感情专项推演",
    paragraphs: [
      "夫妻宫紫微星坐守，对关系质量要求较高，也容易吸引能力较强的对象。",
      "相处中要避免强控制感，保持清晰表达和边界感，会比情绪化表达更有效。",
    ],
    advice: "适合先说感受，再说期待，少做猜测式沟通。",
  },
};

const YEARLY_RECORDS = [
  { year: "2026", label: "丙午", status: "查看" },
  { year: "2025", label: "乙巳", status: "已归档" },
  { year: "2024", label: "甲辰", status: "已归档" },
];

const PAYMENT_OPTIONS = [
  {
    key: "free",
    title: "基础版",
    desc: "命盘图 + 年度 3 关键词",
    price: "免费",
  },
  {
    key: "single",
    title: "单次解锁",
    desc: "1 次深度解读 + 7 天存档",
    price: "12.9 元",
    recommended: true,
  },
  {
    key: "member",
    title: "月度会员",
    desc: "无限轻量分析 + 4 次深度推演",
    price: "39 元",
  },
];

module.exports = {
  QUESTIONS,
  CHART_PALACES,
  CHART_DETAILS,
  DAILY_FORTUNE,
  SERVICE_MENU,
  CONTENT_DETAILS,
  YEARLY_RECORDS,
  PAYMENT_OPTIONS,
};