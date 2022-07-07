<template>
  <table-field v-bind:data_list="data_list">
    <!-- 插入面包板-->
    <template v-slot:bread_crumb>
      <el-breadcrumb-item>用户：<strong>管理员</strong></el-breadcrumb-item>
      <el-breadcrumb-item>学生信息管理</el-breadcrumb-item>
    </template>
    <!-- 插入数据面板-->
    <template v-slot:data_table>
      <el-table-column label="序号" type="index"></el-table-column>
      <el-table-column label="学号" prop="syc_sno13"></el-table-column>
      <el-table-column label="姓名" prop="syc_sname13"></el-table-column>
      <el-table-column label="性别" prop="syc_ssex13"></el-table-column>
      <el-table-column label="年龄" prop="syc_sage13"></el-table-column>
      <el-table-column label="生源地" prop="syc_source13"></el-table-column>
      <el-table-column label="总学分" prop="syc_scredits13"></el-table-column>
      <el-table-column label="所在班级" prop="syc_cno13"></el-table-column>
      <el-table-column label="专业" prop="syc_mno13"></el-table-column>
      <el-table-column label="状态" prop="syc_ifgraduate13"></el-table-column>
      <el-table-column label="操作" width="180px">
        <template v-slot="scope">
          <!-- 修改按钮 -->
          <el-tooltip effect="dark" content="编辑" placement="bottom" :enterable="false">
            <el-button type="primary" v-model="scope.row.Id" size="small"
              ><el-icon><edit /></el-icon
            ></el-button>
          </el-tooltip>
          <!-- 删除按钮 -->
          <el-tooltip effect="dark" content="删除" placement="bottom" :enterable="false">
            <el-button type="danger" size="small"
              ><el-icon><delete /></el-icon
            ></el-button>
          </el-tooltip>
        </template>
      </el-table-column>
    </template>
  </table-field>
</template>

<script>
import TableField from "../../components/TableField";
import global from "../../utils/global";
import { Delete, Edit } from "@element-plus/icons-vue";
export default {
  name: "StudentInfoManage",
  components: { TableField, Edit, Delete },
  data() {
    return {
      /**
          格式：
       {
          s_no: "-",
          s_name: "-",
          s_sex: "-",
          s_age: "-",
          s_source: "-",
          s_credit: "-",
          s_cname: "-",
          s_mno: "-",
          s_password: "-",
          s_ifGraduate: "-",
       }
      **/
      data_list: [],
    };
  },
  created() {
    this.getStudentList();
  },
  methods: {
    // 获取学生表
    getStudentList() {
      const requestLatest = this.$axios.create({
        baseURL: global.backend.getStudentsApi,
        timeout: 1000,
      });
      requestLatest
        .get(global.backend.getStudentsApi)
        .then((res) => {
          console.log(res.data);
          this.data_list = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
};
</script>

<style scoped></style>
