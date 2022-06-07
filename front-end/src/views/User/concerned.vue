<template>
  <el-main style="min-height: calc(100vh - 80px);">
    <el-card
        :body-style="{padding: '5px'}"
        style="margin-top: 5px;"
        v-for="blogger in bloggers.slice((currentPage-1)*pagesize, currentPage*pagesize)">
<!--      <el-col>-->
        <el-avatar :src="blogger.avatar" size="large"></el-avatar>
<!--      </el-col>-->
<!--      <el-col>-->
        {{blogger.nickname}}
      <el-button round>已关注</el-button>
<!--      </el-col>-->
    </el-card>
    <el-pagination
        v-model:currentPage=currentPage
        background
        v-model:page-size=pagesize
        v-model:total=total
        layout="total, prev, pager, next, jumper"
        @current-change="handleCurrentChange"
      />

  </el-main>

</template>

<script>
export default {
  name: "concerned",
  data() {
    return {
      bloggers: [
        {
          id: 1,
          avatar: require('../../assets/head.png'),
          nickname: 'xxx'
        },
        {
          id: 1,
          avatar: require('../../assets/head.png'),
          nickname: 'xxx'
        },
        {
          id: 1,
          avatar: require('../../assets/head.png'),
          nickname: 'xxx'
        },
        {
          id: 1,
          avatar: require('../../assets/head.png'),
          nickname: 'xxx'
        },
        {
          id: 1,
          avatar: require('../../assets/head.png'),
          nickname: 'xxx'
        },
        {
          id: 1,
          avatar: require('../../assets/head.png'),
          nickname: 'xxx'
        },
        {
          id: 1,
          avatar: require('../../assets/head.png'),
          nickname: 'xxx'
        },
        {
          id: 1,
          avatar: require('../../assets/head.png'),
          nickname: 'xxx'
        },
        {
          id: 1,
          avatar: require('../../assets/head.png'),
          nickname: 'xxx'
        },
        {
          id: 1,
          avatar: require('../../assets/head.png'),
          nickname: 'xxx'
        },




      ],
      currentPage: 1,
      total: 20,
      pagesize: 7,
    }
  },
  methods: {
    handleCurrentChange(newSize) {
        this.currentPage = newSize;
    },
  }
}
</script>

<style scoped>

</style>