<template>
  <el-container style="margin-top: 30px; padding-bottom: 70px; min-height: 100%">
    <el-aside class="blog-aside" width="300px">
      <div class="author">
        <el-card class="author-card">
          <template #header>
            <div class="card-header">
              <div class="card-avatar blogger-avatar">
                <el-avatar :size="60" :src="blogForm.author.imgSrc" @click="this.$router.push({name: 'userHome', params: {userId: this.blogForm.author.authorId}})"/>
              </div>
              <div class="card-message blogger-message">
                <h3>{{blogForm.author.nickName}}</h3>
              </div>
            </div>
          </template>
          <el-row :gutter="20" style="margin-bottom: 15px">
            <el-col :span="8" style="text-align: center">{{this.blogForm.likes}}</el-col>
            <el-col :span="8" style="text-align: center">{{this.blogForm.stars}}</el-col>
            <el-col :span="8" style="text-align: center">{{this.blogForm.commentNum}}</el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="8" style="text-align: center">获赞数</el-col>
            <el-col :span="8" style="text-align: center">收藏数</el-col>
            <el-col :span="8" style="text-align: center">评论数</el-col>
          </el-row>
        </el-card>
      </div>
      <div class="icons">
        <el-row>
          <Avatar v-if="isLiked" size="large" class="avatar-icon" icon="pi pi-thumbs-up" shape="circle" style="color: red" @click="delLike"/>
          <Avatar v-else size="large" class="avatar-icon" icon="pi pi-thumbs-up" shape="circle" @click="like"/>
        </el-row>
        <el-row>
          <Avatar v-if="isCollected" size="large" class="avatar-icon" icon="pi pi-bookmark-fill" shape="circle" style="color: #a1a174" @click="delCollect"/>
          <Avatar v-else size="large" class="avatar-icon" icon="pi pi-bookmark" shape="circle" @click="collect"/>
        </el-row>
        <el-row>
          <Avatar v-if="isFollowed" size="large" class="avatar-icon" icon="pi pi-heart-fill" shape="circle" style="color: red" @click="delFollow"/>
          <Avatar v-else size="large" class="avatar-icon" icon="pi pi-heart" shape="circle" @click="follow"/>
        </el-row>
      </div>
      <el-backtop :right="20" :bottom="100" />
    </el-aside>
    <el-container style="width: 270px;">
      <el-header>
        <p>{{blogForm.headline}}</p>
        <div v-if="!displayTags">
          <el-button  size="small" v-for="label in blogForm.labels" @click="search(label)">{{label}}</el-button>
        </div>
      </el-header>
      <el-main>
        <div class="blog-view">
          <v-md-preview :text="blogForm.text"></v-md-preview>
        </div>
      </el-main>
      <el-footer height="auto">
        <div class="comment-room">
          <el-table
            :data="blogForm.comment_list"
            style="margin-bottom: 5px;">
            <el-table-column prop="username" label="用户" width="100"></el-table-column>
            <el-table-column prop="comment" label="评论" ></el-table-column>
          </el-table>
          <el-input
            v-model="myComment"
            :autosize="{ minRows: 2, maxRows: 4 }"
            style="max-width: 100%"
            type="textarea"
            placeholder="请填写评论~"
              />
          <el-button style="margin-top: 5px" @click="submitComment">提交</el-button>
        </div>
      </el-footer>
    </el-container>
  </el-container>
</template>

<script>
import Avatar from "primevue/avatar";
import axios from "axios";
import {ElMessage} from "element-plus";

