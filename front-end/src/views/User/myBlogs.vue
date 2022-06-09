<template>
    <el-main>
      <el-button style="margin-bottom: 15px" @click="this.$router.push({name: 'editor', params: {blogId: -1}})">
        新增博客
      </el-button>
      <div v-if="total">
          <el-table :data="blogs.slice((currentPage-1)*pagesize, currentPage*pagesize)"
                  stripe
                  style="width: 1200px;"
                  height="480">
          <el-table-column fixed prop="title" label="博客名" width="700" />
          <el-table-column fixed="right" label="操作" width="270">
            <template #default="scope">
              <el-button type="text" @click="modify(scope.$index)">修改文章</el-button>
              <el-button
                  @click="handleDelete(scope.$index)"
                  type="text">删除文章</el-button>
            </template>
          </el-table-column>
        </el-table>
        <el-pagination
          v-model:currentPage=currentPage
          background
          v-model:page-size=pagesize
          v-model:total=total
          layout="total, prev, pager, next, jumper"
          @current-change="handleCurrentChange"
          style="margin-top: 45px"
        />
      </div>
      <div class="none" v-else>
        <div class="monkey">
          <img src='../../assets/monkey.png'>
        </div>
        <div style="text-align: center; margin-top: 20px">
          <span class="sorry">
            <em>您还没有发布任何内容哦</em>
          </span>
        </div>
      </div>
    </el-main>
</template>

<script>
import Dialog from 'primevue/dialog';
import Button from "primevue/button";
import myTable from "@/components/myTable";
import axios from "axios";
import {ElMessage} from "element-plus";
export default {
  name: "collect",
  components: {
    Dialog,
    Button,
    myTable
  },
  data() {
    return {
      blogs: [

      ],
      // 是否加载数据
      total: null,         // 总数居条数
      query: '',     // 查询参数
      currentPage: 1,    // 当前页码
      pagesize: 8,       // 每页显示条数
    }
  },
  created() {
    this.load()
  },
  methods: {
    load() {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      axios({
        method: 'post',
        url: 'comment_like/get_my_article',
        data: formData
      }).then(res => {
        console.log(res)
        if(res.data.errno === 0) {
          this.blogs = res.data.article_list
          this.total = this.blogs.length
        } else if(res.data.errno === 1002) {
          this.blogs = []
          this.total = 0
        }
      })
    },
    // 控制页面的切换
    handleCurrentChange(newSize) {
        this.currentPage = newSize;
    },
    handleDelete(index) {
      const formData = new FormData
      formData.append('token', this.$store.state.user.token)
      formData.append('articleId', this.blogs[index].articleId)
      axios({
        method: 'post',
        url: 'backend/deleteArticle',
        data: formData
      }).then(res => {
        if(res.data.errno === 0) {
          this.load()
        } else {
          ElMessage.error(res.data.msg)
        }
      })
    },
    modify(index) {
      this.$router.push({name: 'editor', params: {blogId: this.blogs[index].articleId}})
    }
  },
}
</script>

<style scoped>
.el-row {
  margin-top: 16px;
}
.el-col {
  line-height: 32px;
}
.header {
  border-bottom: #1f2329 1px;
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
</style>