<template>
  <el-container class="user-container">
    <el-aside
      width="200px"
      class="user-aside">
      <el-menu
          style="width: 200px; height: 100%"
          active-text-color="#ffd04b"
          background-color="#545c64"
          class="el-menu-vertical-demo"
          text-color="#fff"
          router
      >
        <div style="height: 20px"></div>
        <el-menu-item v-for="item in items" :index="item.path">
          <span>{{item.label}}</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container class="user-main">
      <router-view />
    </el-container>
  </el-container>
</template>


<script>

export default {
  name: "PersonalSpace",
  created() {
    this.$router.push('/user/profile')
  },
  data() {
    return {
      items: [
        {
          path:'/user/profile',
          label: '个人资料'
        },
          {
          path:'/user/collect',
          label: '我的收藏'
        },
          {
          path:'/user/history',
          label: '浏览历史'
        },
          {
          path:'/user/concerned',
          label: '我的关注'
        },
        {
          path:'/user/myBlogs',
          label: '我的博客'
        },
      ]
    }
  }
}
</script>

<style scoped>
.user-container {
  height: calc(100% - 80px);
  min-height: 600px;
}
.user-aside {
  height: 100%;
}
.user-main {
  height: 100%;
}
.is-active span {
  color: #ffd04b;
}
.el-menu-item span{
  font-size: 20px;
  font-weight: bold;
}
</style>