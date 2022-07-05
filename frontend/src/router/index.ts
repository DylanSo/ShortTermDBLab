import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import LoginPage from "../views/LoginPage.vue";
import AdminPage from "../views/AdminPage.vue";
import StudentPage from "../views/StudentPage.vue";
import TeacherPage from "../views/TeacherPage.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "LoginPage",
    component: LoginPage,
    meta: { displayName: "登录" },
  },
  {
    path: "/StudentPage",
    name: "StudentPage",
    component: StudentPage,
    meta: { displayName: "学生页" },
    children: [
      {
        path: "StudentInfo",
        name: "StudentInfo",
        component: () => import("../views/student_sub_pages/StudentInfo.vue"),
      },
      {
        path: "ChooseCourse",
        name: "ChooseCourse",
        component: () => import("../views/student_sub_pages/ChooseCourse.vue"),
      },
      {
        path: "Curriculum",
        name: "Curriculum",
        component: () => import("../views/student_sub_pages/Curriculum.vue"),
      },
      {
        path: "GradeInfo",
        name: "GradeInfo",
        component: () => import("../views/student_sub_pages/GradeInfo.vue"),
      },
      {
        path: "GpaRanking",
        name: "GpaRanking",
        component: () => import("../views/student_sub_pages/GpaRanking.vue"),
      },
      {
        path: "TotalCredit",
        name: "TotalCredit",
        component: () => import("../views/student_sub_pages/TotalCredit.vue"),
      },
    ],
  },
  {
    path: "/TeacherPage",
    name: "TeacherPage",
    component: TeacherPage,
    meta: { displayName: "教师页" },
    children: [
      {
        path: "TeacherInfo",
        name: "TeacherInfo",
        component: () => import("../views/teacher_sub_pages/TeacherInfo.vue"),
      },
      {
        path: "TeachCourse",
        name: "TeachCourse",
        component: () => import("../views/teacher_sub_pages/TeachCourse.vue"),
      },
      {
        path: "EntryGrade",
        name: "EntryGrade",
        component: () => import("../views/teacher_sub_pages/EntryGrade.vue"),
      },
      {
        path: "ClassGrade",
        name: "ClassGrade",
        component: () => import("../views/teacher_sub_pages/ClassGrade.vue"),
      },
    ],
  },
  {
    path: "/AdminPage",
    name: "AdminPage",
    component: AdminPage,
    meta: { displayName: "管理员页" },
    children: [
      {
        path: "StudentInfoManage",
        name: "StudentInfoManage",
        component: () => import("../views/admin_sub_pages/StudentInfoManage.vue"),
      },
      {
        path: "TeacherInfoManage",
        name: "TeacherInfoManage",
        component: () => import("../views/admin_sub_pages/TeacherInfoManage.vue"),
      },
      {
        path: "CourseInfoManage",
        name: "CourseInfoManage",
        component: () => import("../views/admin_sub_pages/CourseInfoManage.vue"),
      },
      {
        path: "MajorInfoManage",
        name: "MajorInfoManage",
        component: () => import("../views/admin_sub_pages/MajorInfoManage.vue"),
      },
      {
        path: "DepartmentInfoManage",
        name: "DepartmentInfoManage",
        component: () => import("../views/admin_sub_pages/DepartmentInfoManage.vue"),
      },
      {
        path: "ChooseCourseManage",
        name: "ChooseCourseManage",
        component: () => import("../views/admin_sub_pages/ChooseCourseManage.vue"),
      },
      {
        path: "CurriculumTeachArg",
        name: "CurriculumTeachArg",
        component: () => import("../views/admin_sub_pages/CurriculumTeachArg.vue"),
      },
      {
        path: "GradeManage",
        name: "GradeManage",
        component: () => import("../views/admin_sub_pages/GradeManage.vue"),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