export default {
  name: "BlogView",
  components: {
    Avatar,
  },
  computed: {
    displayTags() {
      return this.blogForm.labels.length > 0
    }
  },
  data() {
    return {
      myComment: '',
      isLiked: false,
      isCollected: false,
      isFollowed: false,
      blogId: null,
      blogForm: {
        author: {
          authorId: null,
          nickName: 'Dludora',
          imgSrc: require('../../assets/head.png')
        },
        likes: null,
        commentNum: null,
        comment_list: [],
        stars: null,
        description: '',
        labels: [],
        headline: '题目',
        text: ''
      },
    }
  },
  created() {
    this.load()
    console.log(this.displayTags)
  },
  methods: {
    load() {
      this.blogId = this.$route.params.blogId
      const formData = new FormData()
      formData.append('articleId',this.blogId)
      formData.append('token', this.$store.state.user.token)
      axios({
        method: 'post',
        url: 'backend/readArticle',
        data: formData
      }).then(res => {
        if(res.data.errno === 0) {
          this.blogForm.text = res.data.body
          this.blogForm.headline = res.data.title
          this.blogForm.labels = res.data.label
          this.blogForm.description = res.data.discription
          this.blogForm.author.nickName = res.data.authorName
          this.blogForm.author.imgSrc = res.data.avatarAddr
          this.blogForm.author.authorId = res.data.authorId
          this.blogForm.commentNum = res.data.commentnum
          this.blogForm.likes = res.data.likes
          this.blogForm.stars = res.data.stars
          this.isLiked = res.data.isLiked === 1
          this.isCollected = res.data.isStared === 1
          this.isFollowed = res.data.isFollowed === 1
          this.blogForm.comment_list = res.data.comment_list
          console.log(this.blogForm.comment_list)
        }
      }).catch(err => {
        console.log(err)
      })
      axios({
        method: 'post',
        url: 'stars/addHistory',
        data: formData
      })
    },
    like() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('articleId', this.$route.params.blogId)
      axios({
        method: 'post',
        url: 'comment_like/addLike',
        data: formData
      }).then(res => {
        // this.isLiked = true
        this.load()
      })
    },
    collect() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('articleId', this.$route.params.blogId)
      axios({
        method: 'post',
        url: 'stars/addStars',
        data: formData
      }).then(res => {
        console.log(res)
        this.load()
      }).catch(err => {
        console.log(err)
      })
    },
    follow() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('followId', this.blogForm.author.authorId)
      axios({
        method: 'post',
        url: 'stars/addFollow',
        data: formData
      }).then(res => {
        // console.log(res)
        this.load()
      })
    },
    delLike() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('articleId', this.$route.params.blogId)
      axios({
        method: 'post',
        url: 'comment_like/delLike',
        data: formData
      }).then(res => {
        this.load()
      })
    },
    delCollect() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('articleId', this.$route.params.blogId)
      axios({
        method: 'post',
        url: 'stars/delStars',
        data: formData
      }).then(res => {
        this.load()
      })
    },
    delFollow() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('followId', this.blogForm.author.authorId)
      axios({
        method: 'post',
        url: 'stars/delFollow',
        data: formData
      }).then(res => {
        this.load()
      })
    },
    submitComment() {
      if(!this.myComment) {
        ElMessage.error('写点什么吧QAQ')
        return
      }
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('content', this.myComment)
      formData.append('articleId', this.$route.params.blogId)
      axios({
        method: 'post',
        url: 'comment_like/addComment',
        data: formData
      }).then(res => {
        console.log(res)
        this.load()
      }).catch(err => {

      })
    },
    search(label) {
      // this.route.push({name: })
    }
  }
}
</script>

<style scoped>
.el-button {
  margin-left: 0px;
  margin-right: 12px;
  margin-top: 12px;
}
p {
  font-size: 30px;
  font-weight: bold;
}
.blog-aside {
  border: 1px #1f2329;
  position: relative;
}
.author {
  width: 300px;
  height: 250px;
}
.author-card {
  margin-left: 20px;
  width: 250px;
  margin-bottom: 50px;
  position: fixed;
}

.icons {
  width: 300px;
  position: fixed;
}
.el-row {
  margin-bottom: 20px;
}
.avatar-icon {
  cursor: pointer;
  background-color: #ffffff;
  box-shadow: 0 0 10px 2px rgb(0 0 0 / 6%);
  margin-left: 100px;
}
.blog-view {
  background-color: #ffffff;
}

.card-header {
  display: flex;
}
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
</style>

