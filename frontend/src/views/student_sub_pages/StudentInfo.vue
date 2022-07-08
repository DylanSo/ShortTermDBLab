<template>
  <el-breadcrumb separator-class="el-icon-arrow-right" style="margin-bottom: 20px">
    <el-breadcrumb-item>用户：<strong>学生</strong></el-breadcrumb-item>
    <el-breadcrumb-item>个人信息</el-breadcrumb-item>
  </el-breadcrumb>
  <el-card class="box-card" style="margin-left: 500px; margin-top: 30px">
    <template #header>
      <div class="card-header">
        <span>个人资料</span>
      </div>
    </template>
    <div class="text item">学号：{{ data_list["syc_sno13"] }}</div>
    <div class="text item">姓名：{{ data_list["syc_sname13"] }}</div>
    <div class="text item">性别：{{ data_list["syc_ssex13"] }}</div>
    <div class="text item">年龄：{{ data_list["syc_sage13"] }}</div>
    <div class="text item">生源地：{{ data_list["syc_source13"] }}</div>
    <div class="text item">已修学分：{{ data_list["syc_scredits13"] }}</div>
    <div class="text item">所在学院：{{ data_list["syc_dname13"] }}</div>
    <div class="text item">所在专业：{{ data_list["syc_mname13"] }}</div>
    <div class="text item">所在班级：{{ data_list["syc_cname13"] }}</div>
    <div class="text item">是否毕业：{{ data_list["syc_ifgraduate13"] }}</div>
  </el-card>
</template>

<script>
import global from "../../utils/global";
import { ElMessage } from "element-plus";

export default {
  name: "StudentInfo",
  data() {
    return {
      data_list: [],
    };
  },
  created() {
    this.getPersonalInfo();
  },
  methods: {
    // 获取学生表
    getPersonalInfo() {
      let formData = new FormData();
      formData.append("username", this.$store.state.username);
      const requestLatest = this.$axios.create({
        baseURL: global.backend.getStudentInfoApi,
        timeout: 1000,
      });
      requestLatest
        .post(global.backend.getStudentInfoApi, formData)
        .then((res) => {
          console.log(res.data);
          this.data_list = res.data[0];
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>

<style>
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.text {
  font-size: 14px;
}

.item {
  margin-bottom: 18px;
}

.box-card {
  width: 480px;
}
</style>
