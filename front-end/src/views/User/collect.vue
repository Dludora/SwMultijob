<template>
  <Dialog header="新建收藏夹" v-model:visible="isDisplay">

  </Dialog>
</template>

<script>
import Dialog from 'primevue/dialog'
export default {
  name: "collect",
  components: {
    Dialog,
  },
  data() {
    return {
      isDisplay: false,
      menu: []
    }
  }

}
</script>

<style scoped>

</style>