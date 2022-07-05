<template>
  <Layout>
    <template v-slot:main>
      <div style="display: flex; justify-content: center; align-items: center; height: 100%">
        <div
          style="
            height: 300px;
            width: 500px;
            box-shadow: rgba(60, 64, 67, 0.3) 0 1px 2px 0, rgba(60, 64, 67, 0.15) 0 2px 6px 2px;
            align-content: center;
            padding-top: 30px;
          "
        >
          <div style="font-size: 20px; font-family: '微软雅黑 Light'; text-align: center; margin-bottom: 20px">
            教务管理系统登录
          </div>
          <el-form
            ref="loginForm"
            :model="loginForm"
            status-icon
            :rules="rules"
            label-width="120px"
            style="width: 400px; display: flex; justify-content: center; padding: 20px 0"
          >
            <div>
              <el-form-item label="用户" prop="username" required>
                <el-input v-model="loginForm.username" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item style="margin-bottom: 30px" label="密码" prop="userpwd" required>
                <el-input v-model="loginForm.userpwd" type="password" autocomplete="off" show-password></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" @click="submitForm('loginForm')" style="width: 100%">登陆</el-button>
              </el-form-item>
            </div>
          </el-form>
        </div>
      </div>
    </template>
  </Layout>
</template>

<script>
import Layout from "@/components/Layout";
import { ElMessage } from "element-plus";
// import store from "../store";
export default {
  name: "LoginPage",
  // store,
  components: { Layout },
  data() {
    return {
      loginForm: {
        username: "",
        userpwd: "",
      },
      rules: {
        username: [{ required: true, message: "请输入用户名", trigger: "blur" }],
        userpwd: [{ required: true, message: "请输入密码", trigger: "blur" }],
      },
    };
  },
  methods: {
    // 表单校验
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$store.commit("login", this.loginForm.username);
          ElMessage({
            showClose: true,
            message: `用户 ${this.loginForm.username} 登陆成功!`,
            type: "success",
          });
          this.$router.replace({ name: "AdminPage" });
        } else {
          ElMessage({
            showClose: true,
            message: `用户名或密码错误!`,
            type: "error",
          });
          return false;
        }
      });
    },
  },
};
</script>

<style scoped></style>
