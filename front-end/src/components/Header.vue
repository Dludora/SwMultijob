<template>
  <Sidebar v-model:visible="visibleFull" :baseZIndex="10000" position="right">
    <el-button size="small" v-for="label in labels" @click="labelSearch(label)">{{label}}</el-button>
  </Sidebar>
  <div class="Header">
    <div class="Header_main">
      <div class="brand" @click="this.$router.push({name: 'home'})">
        <router-link to="/">
          Our Blog
        </router-link>
      </div>
      <div class="Header-nav">
        <li v-for="link in links">
          <router-link :to=link.path active-class="blue">
          <span>{{link.name}}</span>
          </router-link>
        </li>
        <Button label="分类" @click="visibleFull = true"  class="p-button-secondary"/>
      </div>
      <div class="p-input-icon-left search">
            <i class="pi pi-search"/>
            <InputText type="text" placeholder="Search" class="search" v-model="key"
              @keyup.enter.native="handleSearchMember"/>
      </div>
      <div class="top-menu">
        <li v-if="!isLogin">
          <a href="/login">登录/注册</a>
        </li>
        <li v-else>
          <userMenu/>
        </li>
      </div>
    </div>
  </div>

</template>

<script>
import Sidebar from 'primevue/sidebar'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
import userMenu from "@/components/users/userMenu";
export default {
  components: {
    Sidebar,
    Button,
    InputText,
    userMenu,
  },
  data() {
    return {
      key: '',
      labels: [
          '后端',
          '前端',
          '移动开发',
          '编程语言',
          'Java',
          'Python',
          '人工智能',
          '大数据',
          '数据结构与算法',
          '云原生',
          '云平台',
          '运维',
          '服务器',
          '操作系统',
          '数据库管理',
          'IOS',
          'Android',
          '小程序',
          '硬件开发',
          '区块链'
      ],
      visibleFull: false,
      links: []
    }
  },
  created() {

  },
  computed: {
    isLogin() {
      return this.$store.state.user.token;
    }
  },
  methods: {
    handleSearchMember() {
      this.$router.push({name: 'search', params: {key: this.key}})
    },
    labelSearch(label) {
      this.$router.push({name: 'search', params: {key: label}})
    }
  }
}
</script>

<style scoped>
.el-button {
  margin-left: 0px;
  margin-right: 12px;
  margin-bottom: 12px;
}
.blue span {
  color: #4d90fe;
}
.Header {
  width: auto;
  height: 60px;
  border-bottom: 1px solid #ccc;
  z-index: 1041;
  position: relative;
  right: 0;
  left: 0;
  top: 0;
  box-shadow: 0 3px 6px 0 rgb(50 50 50 / 30%);
  background-color: #f7fcfe;
}

.Header_main {
  display: flex;
  height: 100%;
  width: 100%;
}

.brand {
  width: 140px;
  height: 100%;
  margin-left: 24px;
  margin-right: 16px;
  cursor: pointer;
}
.brand a {
  text-decoration: none;
  line-height: 60px;
  font-weight: 600;
  font-size: 20px;
  color: #161616;
  font-family: Lora,'Times New Roman',serif;
  /*color: #a3a3a3;*/
  font-style: italic;
}
.brand:hover a{
  color: #4d90fe;
}

.Header-nav {
  flex: 1;
  display: flex;
  height: 100%;
  margin: 0;
}
.Header-nav li {
  width: 80px;
  height: 100%;
  font-weight: 600;
  display: inline-block;
  position: relative;
}

.Header-nav li:hover a{
  color: #4d90fe;
}

.Header-nav li a {
  line-height: 60px;
  text-decoration: none;
  color: #161616;
  cursor: pointer;
}

.search {
  height: 100%;
  width: 70%;
  flex: 2;
}

.top-menu {
  display: flex;
  height: 100%;
  margin-right: 20px;
}
.top-menu li {
  height: 100%;
  font-weight: 600;
  display: inline-block;
  position: relative;
}

.top-menu li:hover a{
  color: #4d90fe;
}


.top-menu li a {
  border-top: 1px solid rgba(0,0,0,0);
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding: 0 24px;
  line-height: 60px;
  height: 61px;
  text-decoration: none;
  text-transform: uppercase;
  margin-top: -1px;
  color: #161616;
  cursor: pointer;
  text-align: center;
}
li {
  list-style: none;
}
</style>