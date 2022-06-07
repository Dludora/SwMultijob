<template>
  <el-main style="height: 650px">
    <div class="cards">
      <el-card
          :body-style="{padding: '3px'}"
          style="margin-bottom: 10px;"
          v-for="blogger in bloggers.slice((currentPage-1)*pagesize, currentPage*pagesize)">
        <div class="card-container">
          <div>
            <el-avatar :src="blogger.avatar"
                     size="large"
                     class="blogger-avatar"
                    @click="showBlogger(blogger)"/>
          </div>
          <div class="blogger-message">
            <span class="nickname">{{blogger.nickname}}</span>
          </div>
          <el-button round>已关注</el-button>
        </div>
      </el-card>
    </div>
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
    showBlogger(blogger) {
      console.log(blogger)
    }
  }
}
</script>

<style scoped>
.blogger-avatar {
  cursor: pointer;
}
.cards {
  height: 565px;
  width: 1200px;
}
.card-container {
  width: 100%;
  padding: 0 30px;
  display: flex;
}
.nickname {
  line-height: 56px;
  font-size: 20px;
}
.blogger-message {
  margin-left: 10px;
}
.el-button {
  margin-top: auto;
  margin-bottom: auto;
  margin-left: auto;
}
</style>