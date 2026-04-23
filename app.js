const storage = require("./utils/storage");

App({
  globalData: {
    theme: {
      primary: "#8B9A8F",
      secondary: "#9B8FA9",
      accent: "#C4A370",
    },
  },

  onLaunch() {
    storage.initAppState();
  },
});
