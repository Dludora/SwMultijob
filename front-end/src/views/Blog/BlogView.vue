<template>
  <el-container style="margin-top: 30px">
    <el-aside class="blog-aside" width="270px">
      <div class="author">
        <el-card class="author-card">
          <template #header>
            <div class="card-header">
              <div class="card-avatar blogger-avatar">
                <el-avatar :size="60" :src="blogForm.author.imgSrc" />
              </div>
              <div class="card-message blogger-message">
                <span>{{blogForm.author.nickName}}</span>
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
          <Avatar v-if="isCollected" size="large" class="avatar-icon" icon="pi pi-bookmark" shape="circle" style="color: red" @click="delCollect"/>
          <Avatar v-else size="large" class="avatar-icon" icon="pi pi-bookmark" shape="circle" @click="collect"/>
        </el-row>
        <el-row>
          <Avatar v-if="isFollowed" size="large" class="avatar-icon" icon="pi pi-heart-full" shape="circle" style="color: red" @click="delFollow"/>
          <Avatar v-else size="large" class="avatar-icon" icon="pi pi-heart" shape="circle" @click="follow"/>
        </el-row>
      </div>
      <el-backtop :right="20" :bottom="100" />
    </el-aside>
    <el-container style="width: 270px;">
      <el-header>
        <p>{{blogForm.headline}}</p>
      </el-header>
      <el-main>
        <div class="blog-view">
          <v-md-preview :text="blogForm.text"></v-md-preview>
        </div>
      </el-main>
      <el-footer>

      </el-footer>
    </el-container>
  </el-container>

</template>

<script>
import Avatar from "primevue/avatar";
import axios from "axios";

export default {
  name: "BlogView",
  components: {
    Avatar,
  },
  data() {
    return {
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
        stars: null,
        description: '',
        label: [],
        headline: '题目',
        text: ''
      },
    }
  },
  created() {
    this.load()
  },
  methods: {
    load() {
      this.blogId = this.$route.params.blogId
      // console.log(this.blogId)
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
          this.blogForm.label = res.data.label
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
        }
        // console.log(res)
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
        this.load()
      })
    },
    follow() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('articleId', this.$route.params.blogId)
      axios({
        method: 'post',
        url: 'stars/addFollow',
        data: formData
      }).then(res => {
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
      formData.append('articleId', this.$route.params.blogId)
      axios({
        method: 'post',
        url: 'stars/delFollow',
        data: formData
      }).then(res => {
        this.load()
      })
    }
  }
}
</script>

<style scoped>
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

