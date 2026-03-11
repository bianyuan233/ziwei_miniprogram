const KEYS = {
  PROFILE: "ssn_profile",
  VERIFIED: "ssn_verified",
  PAID: "ssn_paid",
  HISTORY: "ssn_history",
};

function initAppState() {
  if (!wx.getStorageSync(KEYS.PROFILE)) {
    wx.setStorageSync(KEYS.PROFILE, {
      nickname: "有缘人",
      avatarText: "顺",
      memberType: "普通会员",
      memberExpireAt: "2026-12-31",
      userId: "889203",
      gender: "男",
      profession: "互联网/软件",
      birthDate: "",
      birthHour: 12,
      shichen: "午时",
    });
  }

  const profile = wx.getStorageSync(KEYS.PROFILE) || {};
  wx.setStorageSync(KEYS.PROFILE, {
    nickname: "有缘人",
    avatarText: "顺",
    memberType: "普通会员",
    memberExpireAt: "2026-12-31",
    userId: "889203",
    gender: "男",
    profession: "互联网/软件",
    birthDate: "",
    birthHour: 12,
    shichen: "午时",
    ...profile,
  });

  if (wx.getStorageSync(KEYS.VERIFIED) === "") {
    wx.setStorageSync(KEYS.VERIFIED, false);
  }

  if (wx.getStorageSync(KEYS.PAID) === "") {
    wx.setStorageSync(KEYS.PAID, false);
  }

  if (!wx.getStorageSync(KEYS.HISTORY)) {
    wx.setStorageSync(KEYS.HISTORY, []);
  }
}

function getProfile() {
  return wx.getStorageSync(KEYS.PROFILE);
}

function saveProfile(profile) {
  wx.setStorageSync(KEYS.PROFILE, {
    ...getProfile(),
    ...profile,
  });
}

function isVerified() {
  return !!wx.getStorageSync(KEYS.VERIFIED);
}

function setVerified(value) {
  wx.setStorageSync(KEYS.VERIFIED, !!value);
}

function isPaid() {
  return !!wx.getStorageSync(KEYS.PAID);
}

function setPaid(value) {
  wx.setStorageSync(KEYS.PAID, !!value);
}

function getHistory() {
  return wx.getStorageSync(KEYS.HISTORY) || [];
}

function appendHistory(record) {
  const history = getHistory();
  wx.setStorageSync(KEYS.HISTORY, [record, ...history].slice(0, 20));
}

function clearAll() {
  wx.removeStorageSync(KEYS.PROFILE);
  wx.removeStorageSync(KEYS.VERIFIED);
  wx.removeStorageSync(KEYS.PAID);
  wx.removeStorageSync(KEYS.HISTORY);
  initAppState();
}

module.exports = {
  KEYS,
  initAppState,
  getProfile,
  saveProfile,
  isVerified,
  setVerified,
  isPaid,
  setPaid,
  getHistory,
  appendHistory,
  clearAll,
};