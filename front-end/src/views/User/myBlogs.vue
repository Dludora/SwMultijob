<template>
    <el-main>
      <el-button style="margin-bottom: 20px" @click="this.$router.push({name: 'editor', params: {blogId: -1}})">
        新增博客
      </el-button>
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
    </el-main>
</template>

<script>
import Dialog from 'primevue/dialog';
import Button from "primevue/button";
import myTable from "@/components/myTable";
import axios from "axios";
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
      total: 100,         // 总数居条数
      query: '',     // 查询参数
      currentPage: 1,    // 当前页码
      pagesize: 8,       // 每页显示条数
    }
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
        if(res.data.errno === 0) {

        } else if(res.data.errno === 1002) {
          this.blogs = []
        }
      })
    },
    // 控制页面的切换
    handleCurrentChange(newSize) {
        this.currentPage = newSize;
    },
    handleDelete(index) {
      this.blogs.splice(index, 1)
    },
    modify(index) {
      this.$router.push({name: 'view', params: {blogId: this.blogs[index].articleId}})
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
</style>