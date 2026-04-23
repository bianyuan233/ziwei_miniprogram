const TIME_OPTIONS = [
  { label: "晚子时 (23:00-00:00)", timeIndex: 0, hour: 23, shichen: "子时" },
  { label: "丑时 (01:00-03:00)", timeIndex: 1, hour: 1, shichen: "丑时" },
  { label: "寅时 (03:00-05:00)", timeIndex: 2, hour: 3, shichen: "寅时" },
  { label: "卯时 (05:00-07:00)", timeIndex: 3, hour: 5, shichen: "卯时" },
  { label: "辰时 (07:00-09:00)", timeIndex: 4, hour: 7, shichen: "辰时" },
  { label: "巳时 (09:00-11:00)", timeIndex: 5, hour: 9, shichen: "巳时" },
  { label: "午时 (11:00-13:00)", timeIndex: 6, hour: 11, shichen: "午时" },
  { label: "未时 (13:00-15:00)", timeIndex: 7, hour: 13, shichen: "未时" },
  { label: "申时 (15:00-17:00)", timeIndex: 8, hour: 15, shichen: "申时" },
  { label: "酉时 (17:00-19:00)", timeIndex: 9, hour: 17, shichen: "酉时" },
  { label: "戌时 (19:00-21:00)", timeIndex: 10, hour: 19, shichen: "戌时" },
  { label: "亥时 (21:00-23:00)", timeIndex: 11, hour: 21, shichen: "亥时" },
  { label: "早子时 (00:00-01:00)", timeIndex: 12, hour: 0, shichen: "子时" },
];

function getShichenByHour(hour) {
  const val = Number(hour);

  if (val >= 23 || val < 1) return "子时";
  if (val >= 1 && val < 3) return "丑时";
  if (val >= 3 && val < 5) return "寅时";
  if (val >= 5 && val < 7) return "卯时";
  if (val >= 7 && val < 9) return "辰时";
  if (val >= 9 && val < 11) return "巳时";
  if (val >= 11 && val < 13) return "午时";
  if (val >= 13 && val < 15) return "未时";
  if (val >= 15 && val < 17) return "申时";
  if (val >= 17 && val < 19) return "酉时";
  if (val >= 19 && val < 21) return "戌时";
  return "亥时";
}

function getBackendTimeIndex(hour) {
  const val = Number(hour);

  if (val === 23) return 0;
  if (val >= 1 && val < 3) return 1;
  if (val >= 3 && val < 5) return 2;
  if (val >= 5 && val < 7) return 3;
  if (val >= 7 && val < 9) return 4;
  if (val >= 9 && val < 11) return 5;
  if (val >= 11 && val < 13) return 6;
  if (val >= 13 && val < 15) return 7;
  if (val >= 15 && val < 17) return 8;
  if (val >= 17 && val < 19) return 9;
  if (val >= 19 && val < 21) return 10;
  if (val >= 21 && val < 23) return 11;
  return 12;
}

function padHour(hour) {
  return `${String(hour).padStart(2, "0")}:00`;
}

function getTimeLabel(hour) {
  return `${padHour(hour)} (${getShichenByHour(hour)})`;
}

function getTimeOptions() {
  return TIME_OPTIONS.map(item => Object.assign({}, item));
}

function getTimeOptionByIndex(timeIndex) {
  const found = TIME_OPTIONS.find(item => item.timeIndex === Number(timeIndex));
  return found ? Object.assign({}, found) : Object.assign({}, TIME_OPTIONS[6]);
}

function getTimeOptionArrayIndex(timeIndex) {
  const index = TIME_OPTIONS.findIndex(item => item.timeIndex === Number(timeIndex));
  return index >= 0 ? index : 6;
}

function getCurrentDate() {
  const now = new Date();
  const year = now.getFullYear();
  const month = `${now.getMonth() + 1}`.padStart(2, "0");
  const day = `${now.getDate()}`.padStart(2, "0");
  return `${year}-${month}-${day}`;
}

module.exports = {
  TIME_OPTIONS,
  getTimeOptions,
  getTimeOptionByIndex,
  getTimeOptionArrayIndex,
  getShichenByHour,
  getBackendTimeIndex,
  padHour,
  getTimeLabel,
  getCurrentDate,
};
