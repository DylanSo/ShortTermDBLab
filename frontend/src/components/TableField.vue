<template>
  <div>
    <!-- 面包屑导航区域 -->

    <el-breadcrumb separator-class="el-icon-arrow-right" style="margin-bottom: 20px">
      <!--跳转：:to="{ path: '/home' }"-->
      <el-breadcrumb-item>用户：<strong>管理员</strong></el-breadcrumb-item>
      <el-breadcrumb-item>学生信息管理</el-breadcrumb-item>
    </el-breadcrumb>
    <!-- 卡片视图区域 -->
    <el-card>
      <el-row :gutter="20">
        <search-form></search-form>
        <!--        <el-col :span="8">-->
        <!--          &lt;!&ndash; 搜索与添加区域 &ndash;&gt;-->
        <!--          <el-input placeholder="请输入内容" type="text">-->
        <!--            <template #append>-->
        <!--              <el-icon><search /></el-icon>-->
        <!--            </template>-->
        <!--          </el-input>-->
        <!--        </el-col>-->
        <!--        <el-col :span="4">-->
        <!--          <el-button type="primary">添加用户</el-button>-->
        <!--        </el-col>-->
      </el-row>
      <!-- 用户列表区域  -->
      <el-table :data="user_list.slice((currentPage - 1) * pagesize, currentPage * pagesize)" border stripe style="">
        <el-table-column label="序号" type="index"></el-table-column>
        <el-table-column label="学号" prop="s_no"></el-table-column>
        <el-table-column label="姓名" prop="s_name"></el-table-column>
        <el-table-column label="性别" prop="s_sex"></el-table-column>
        <el-table-column label="年龄" prop="s_age"></el-table-column>
        <el-table-column label="生源地" prop="s_source"></el-table-column>
        <el-table-column label="总学分" prop="s_credit"></el-table-column>
        <el-table-column label="所在班级" prop="s_cname"></el-table-column>
        <el-table-column label="专业" prop="s_mno"></el-table-column>
        <el-table-column label="状态" prop="s_ifGraduate"></el-table-column>
        <!--        <el-table-column label="操作" prop="mg_state">-->
        <!--          <template v-slot="scope">-->
        <!--            <el-switch v-model="scope.row.mg_state" />-->
        <!--          </template>-->
        <!--        </el-table-column>-->
        <el-table-column label="操作" width="180px">
          <template v-slot="scope">
            <!-- 修改按钮 -->
            <el-tooltip effect="dark" content="编辑" placement="bottom" :enterable="false">
              <el-button type="primary" v-model="scope.row.Id" size="mini"
                ><el-icon><edit /></el-icon
              ></el-button>
            </el-tooltip>
            <!-- 删除按钮 -->
            <el-tooltip effect="dark" content="删除" placement="bottom" :enterable="false">
              <el-button type="danger" size="mini"
                ><el-icon><delete /></el-icon
              ></el-button>
            </el-tooltip>
            <!-- 分配角色按钮 -->
            <!--            <el-tooltip effect="dark" content="分配角色" placement="top" :enterable="false">-->
            <!--              <el-button type="warning" size="mini"-->
            <!--                ><el-icon><setting /></el-icon-->
            <!--              ></el-button>-->
            <!--            </el-tooltip>-->
          </template>
        </el-table-column>
      </el-table>
      <el-pagination
        layout="total,sizes,prev,pager,next,jumper"
        :total="user_list.length"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
      />
    </el-card>
  </div>
</template>

<script>
import { Edit, Delete } from "@element-plus/icons-vue";
import SearchForm from "./SearchForm";
export default {
  components: { Edit, Delete, SearchForm },
  data() {
    return {
      // 获取用户列表的参数对象
      queryInfo: {
        query: "", // 查询参数
      },
      currentPage: 1, //默认页码为1
      pagesize: 10, //默认一页显示10条
      // 用户列表
      user_list: [
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
        {
          s_no: "S01010101",
          s_name: "张三",
          s_sex: "男",
          s_age: 21,
          s_source: "浙江省杭州市",
          s_credit: 0,
          s_cname: "嵌入式01",
          s_mno: "嵌入式系统",
          s_password: "123456",
          s_ifGraduate: "在读",
        },
      ],
      // 总数据条数
      total: 0,
    };
  },
  created() {
    // this.getUserList();
    this.setCount();
  },
  methods: {
    setCount() {
      this.count = this.user_list.length;
      console.log(this.count);
    },
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
      // if (this.count === 0) {
      //   this.count = this.user_list.length;
      // }
      // // eslint-disable-next-line no-debugger
      // debugger;
    },
  },
};
</script>

<style lang="less" scoped></style>
