<template>
  <layout>
    <template v-slot:manu>
      <el-menu-item index="StudentInfo">个人信息</el-menu-item>
      <el-menu-item index="ChooseCourse">选课</el-menu-item>
      <el-menu-item index="Curriculum">课程表</el-menu-item>
      <el-menu-item index="GradeInfo">成绩详情</el-menu-item>
      <el-menu-item index="GpaRanking">绩点排名</el-menu-item>
      <el-menu-item index="TotalCredit">学分统计</el-menu-item>
    </template>
    <template v-slot:main></template>
  </layout>
</template>

<script>
import Layout from "@/components/Layout";
export default {
  name: "StudentPage",
  components: { Layout },
};
</script>

<style scoped></style>
