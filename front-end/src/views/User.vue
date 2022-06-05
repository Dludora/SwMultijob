<template>
  <el-container>
    <el-aside
      width="200px">
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
        <el-menu-item v-for="item in items" :index="item.path">
          <span>{{item.label}}</span>
        </el-menu-item>
      </el-menu>
    </el-aside>
    <el-container>
      <router-view />
    </el-container>
  </el-container>
</template>


<script>

export default {
  name: "PersonalSpace",
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
.el-menu-item span{
  font-size: 20px;
  font-weight: bold;
}
</style>