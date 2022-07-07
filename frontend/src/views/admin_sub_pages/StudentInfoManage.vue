<template>
  <el-button @click="getMessage">{{ msg }}</el-button>
  <table-field></table-field>
</template>

<script>
import TableField from "../../components/TableField";
import global from "../../utils/global";
export default {
  name: "StudentInfoManage",
  components: { TableField },
  data() {
    return {
      msg: "hi",
    };
  },
  methods: {
    getMessage() {
      const path = "http://127.0.0.1:5000/";
      const requestLatest = this.$axios.create({
        baseURL: global.backEndHost,
        timeout: 1000,
      });
      console.log(path);
      requestLatest
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.msg = res.data;
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
