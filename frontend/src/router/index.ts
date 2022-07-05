import { createRouter, createWebHashHistory, RouteRecordRaw } from "vue-router";
import LoginPage from "../views/LoginPage.vue";
import AdminPage from "../views/AdminPage.vue";
import StudentPage from "../views/StudentPage.vue";
import TeacherPage from "../views/TeacherPage.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "LoginPage",
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () =>
    //     import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
    component: LoginPage,
    meta: { displayName: "登录" },
  },
  {
    path: "/studentPage",
    name: "StudentPage",
    component: StudentPage,
    meta: { displayName: "学生页" },
  },
  {
    path: "/teacherPage",
    name: "TeacherPage",
    component: TeacherPage,
    meta: { displayName: "教师页" },
  },
  {
    path: "/adminPage",
    name: "AdminPage",
    component: AdminPage,
    meta: { displayName: "管理员页" },
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
