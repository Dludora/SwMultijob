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

.headerBar {
  width: 100%;
  height: 50px;
}
</style>
