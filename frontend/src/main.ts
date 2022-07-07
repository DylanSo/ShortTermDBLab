import { createApp } from "vue";
import router from "./router";
import ElementPlus from "element-plus";
import "../node_modules/element-plus/theme-chalk/index.css";
import App from "./App.vue";
import "dayjs/locale/zh-cn";
import locale from "element-plus/lib/locale/lang/zh-cn";
import store from "./store";
import axios from "axios";

// eslint-disable-next-line
const app = createApp(App);
app.config.globalProperties.$axios = axios; // 配置axios的全局引用
app.use(router).use(ElementPlus, { locale }).use(store).mount("#app");

router.beforeEach((to, from, next) => {
  // eslint-disable-next-line
  if (to.name !== "LoginPage" && store.state.username === "") next({ name: "LoginPage" });
  else next();
});
