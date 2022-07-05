<template>
  <layout>
    <template v-slot:bar>
      <el-menu :default-active="activeIndex" mode="horizontal" router>
        <el-menu-item style="padding: 0" index="logo">
          <!--eslint-disable-next-line-->
          <img src="../assets/schoolLogo.png" style="width: 160px; height: 62px"/>
        </el-menu-item>
        <template v-if="this.username !== ''">
          <el-menu-item index="/AdminPage/StudentInfoManage">学生信息管理</el-menu-item>
          <el-menu-item index="/AdminPage/TeacherInfoManage">教师信息管理</el-menu-item>
          <el-menu-item index="/AdminPage/CourseInfoManage">课程信息管理</el-menu-item>
          <el-menu-item index="/AdminPage/MajorInfoManage">专业信息管理</el-menu-item>
          <el-menu-item index="/AdminPage/DepartmentInfoManage">部门信息管理</el-menu-item>
          <el-menu-item index="/AdminPage/ChooseCourseManage">学生选课情况更改</el-menu-item>
          <el-menu-item index="/AdminPage/CurriculumTeachArg">教师排课情况更改</el-menu-item>
          <el-menu-item index="/AdminPage/GradeManage">成绩信息管理</el-menu-item>
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
  name: "AdminPage",
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
