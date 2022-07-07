<template>
  <el-form :model="form" label-width="120px" style="display: flex">
    <el-form-item label="关键字搜索">
      <el-input v-model="form.key_search" />
    </el-form-item>
    <el-form-item label="Activity zone">
      <el-select v-model="form.region" placeholder="please select your zone">
        <el-option label="Zone one" value="shanghai" />
        <el-option label="Zone two" value="beijing" />
      </el-select>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">查调</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive } from "vue";

// do not use same name with ref
const form = reactive({
  key_search: "",
  region: "",
});

const onSubmit = () => {
  console.log("submit!");
};
</script>
