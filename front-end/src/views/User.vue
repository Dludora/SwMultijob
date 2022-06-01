<template>
  <el-col :span="12">
    <el-menu
        style="width: 200px; min-height: calc(100vh - 80px);"
        active-text-color="#ffd04b"
        background-color="#545c64"
        class="el-menu-vertical-demo"
        default-active="2"
        text-color="#fff"
        router
    >
      <div style="height: 20px"></div>
      <el-menu-item index="/user/profile">
        <span>个人资料</span>
      </el-menu-item>
      <el-menu-item index="/user/collect">
        <span>我的收藏</span>
      </el-menu-item>
      <el-menu-item index="/user/history">
        <span>浏览历史</span>
      </el-menu-item>
      <el-menu-item index="/user/concerned">
        <span>我的关注</span>
      </el-menu-item>
      <el-menu-item index="/user/myBlogs">
        <span>我的博客</span>
      </el-menu-item>
    </el-menu>
  </el-col>
  <div class="main-content">
    <router-view />
  </div>
</template>


<script>

export default {
  name: "PersonalSpace",

}
</script>

<style scoped>
.main-content {
  margin-left: 220px;
  width: 1200px;
  background-color: #f0f0f0;
}
.el-menu-item span{
  font-size: 20px;
  font-weight: bold;
}
</style>