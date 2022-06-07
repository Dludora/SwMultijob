<template>
  <el-container style="margin-top: 30px">
    <el-aside class="blog-aside" width="270px">
      <div class="author">
        <el-card class="author-card">
          <template #header>
            <div class="card-header">
              <div class="card-avatar">
                <el-avatar :size="60" :src="blogForm.author.imgSrc" />
              </div>
              <div class="card-message">
                <span>{{blogForm.author.nickName}}</span>
              </div>
            </div>
          </template>
          <el-row :gutter="20" style="margin-bottom: 15px">
            <el-col :span="8" style="text-align: center">1</el-col>
            <el-col :span="8" style="text-align: center">2</el-col>
            <el-col :span="8" style="text-align: center">3</el-col>
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
          <Avatar size="large" class="avatar-icon" icon="pi pi-thumbs-up" shape="circle"/>
          <!--  <i class="pi pi-heart-fill"></i>-->
        </el-row>
        <el-row>
          <Avatar size="large" class="avatar-icon" icon="pi pi-bookmark" shape="circle"/>
          <!--  <i class="pi pi-heart-fill"></i>-->
        </el-row>
        <el-row>
          <Avatar size="large" class="avatar-icon" icon="pi pi-heart" shape="circle"/>
          <!--  <i class="pi pi-heart-fill"></i>-->
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
      goTop: false,
      blogForm: {
        author: {
          nickName: 'Dludora',
          imgSrc: require('../../assets/head.png')
        },
        headline: '题目',
        text: ''
      }
    }
  },
  created() {
    axios({
      method: 'post',
      url: 'getBlog'
    }).then(res => {
      this.blogForm.text = res.data.blog;
      // console.log(res)
    }).catch(err => {
      console.log(err)
    })
  },
  methods: {
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
</style>

