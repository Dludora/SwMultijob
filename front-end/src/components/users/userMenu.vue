<template>
    <el-dropdown>
      <el-avatar :size="40" :src="src" class="avater"/>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item v-for="mi in userMenus">
            <router-link :to=mi.to>{{mi.label}}</router-link>
          </el-dropdown-item>
          <el-dropdown-item>
            <a href="#" @click="logout">退出登录</a>
          </el-dropdown-item>
        </el-dropdown-menu>
      </template>
    </el-dropdown>
</template>

<script>
export default {
  name: "userMenu",
  data() {
    return {
      src: require('D:\\My Blog\\SwMultijob\\front-end\\src\\assets\\head.png'),
      userMenus: [
        {
          label: '个人资料',
          to: '/user/profile',
        },
        {
          label: '我的收藏',
          to: '/user/collect',
        },
        {
          label: '浏览历史',
          to: '/user/history',
        },
        {
          label: '我的关注',
          to: '/user/concerned',
        },
        {
          label: '我的博客',
          to: '/user/myBlogs',
        },
      ]
    }
  },
  methods: {
    logout() {
      this.$store.commit('clearToken');
    }
  }
}
</script>

<style scoped>
.avater {
  margin: auto;
  cursor: pointer;
}
</style>