<template>
  <!-- eslint-disable-next-line -->
  <el-dialog
    :modal="true"
    :modal-append-to-body="true"
    :title="tittle"
    :visible="is_show"
    :width="width"
    :height="height"
    :close-on-click-modal="false"
    :show-close="true"
    :close-on-press-escape="true"
    center
  >
    <slot></slot>
  </el-dialog>
</template>

<script>
export default {
  name: "ChangePwdWindow",
  props: {
    is_show: {
      type: Boolean,
      default: true,
    },
    switchStyle: {
      type: Boolean,
      default: true,
    },
    tittle: {
      type: String,
      default: "标题",
    },
    width: {
      type: String,
      default: "35%",
    },
    height: {
      type: String,
      default: "1000px",
    },
  },
};
</script>

<style scoped>
.dialog-footer button:first-child {
  margin-right: 10px;
}
</style>
