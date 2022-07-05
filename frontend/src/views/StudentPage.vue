<template>
  <layout>
    <template v-slot:bar>
      <el-menu :default-active="activeIndex" mode="horizontal" router>
        <el-menu-item style="padding: 0" index="logo">
          <!--eslint-disable-next-line-->
          <img src="../assets/schoolLogo.png" style="width: 160px; height: 62px"/>
        </el-menu-item>
        <template v-if="this.username !== ''">
          <el-menu-item index="/StudentPage/StudentInfo">个人信息</el-menu-item>
          <el-menu-item index="/StudentPage/ChooseCourse">选课</el-menu-item>
          <el-menu-item index="/StudentPage/Curriculum">课程表</el-menu-item>
          <el-menu-item index="/StudentPage/GradeInfo">成绩详情</el-menu-item>
          <el-menu-item index="/StudentPage/GpaRanking">绩点排名</el-menu-item>
          <el-menu-item index="/StudentPage/TotalCredit">学分统计</el-menu-item>
          <el-sub-menu style="margin-left: auto" index="logoutMenu">
            <template #title>
              <i class="el-icon-setting"></i>
              {{ username }}
            </template>
            <el-menu-item index="ChangePassword">
              <i class="el-icon-right"></i>
              修改密码
            </el-menu-item>
            <el-menu-item @click="logoff()" index="logout">
              <i class="el-icon-right"></i>
              注销登陆
            </el-menu-item>
          </el-sub-menu>
        </template>
        <template v-else>
          <el-menu-item class="is-active">请登陆后访问!</el-menu-item>
        </template>
      </el-menu>
    </template>
    <template v-slot:main>
      <router-view />
    </template>
  </layout>
</template>

<script>
import Layout from "@/components/Layout.vue";
import { ElMessage } from "element-plus";
export default {
  name: "StudentPage",
  components: { Layout },
  data() {
    return {
      username: this.$store.state.username,
    };
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

<style scoped></style>
