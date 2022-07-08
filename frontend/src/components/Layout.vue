<template>
  <el-container id="layout_container">
    <el-header>
      <slot name="bar">
        <el-menu :default-active="activeIndex" mode="horizontal" router>
          <el-menu-item style="padding: 0" index="logo">
            <!--eslint-disable-next-line-->
            <img src="../assets/schoolLogo.png" style="width: 160px; height: 62px" />
          </el-menu-item>
          <template v-if="username !== ''">
            <!--eslint-disable-next-line-->
            <!--<template v-for="route in routes" :key="route.name" :route="route">-->
            <!--<el-menu-item :index="route.path">{{ route.meta.displayName }}</el-menu-item>-->
            <!--</template>-->
            <el-sub-menu style="margin-left: auto" index="logoutMenu">
              <template #title>
                <i class="el-icon-setting"></i>
                {{ username }}
              </template>
              <el-menu-item @click="logoff()" index="logout">
                <i class="el-icon-right"></i>
                注销登陆
              </el-menu-item>
              <el-menu-item>
                <i class="el-icon-right"></i>
                修改密码
              </el-menu-item>
            </el-sub-menu>
          </template>
          <template v-else>
            <el-menu-item class="is-active">请登陆后访问!</el-menu-item>
          </template>
        </el-menu>
      </slot>
    </el-header>
    <el-main style="height: 100%">
      <slot name="main"></slot>
    </el-main>
    <el-footer height="40px" style="color: #909399; text-align: center">教务管理系统</el-footer>
  </el-container>
</template>

<script>
import { useRoute, useRouter } from "vue-router";
import { ElMessage } from "element-plus";
// import store from "../store";

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Layout",
  // store,
  setup() {
    const router = useRouter();
    const route = useRoute();
    return {
      routes: router.getRoutes().filter((value) => value.name !== "Login" && value.name !== "Logout"),
      activeIndex: route.path,
    };
  },
  computed: {
    username() {
      return this.$store.state.username || "";
    },
  },
  methods: {
    logoff() {
      this.$store.commit("logoff");
      ElMessage({
        showClose: true,
        message: `用户 ${this.$store.state.username} 注销成功!`,
        type: "success",
      });
      this.$router.replace({ name: "LoginPage" });
    },
  },
};
</script>

<style scoped>
#layout_container {
  height: 100%;
  min-height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
</style>
