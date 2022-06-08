<template>
  <el-main>
    <el-table :data="history_list.slice((currentPage-1)*pagesize, currentPage*pagesize)"
                stripe
                style="width: 1200px;"
                height="530">
        <el-table-column fixed prop="title" label="博客名" width="500" />
        <el-table-column prop="author" label="作者" width="200" />
        <el-table-column prop="time" label="浏览时间" width="200" />
        <el-table-column fixed="right" label="操作" width="270">
          <template #default="scope">
            <el-button type="text" @click="handleCheck(scope.$index)">查看文章</el-button>
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
      history_list: [],
      // 是否加载数据
      total: 100,         // 总数居条数
      query: '',     // 查询参数
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
        url: 'stars/get_history_list',
        data: formData
      }).then(res => {
        console.log(res.data)
        if(res.data.errno === 1002) {
          this.history_list = []
          this.total = 0
        } else if(res.data.errno === 0) {
          this.history_list = res.data.hitory_list
          this.total = res.data.size
        } else {
          ElMessage(res.data.msg)
        }
      }).catch(err =>{
        console.log(err)
      })
    },
    // 控制页面的切换
    handleCurrentChange(newSize) {
      this.currentPage = newSize;
    },
    handleCheck(index) {
      const articleId = this.history_list[index].articleId
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
</style>