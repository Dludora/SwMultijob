<template>
  <div class="home">
    <div class="tags">
        <el-avatar :src="formPersonal.avatarAddr" :size=100></el-avatar>
        <div style="margin-left: 30px; flex: 2">
          <h2>{{formPersonal.username}}</h2>
          <h4>粉丝量：<em>{{this.formPersonal.follows}}</em></h4>
        </div>

        <el-button v-if="formPersonal.isFollowed" @click="delFollow" size="large" round type="info">已关注</el-button>
        <el-button v-else @click="follow" size="large" type="danger" round>未关注</el-button>

      </div>
    <h2>文章</h2>
    <div class="content" v-if="isDisplay">
      <el-card v-for="article in blogs.slice((currentPage-1)*maxDisplay, currentPage*maxDisplay)" shadow="never">
          <router-link :to="{name: 'view', params: {blogId: article.id}}">
            <h2>{{article.title}}</h2>
            <h4>{{article.discription}}</h4>
          </router-link>
        </el-card>
      <li class="next" @click="currentPage++" v-if="isDisplayNext">
          MORE BLOGS →
        </li>
      <li class="before" @click="currentPage--" v-if="isDisplayBefore">
          NEWER BLOGS →
        </li>
    </div>
    <div class="else" v-else>
      <div class="monkey">
        <img src='../../assets/monkey.png'>
      </div>
      <div style="text-align: center; margin-top: 20px">
        <span class="sorry">
          <em>该用户还没有上传文章</em>
        </span>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "otherHome",
  data() {
    return {
      formPersonal: {
        avatarAddr: '',
        username: '',
        sex: '',
        birthday: '',
        resume: '',
        email: '',
        follows: null,
        isFollowed: null,
        description: ''
      },
      blogs: [],
      currentPage: 1,
      total: 20,
      maxDisplay: 5,
    }
  },
  computed: {
    isDisplayNext() {
      return this.currentPage*this.maxDisplay < this.blogs.length
    },
    isDisplayBefore() {
      return this.currentPage > 1
    },
    isDisplay() {
      return this.blogs.length
    }
  },
  created() {
    this.load()
  },
  methods: {
    load() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('authorId', this.$route.params.userId)
      axios({
        method: 'post',
        url: 'backend/getOtherInformation',
        data: formData
      }).then(res => {
        this.formPersonal.avatarAddr = res.data.avatarAddr
        this.formPersonal.username = res.data.username
        this.formPersonal.sex = res.data.sex
        this.formPersonal.description = res.data.discription
        this.formPersonal.follows = res.data.follows
        this.formPersonal.isFollowed = res.data.isFollowed
        this.blogs = res.data.blogs

        console.log(res.data)
      })
    },
    handleCurrentChange(newSize) {
      this.currentPage = newSize;
    },
    follow() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('followId', this.$route.params.userId)
      axios({
        method: 'post',
        url: 'stars/addFollow',
        data: formData
      }).then(res => {
        // console.log(res)
        this.load()
      })
    },
    delFollow() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('followId', this.$route.params.userId)
      axios({
        method: 'post',
        url: 'stars/delFollow',
        data: formData
      }).then(res => {
        this.load()
      })
    },
  }
}
</script>
<style scoped>
em {
  color: #fc5531;
}
a {
  text-decoration: none;
  color: #1f2329;
}
a:hover {
  color: #337ab7
}
h2 {
  margin-top: 10px;
  font-size: 26px;
  line-height: 1.3;
  margin-left: 10px;
  margin-bottom: 10px;
}
h4 {
  /*font-size: 15px;*/
  line-height: 1.3;
  margin: 0;
  font-weight: 400;
  margin-bottom: 10px;
}
p {
  font-weight: normal;
  font-family: Lora,'Times New Roman',serif;
  color: #a3a3a3;
  font-style: italic;
}
.home {
  margin-top: 20px;
  margin-left: 100px;
  margin-right: 100px;
  margin-bottom: 100px;
  min-height: calc(100% - 180px);
}
.tags {
  display: flex;
  padding: 10px;
  border-bottom: #1f2329 5px;
  background-color: #ffffff;
}
.content, .else{
  background-color: #ffffff;
  /*margin-top: 30px;*/
}
.else {
  min-height: calc(100% - 180px);
  padding: 40px;
}

.monkey {
  width: 120px;
  height: 95px;
  margin: 0 auto;
}
em {
  font-weight: bold;
  color: #fc5531;
}
img {
  width: 100%;
  height: 100%;
}

.el-button {
  margin-left: 0;
  margin-right: 10px;
  margin-bottom: 3px;
}
.next {
  box-shadow: #1f2329;
  cursor: pointer;
  float: right;
  display: inline-block;
  margin-top: 20px;
  font-size: 20px;
  font-weight: 700;
  padding: 25px 40px;
  background-color: #ffffff;
}
.next:hover {
  color: #ffffff;
  background-color: #337ab7
}
.before {
  box-shadow: #1f2329;
  cursor: pointer;
  float: left;
  display: inline-block;
  margin-top: 20px;
  font-size: 20px;
  font-weight: 700;
  padding: 25px 40px;
  background-color: #ffffff;
}
.before:hover {
  color: #ffffff;
  background-color: #337ab7
}
.el-button {
  margin-top: auto;
  margin-bottom: auto;
  margin-left: auto;
}
</style>