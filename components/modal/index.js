Component({
  properties: {
    visible: {
      type: Boolean,
      value: false,
    },
    icon: {
      type: String,
      value: "",
    },
    title: {
      type: String,
      value: "",
    },
    message: {
      type: String,
      value: "",
    },
    buttons: {
      type: Array,
      value: [],
    },
  },

  methods: {
    noop() {},

    handleAction(event) {
      const action = event.currentTarget.dataset.action || "close";
      this.triggerEvent("action", { action });
    },
  },
});
