<template>
  <layout>
    <template v-slot:manu>
      <el-menu-item index="StudentInfoManage">学生信息管理</el-menu-item>
      <el-menu-item index="TeacherInfoManage">教师信息管理</el-menu-item>
      <el-menu-item index="CourseInfoManage">课程信息管理</el-menu-item>
      <el-menu-item index="MajorInfoManage">专业信息管理</el-menu-item>
      <el-menu-item index="DepartmentInfoManage">部门信息管理</el-menu-item>
      <el-menu-item index="ChooseCourseManage">学生选课情况更改</el-menu-item>
      <el-menu-item index="CurriculumTeachArg">教师排课情况更改</el-menu-item>
      <el-menu-item index="GradeManage">成绩信息管理</el-menu-item>
    </template>
    <template v-slot:main></template>
  </layout>
</template>

<script>
import Layout from "@/components/Layout";
export default {
  name: "AdminPage",
  components: { Layout },
};
</script>

<style scoped></style>
