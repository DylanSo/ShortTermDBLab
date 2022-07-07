<template>
  <div>
    <!-- 面包屑导航区域 -->
    <el-breadcrumb separator-class="el-icon-arrow-right" style="margin-bottom: 20px">
      <!--跳转：:to="{ path: '/home' }"-->
      <slot name="bread_crumb"></slot>
    </el-breadcrumb>
    <!-- 卡片视图区域 -->
    <el-card>
      <el-row :gutter="20">
        <search-form></search-form>
      </el-row>
      <!-- 用户列表区域  -->
      <el-table :data="data_list.slice((currentPage - 1) * pagesize, currentPage * pagesize)" border stripe style="">
        <slot name="data_table"></slot>
      </el-table>
      <el-pagination
        layout="total,sizes,prev,pager,next,jumper"
        :total="data_list.length"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
      />
    </el-card>
  </div>
</template>

<script>
import SearchForm from "./SearchForm";
export default {
  components: { SearchForm },
  data() {
    return {
      // 获取用户列表的参数对象
      queryInfo: {
        query: "", // 查询参数
      },
      currentPage: 1, //默认页码为1
      pagesize: 10, //默认一页显示10条
      // 总数据条数
      total: 0,
    };
  },
  props: {
    // 用户列表
    data_list: {
      type: Array,
    },
  },
  created() {
    // this.getUserList();
  },
  methods: {
    handleSizeChange: function (size) {
      //一页显示多少条
      this.pagesize = size;
    },
    handleCurrentChange: function (currentPage) {
      //页码更改方法
      this.currentPage = currentPage;
    },
    async getUserList() {
      const { data: res } = await this.$http.get("users", {
        params: this.queryInfo,
      });
      if (res.meta.status !== 200) return this.$message.error("获取用户列表失败");
      this.userlist = res.data.users;
      this.total = res.data.total;
      console.log(res);
    },
  },
};
</script>

<style lang="less" scoped></style>
