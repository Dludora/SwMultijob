<template>
  <Header class="header"/>
  <router-view class="main-content"/>
  <div class="mainFooter">
    友情赞助：北京航空航天大学软件学院
  </div>
</template>


<script>
import Header from './components/Header'

export default {
  components: {
    Header
  }
}

</script>
<style>
body {
  background: #f5f6f7;
  height: 100%;
  display: flex;
  flex-direction: column;
}
html, body #app{
  height: 100%;
}
.header {
  flex: 0;
}
.main-content {
  /*height: 100%;*/
  flex: 1;
}
.mainFooter {
  flex: 0;
  font-size: 15px;
  height: 30px;
  line-height: 30px;
  background-color: #f7fcfe;
  box-shadow: 0 3px 6px 0 rgb(50 50 50 / 30%);
  text-align: center;
  /*float: left;*/
}
</style>
