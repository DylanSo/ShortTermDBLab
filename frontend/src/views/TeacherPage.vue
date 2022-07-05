<template>
  <layout>
    <template v-slot:manu>
      <el-menu-item index="TeacherInfo">个人信息</el-menu-item>
      <el-menu-item index="TeachCourse">授课表</el-menu-item>
      <el-menu-item index="EntryGrade">成绩录入</el-menu-item>
      <el-menu-item index="ClassGrade">教学班成绩</el-menu-item>
    </template>
    <template v-slot:main></template>
  </layout>
</template>

<script>
import Layout from "@/components/Layout";
export default {
  name: "TeacherPage",
  components: { Layout },
};
</script>

<style scoped></style>
