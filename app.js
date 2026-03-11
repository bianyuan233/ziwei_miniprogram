const storage = require("./utils/storage");

App({
  globalData: {
    theme: {
      primary: "#7D9D9C",
      accent: "#D4A59A",
    },
  },

  onLaunch() {
    storage.initAppState();
  },
});
