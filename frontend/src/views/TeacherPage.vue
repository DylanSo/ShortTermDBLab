<template>
  <el-dialog v-model="dialogFormVisible" title="修改密码">
    <el-form :model="form">
      <el-form-item label="新密码" :label-width="formLabelWidth">
        <el-input v-model="form.new_pwd" autocomplete="off" />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取消</el-button>
        <!-- eslint-disable-next-line -->
        <el-button type="primary" @click="cpwd">提交</el-button>
      </span>
    </template>
  </el-dialog>
  <layout>
    <template v-slot:bar>
      <el-menu :default-active="activeIndex" mode="horizontal" router>
        <el-menu-item style="padding: 0" index="logo">
          <!-- eslint-disable-next-line -->
          <img src="../assets/schoolLogo.png" style="width: 160px; height: 62px"/>
        </el-menu-item>
        <template v-if="this.username !== ''">
          <el-menu-item index="/TeacherPage/TeacherInfo">个人信息</el-menu-item>
          <el-menu-item index="/TeacherPage/TeachCourse">授课表</el-menu-item>
          <el-menu-item index="/TeacherPage/EntryGrade">成绩录入</el-menu-item>
          <el-menu-item index="/TeacherPage/ClassGrade">教学班成绩</el-menu-item>
          <el-sub-menu style="margin-left: auto" index="logoutMenu">
            <template #title>
              <i class="el-icon-setting"></i>
              {{ username }}
            </template>
            <el-menu-item @click="logoff()" index="logout">
              <i class="el-icon-right"></i>
              注销登陆
            </el-menu-item>
          </el-sub-menu>
          <el-button @click="dialogFormVisible = true" style="margin-top: 20px">修改密码</el-button>
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
import global from "@/utils/global";
export default {
  name: "TeacherPage",
  components: { Layout },
  data() {
    return {
      username: this.$store.state.username,
      form: {
        username: this.$store.state.username,
        new_pwd: "",
      },
      formLabelWidth: "140px",
      dialogFormVisible: false,
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
    cpwd() {
      this.changePwd().then((tem) => {
        if (tem === "ok") {
          ElMessage({
            showClose: true,
            message: `已修改!`,
            type: "success",
          });
        } else {
          ElMessage({
            showClose: true,
            message: `修改失败!`,
            type: "error",
          });
        }
        this.dialogFormVisible = false;
      });
    },
    async changePwd() {
      let formData = new FormData();
      let tem;
      formData.append("new_pwd", this.form.new_pwd.toString());
      formData.append("username", this.form.username.toString());
      const requestLatest = this.$axios.create({
        baseURL: global.backend.changePwdApi,
        timeout: 5000,
      });
      await requestLatest
        .post(global.backend.changePwdApi, formData)
        .then((res) => {
          tem = res.data["msg"];
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      return tem;
    },
  },
};
</script>

<style scoped></style>
