const backendHost = "http://127.0.0.1:5000/";
const backend = {
  baseURL: backendHost,
  getStudentsApi: backendHost + "getStudentsData",
  getTeachersApi: backendHost + "getTeachersData",
  getCoursesApi: backendHost + "getCoursesData",
  getMajorsApi: backendHost + "getMajorsData",
  getDepartmentsApi: backendHost + "getDepartmentsData",
  getChooseCourseApi: backendHost + "getChooseCourseData",
  getTeachCourseApi: backendHost + "getTeachCourseData",
  getGradeApi: backendHost + "getGradeApi",
  chooseCourseApi: backendHost + "chooseCourseApi",
  getStudentInfoApi: backendHost + "stuInfoApi",
  verifyLoginApi: backendHost + "login",
  changePwdApi: backendHost + "changePwdApi",
};
const frontEndHost = " http://localhost:8080/";
export default {
  backend, // 后端地址
  frontEndHost, // 前端地址
};
