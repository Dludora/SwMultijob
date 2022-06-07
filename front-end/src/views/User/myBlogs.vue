<template>
    <el-main >
      <el-table :data="collections.slice((currentPage-1)*pagesize, currentPage*pagesize)"
                stripe
                style="width: 1200px;"
                height="530">
        <el-table-column fixed prop="blogName" label="博客名" width="700" />
        <el-table-column prop="blogAuthor" label="修改日期" width="200" />
        <el-table-column fixed="right" label="操作" width="270">
          <template #default="scope">
            <el-button type="text">修改文章</el-button>
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
export default {
  name: "collect",
  components: {
    Dialog,
    Button,
    myTable
  },
  data() {
    return {
      collections: [
        {
          blogName: '愚蠢',
          blogAuthor: '张三',
          blogUrl: '',
        },
        {
          blogName: '呆瓜',
          blogAuthor: '李四',
          blogUrl: '',
        },
        {
          blogName: '傻子',
          blogAuthor: '王五',
          blogUrl: '',
        },
          {
          blogName: '傻子',
          blogAuthor: '王五',
          blogUrl: '',
        },
        {
          blogName: '傻子',
          blogAuthor: '王五',
          blogUrl: '',
        },
        {
          blogName: '傻子',
          blogAuthor: '王五',
          blogUrl: '',
        },
        {
          blogName: '傻子',
          blogAuthor: '王五',
          blogUrl: '',
        },
        {
          blogName: '傻子',
          blogAuthor: '王五',
          blogUrl: '',
        },
        {
          blogName: '傻子',
          blogAuthor: '王五',
          blogUrl: '',
        },
        {
          blogName: '傻子',
          blogAuthor: '王五',
          blogUrl: '',
        },
        {
          blogName: '傻子',
          blogAuthor: '王五',
          blogUrl: '',
        },
      ],
      // 是否加载数据
      total: 100,         // 总数居条数
      query: '',     // 查询参数
      currentPage: 1,    // 当前页码
      pagesize: 10,       // 每页显示条数
    }
  },
  methods: {
    load() {

    },
    // 控制页面的切换
    handleCurrentChange(newSize) {
        this.currentPage = newSize;
        // this.load()
    },
    handleDelete(index) {
      this.collections.splice(index, 1)
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