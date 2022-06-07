<template>
  <Header />
  <router-view/>
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
}
html, body #app{
  height: 100%;
}

</style>
