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

function getCurrentDate() {
  const now = new Date();
  const year = now.getFullYear();
  const month = `${now.getMonth() + 1}`.padStart(2, "0");
  const day = `${now.getDate()}`.padStart(2, "0");
  return `${year}-${month}-${day}`;
}

module.exports = {
  getShichenByHour,
  getBackendTimeIndex,
  padHour,
  getTimeLabel,
  getCurrentDate,
};