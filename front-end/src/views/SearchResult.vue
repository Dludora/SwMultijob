<template>
  <div class="home">
    <div class="tags" v-if="total">
      <h1>{{this.$route.params.key}}</h1>
    </div>
    <div class="content" v-if="total">
      <el-card v-for="article in result_list.slice((currentPage-1)*maxDisplay, currentPage*maxDisplay)" shadow="never">
        <router-link :to="{name: 'view', params: {blogId: article.articleId}}">
          <h2>{{article.title}}</h2>
          <h4>{{article.description}}</h4>
        </router-link>
        <p>Posted by {{article.author}}</p>
      </el-card>
      <li class="next" @click="currentPage++" v-if="isDisplayNext">
          MORE BLOGS →
        </li>
      <li class="before" @click="currentPage--" v-if="isDisplayBefore">
          NEWER BLOGS →
        </li>
    </div>
    <div class="none" v-else>
      <div class="monkey">
        <img src='../assets/monkey.png'>
      </div>
      <div style="text-align: center; margin-top: 20px">
        <span class="sorry">
          抱歉, 没有找到
          <em>{{this.$route.params.key}}</em>
          相关内容
        </span>
      </div>
    </div>
<!--    <div class="footer">-->
<!--    </div>-->
  </div>
</template>
<script>
import axios from "axios";
import {ElMessage} from "element-plus";

export default {
  name: "SearchResult",
  computed: {
    isDisplayNext() {
      return this.currentPage*this.maxDisplay < this.result_list.length
    },
    isDisplayBefore() {
      return this.currentPage > 1
    }
  },
  data() {
    return {
      result_list: [],
      maxDisplay: 4,
      currentPage: 1,
      total: null
    }
  },
  created() {
    // console.log(this.$route.params.key)
    this.load()
  },
  methods: {
    load() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('key', this.$route.params.key)
      axios({
        method: 'post',
        url: 'comment_like/search',
        data: formData
      }).then(res => {
        if(res.data.errno === 0) {
          this.result_list = res.data.result_list
          this.total = res.data.result_list_size
        } else {
          ElMessage.error(res.data.msg)
        }
      }).catch(err => {
        ElMessage.error('搜索失败')
      })
    }
  }
}
</script>
<style scoped>
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
  margin-bottom: 70px;
  min-height: calc(100% - 180px);
}
.tags {
  padding: 10px;
  border-bottom: #1f2329 5px;
  background-color: #ffffff;
}
.content {
  background-color: #ffffff;
  margin-top: 30px;
}
.footer {
  height: 150px;
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
.none {
  margin-top: 10px;
  padding: 40px;
}
.monkey {
  width: 120px;
  height: 95px;
  margin: 0 auto;
}
em {
  color: #fc5531;
}
img {
  width: 100%;
  height: 100%;
}
/*.sorry {*/
/*  display: block;*/
/*  margin: 0 auto;*/
/*}*/
</style>