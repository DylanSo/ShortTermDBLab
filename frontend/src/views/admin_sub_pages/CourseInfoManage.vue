<template>
  <table-field v-bind:data_list="data_list">
    <!-- 插入面包板-->
    <template v-slot:bread_crumb>
      <el-breadcrumb-item>用户：<strong>管理员</strong></el-breadcrumb-item>
      <el-breadcrumb-item>课程信息管理</el-breadcrumb-item>
    </template>
    <!-- 插入数据面板-->
    <template v-slot:data_table>
      <el-table-column label="序号" type="index"></el-table-column>
      <el-table-column label="课程编号" prop="syc_cono13" sortable></el-table-column>
      <el-table-column label="课程名" prop="syc_coname13" sortable></el-table-column>
      <el-table-column label="所属专业" prop="syc_mno13"></el-table-column>
      <el-table-column label="开课学期" prop="syc_semester13" sortable></el-table-column>
      <el-table-column label="课程学分" prop="syc_cocredit13" sortable></el-table-column>
      <el-table-column label="课程学时" prop="syc_cohours13" sortable></el-table-column>
      <el-table-column label="考查方式" prop="syc_coassessment13" sortable></el-table-column>
      <el-table-column label="可选状态" prop="syc_coifOptional13" sortable></el-table-column>
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
import { Delete, Edit } from "@element-plus/icons-vue";
import global from "../../utils/global";

export default {
  name: "CourseInfoManage",
  components: { TableField, Edit, Delete },
  data() {
    return {
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
        baseURL: global.backend.getCoursesApi,
        timeout: 1000,
      });
      requestLatest
        .get(global.backend.getCoursesApi)
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
