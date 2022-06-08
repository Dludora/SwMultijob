<template>
    <el-dropdown>
      <el-avatar size="large" :src="avatar_src" class="avater"/>
      <template #dropdown>
        <el-dropdown-menu>
          <el-dropdown-item v-for="mi in userMenus">
            <router-link :to=mi.to active-class="act">{{mi.label}}</router-link>
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
  computed: {
    avatar_src: function() {
      if(!this.$store.state.user.avatar)
        return 'http://127.0.0.1:8000/user_img/img/default_img.png'
      return this.$store.state.user.avatar
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

a {
  text-decoration: none;
  color: #1f2329;
}

a:hover {
  color: #4d90fe;
}

.act span {
  color: #4d90fe;
}
</style>