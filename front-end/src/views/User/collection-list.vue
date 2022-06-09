<template>
  <el-main>
    <div v-if="total">
      <el-table :data="this.star_list"
                stripe
                style="width: 1200px;"
                height="530">
      <el-table-column fixed prop="title" label="博客名" width="700" />
      <el-table-column prop="author" label="作者" width="200" />
      <el-table-column fixed="right" label="操作" width="270">
        <template #default="scope">
          <el-button type="text" @click="handleCheck(scope.$index)">查看文章</el-button>
          <el-button
              @click="handleDelete(scope.$index)"
              type="text">取消收藏</el-button>
          </template>
      </el-table-column>
    </el-table>
      <el-pagination
        v-model:currentPage=currentPage
        background
        v-model:page-size=pagesize
        v-model:total=total
        layout="total, prev, pager, next, jumper"
        style="margin-top: 45px"
        @current-change="handleCurrentChange"
      />
    </div>
    <div class="none" v-else>
      <div class="monkey">
        <img src='../../assets/monkey.png'>
      </div>
      <div style="text-align: center; margin-top: 20px">
        <span class="sorry">
          <em>您还没有收藏任何内容哦</em>
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
  computed: {
    displayed() {
      if(this.star_list.length !== 0) {
        return this.star_list.slice((this.currentPage-1)*this.pagesize, this.currentPage*this.pagesize)
      } else {
        return this.star_list
      }
    }
  },
  data() {
    return {
      star_list: [],
      // 是否加载数据
      total: null,         // 总数居条数
      currentPage: 1,    // 当前页码
      pagesize: 10,       // 每页显示条数
    }
  },
  created() {
    this.load();
  },
  methods: {
    load() {
      const formData = new FormData();
      formData.append('token', this.$store.state.user.token)
      axios({
        method: 'post',
        url: 'stars/get_all_star_article',
        data: formData
      }).then(res => {
        // console.log(res)
        if(res.data.errno === 1002) {
          this.star_list = []
          this.total = 0
        } else if(res.data.errno === 0) {
          this.star_list = res.data.stars_list
          this.total = res.data.size
        }
      }).catch(err =>{
        this.star_list = []
      })
    },
    // 控制页面的切换
    handleCurrentChange(newSize) {
      this.currentPage = newSize;
    },
    handleDelete(index) {
      const formData = new FormData()
      formData.append('token', this.$store.state.user.token)
      formData.append('articleId', this.star_list[index].articleId)
      axios({
        method: 'post',
        url: 'stars/delStars',
        data: formData
      }).then(res => {
        ElMessage.success(res.data.msg)
        this.load()
      }).catch(err => {
        ElMessage.error('取消失败！')
      })
    },
    handleCheck(index) {
      const articleId = this.star_list[index].articleId
      console.log(articleId)
      this.$router.push({name: 'view', params: {blogId: articleId}})
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
  /*background-color: #3370ff;*/
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