const STATE_KEY = "ssn_app_state_v2";

const DEFAULT_STATE = {
  currentUser: null,
  profiles: [],
  selectedProfileId: "",
  subscription: {
    plan: null,
    purchaseDate: null,
    expiryDate: null,
  },
  paymentHistory: [],
  qaCount: 0,
};

function clone(value) {
  return JSON.parse(JSON.stringify(value));
}

function createDefaultState() {
  return clone(DEFAULT_STATE);
}

function getState() {
  const stored = wx.getStorageSync(STATE_KEY);
  if (!stored || typeof stored !== "object") {
    return createDefaultState();
  }

  return Object.assign(createDefaultState(), stored, {
    subscription: Object.assign({}, DEFAULT_STATE.subscription, stored.subscription || {}),
    paymentHistory: Array.isArray(stored.paymentHistory) ? stored.paymentHistory : [],
    profiles: Array.isArray(stored.profiles) ? stored.profiles : [],
    qaCount: Number(stored.qaCount || 0),
  });
}

function saveState(nextState) {
  wx.setStorageSync(STATE_KEY, Object.assign(createDefaultState(), nextState));
}

function initAppState() {
  const existing = wx.getStorageSync(STATE_KEY);
  if (!existing) {
    saveState(createDefaultState());
  }
}

function genId(prefix) {
  return `${prefix}_${Date.now()}_${Math.random().toString(36).slice(2, 8)}`;
}

function getCurrentUser() {
  return getState().currentUser;
}

function saveCurrentUser(user) {
  const state = getState();
  state.currentUser = Object.assign({}, state.currentUser || {}, user);
  saveState(state);
  return state.currentUser;
}

function isRegistered() {
  return !!getState().currentUser;
}

function getProfiles() {
  return getState().profiles;
}

function getSelectedProfileId() {
  return getState().selectedProfileId;
}

function setSelectedProfile(profileId) {
  const state = getState();
  state.selectedProfileId = profileId;
  saveState(state);
}

function getSelectedProfile() {
  const state = getState();
  if (!state.profiles.length) return null;
  const selected = state.profiles.find(item => item.id === state.selectedProfileId);
  return selected || state.profiles[0];
}

function addProfile(profile) {
  const state = getState();
  const nextProfile = Object.assign({
    id: genId("profile"),
    name: "本人",
    gender: "男",
    birthDate: "",
    timeIndex: 6,
    timeLabel: "午时 (11:00-13:00)",
    profession: "",
    calibrationStatus: "pending",
    accuracy: 0,
    chartKey: "",
    chartData: null,
    createdAt: new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  }, profile);

  state.profiles = [nextProfile].concat(state.profiles);
  state.selectedProfileId = nextProfile.id;
  saveState(state);
  return nextProfile;
}

function updateProfile(profileId, patch) {
  const state = getState();
  state.profiles = state.profiles.map(profile => {
    if (profile.id !== profileId) return profile;
    return Object.assign({}, profile, patch, { updatedAt: new Date().toISOString() });
  });
  saveState(state);
  return state.profiles.find(profile => profile.id === profileId) || null;
}

function saveChartForProfile(profileId, chartData, chartKey) {
  return updateProfile(profileId, { chartData, chartKey });
}

function getSubscription() {
  return getState().subscription;
}

function setSubscription(subscription) {
  const state = getState();
  state.subscription = Object.assign({}, DEFAULT_STATE.subscription, subscription);
  saveState(state);
}

function getPaymentHistory() {
  return getState().paymentHistory;
}

function addPaymentRecord(record) {
  const state = getState();
  state.paymentHistory = [record].concat(state.paymentHistory || []).slice(0, 30);
  saveState(state);
}

function getQaCount() {
  return getState().qaCount;
}

function incrementQaCount() {
  const state = getState();
  state.qaCount = Number(state.qaCount || 0) + 1;
  saveState(state);
  return state.qaCount;
}

function clearAll() {
  wx.removeStorageSync(STATE_KEY);
  initAppState();
}

module.exports = {
  STATE_KEY,
  initAppState,
  genId,
  getState,
  saveState,
  getCurrentUser,
  saveCurrentUser,
  isRegistered,
  getProfiles,
  getSelectedProfileId,
  setSelectedProfile,
  getSelectedProfile,
  addProfile,
  updateProfile,
  saveChartForProfile,
  getSubscription,
  setSubscription,
  getPaymentHistory,
  addPaymentRecord,
  getQaCount,
  incrementQaCount,
  clearAll,
};
