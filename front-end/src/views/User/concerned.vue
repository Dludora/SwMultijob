<template>
  <el-main style="height: 650px">
    <div class="cards">
      <el-card
          v-if="follow_user_list.length !== 0"
          :body-style="{padding: '3px'}"
          style="margin-bottom: 10px;"
          v-for="blogger in follow_user_list.slice((currentPage-1)*pagesize, currentPage*pagesize)">
        <div class="card-container">
          <div>
            <el-avatar :src="blogger.followAvatar"
                     size="large"
                     class="blogger-avatar"
                    @click="showBlogger(blogger)"/>
          </div>
          <div class="blogger-message">
            <span class="nickname">{{blogger.followName}}</span>
          </div>
          <el-button round @click="cancelFollow(blogger)">已关注</el-button>
        </div>
      </el-card>
      <span v-else>暂无关注</span>
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
import axios from "axios";
import {ElMessage} from "element-plus";

export default {
  name: "concerned",
  data() {
    return {
      follow_user_list: [],
      currentPage: 1,
      total: 20,
      pagesize: 7,
    }
  },
  created() {
    this.load()
  },
  methods: {
    load() {
      const formData = new FormData();
      formData.append('token', this.$store.state.user.token)
      axios({
        method: 'post',
        url: 'stars/get_follow_list',
        data: formData
      }).then(res => {
        console.log(res.data)
        if(res.data.errno === 1002) {
          this.follow_user_list = []
          this.total = 0
        } else if(res.data.errno === 0) {
          this.follow_user_list = res.data.follow_user_list
          this.total = res.data.size
        }
      }).catch(err =>{
        console.log(err)
        ElMessage.error('加载关注列表失败')
      })
    },
    handleCurrentChange(newSize) {
        this.currentPage = newSize;
    },
    cancelFollow(blogger) {
      const followId = blogger.followId
      const formData = new FormData();
      formData.append('token', this.$store.state.user.token)
      formData.append('followId', followId)
      axios({
        method: 'post',
        url: 'stars/delFollow',
        data: formData
      }).then(res => {
        ElMessage.success(res.data.msg)
        this.load()
      }).catch(err => {
        ElMessage.error('取消关注失败')
      })
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