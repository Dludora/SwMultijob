<template>
  <Sidebar v-model:visible="visibleFull" :baseZIndex="10000" position="full">
    你是煞笔
  </Sidebar>
  <div class="Header">
    <div class="Header_main">
      <div class="brand">
        <a href="/">
          shabi
        </a>
      </div>
      <div class="Header-nav">
        <li>
          <a href="/">首页</a>
        </li>
        <li>
          <a href="/about">关于</a>
        </li>
        <Button label="分类" @click="visibleFull = true"  class="p-button-secondary"/>
      </div>
      <div class="p-input-icon-left search">
            <i class="pi pi-search"/>
            <InputText type="text" placeholder="Search" class="search"/>
      </div>
      <div class="top-menu">
        <li>
          <a href="/login">登录/注册</a>
        </li>
      </div>
    </div>
  </div>

</template>

<script>
import Sidebar from 'primevue/sidebar'
import Button from 'primevue/button'
import InputText from 'primevue/inputtext'
export default {
  components: {
    Sidebar,
    Button,
    InputText,
  },
  data() {
    return {
      visibleFull: false,
    }
  }
}
</script>

<style scoped>
.Header {
  width: 100%;
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
}
.brand a {
  display: inline-block;
  width: 100%;
  height: 100%;
  text-decoration: none;
  line-height: 60px;
  font-weight: 600;
  color: #161616;
}
.brand:hover a{
  color: #4d90fe;
}
img {
  height: 50%;
  margin-top: 15px;
  margin-left: 10px;
}


.Header-nav {
  flex: 1;
  display: flex;
  height: 100%;

  margin: 0;
}
.Header-nav li {
  height: 100%;
  font-weight: 600;
  display: inline-block;
  position: relative;
}
.Header-nav li:hover a{
  color: #4d90fe;
}
.Header-nav li a {
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

.search {
  height: 100%;
  width: 70%;
  flex: 2;
}

.top-menu {
  display: flex;
  height: 100%;
  margin: 0;
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