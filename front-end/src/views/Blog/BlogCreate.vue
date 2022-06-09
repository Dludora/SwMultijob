<template>
  <Sidebar v-model:visible="visibleRight" position="right">

    <h3 style="font-size: 25px;">上传博客</h3>
      <el-form
          ref="blogForm"
          :model="blogForm"
          label-width="120px"
          label-position="top"
          style="max-width: 300px"
          :rules="blogRule">
        <el-form-item prop="headline" label="博客标题">
          <el-input type="text" placeholder="请填写博客标题" v-model="blogForm.headline" />
        </el-form-item>
        <el-form-item prop="headline" label="博客标题">
          <el-input
                  v-model="blogForm.description"
                  :autosize="{ minRows: 2, maxRows: 4 }"
                  style="max-width: 400px"
                  type="textarea"
                  placeholder="博客简介"
              />
        </el-form-item>
        <el-form-item prop="label" label="标签">
<!--          <div class="labels">-->
            <el-tag
                v-if="blogForm.label.length!==0"
                class="ml-2"
                closable
                :key="label"
                v-for="label in blogForm.label"
                @close="handleClose(tag)">
              {{label}}
            </el-tag>
            <span v-else>添加标签</span>
<!--          </div>-->
        </el-form-item>
      </el-form>
    <el-button size="small" v-for="label in labels" @click="addLabel(label)">{{label}}</el-button>

    <Button label="提交" icon="pi pi-check" class="p-button-secondary" autofocus @click="addBlogSubmit('blogForm')" style="margin-top: 30px"/>


  </Sidebar>
  <div id="main">
    <v-md-editor
        :disabled-menus="[]"
        v-model="blogForm.content"
        height="600px"
        @upload-image="handleUploadImage"
    ></v-md-editor>
    <Button class="pi pi-arrow-up" label=" 提交" iconPos="right" @click="()=>visibleRight=true" style="margin: 10px 30px"/>
  </div>
</template>

<script>
import Sidebar from "primevue/sidebar";
import Dialog from "primevue/dialog";
import Button from "primevue/button";
import axios from "axios";
import {ElMessage} from "element-plus";
export default {
  name: "BlogCreate",
  components: {
    Dialog,
    Button,
    Sidebar
  },
  data() {
    let checkBlogHeadline = (rule, value, callback) => {
      if(!value) {
        return callback(new Error('标题不能空'));
      } else if(value.length > 10) {
        return callback(new Error('长度在1-10个字符之间'));
      } else {
        callback();
      }
    };
    return {
      labels: [
          '后端',
          '前端',
          '移动开发',
          '编程语言',
          'Java',
          'Python',
          '人工智能',
          '大数据',
          '数据结构与算法',
          '云原生',
          '云平台',
          '运维',
          '服务器',
          '操作系统',
          '数据库管理',
          'IOS',
          'Android',
          '小程序',
          '硬件开发',
          '区块链'
      ],
      visibleRight: false,
      imgUrl: '',
      isDisplay: false,
      blogForm: {
        headline: '',
        content: '',
        label: [],
        description: '',
      },
      blogRule: {
        headline: [
          {validator: checkBlogHeadline, trigger: 'blur'}
        ],
      },
    }
  },
  created() {
    this.load()
  },
  methods: {
    load() {
      if(this.$route.params.blogId !== '-1') {
        const formData = new FormData()
        formData.append('token', this.$store.state.user.token)
        formData.append('articleId', this.$route.params.blogId)
        axios({
          method: 'post',
          url: 'backend/getEdit',
          data: formData
        }).then(res => {
          if(res.data.errno === 0) {
            this.blogForm.content = res.data.body
            this.blogForm.headline = res.data.title
            this.blogForm.label = res.data.label
            this.blogForm.description = res.data.discription
          } else {
            ElMessage(res.data.msg)
          }
        })
      }
    },
    addLabel(label) {
      this.blogForm.label.push(label)
    },
    handleClose(tag) {
      this.blogForm.label.splice(this.blogForm.label.indexOf(tag), 1)
    },
    addBlogSubmit(formName) {
      this.$refs[formName].validate(valid => {
        if(valid) {
          const formData = new FormData()
          formData.append('token', this.$store.state.user.token)
          formData.append('title', this.blogForm.headline)
          formData.append('body', this.blogForm.content)
          formData.append('label', this.blogForm.label)
          formData.append('discription', this.blogForm.description)
          formData.append('articleId', this.$route.params.blogId)
          axios({
            method: 'post',
            url: 'backend/publish',
            data: formData
          }).then(res => {
            ElMessage(res.data.msg)
            this.blogForm.headline = '';
            this.blogForm.content = '';
            this.visibleRight = false;

            this.$router.push({name: 'view', params: {blogId: res.data.articleId}})
          })
        } else {
          console.log("error submit!!");
        }
      })
    },
    addBlogCancel() {
      this.blogForm.headline = '';
      this.isDisplay = false;
    },
    handleUploadImage(event, insertImage, files) {
      // 拿到 files 之后上传到文件服务器，然后向编辑框中插入对应的内容
      const formData = new FormData()
      formData.append('img', files[0])
      formData.append('token', this.$store.state.user.token)
      axios({
        method: 'post',
        url: 'backend/addImg',
        data: formData,
      }).then(res => {
        insertImage({
          url: res.data.url,
          desc: files[0].name,
        });
      }).catch(err => {
        ElMessage.error('插入失败')
      })
    },

  }
}
</script>

<style scoped>
.el-tag {
  margin-left: 0px;
  margin-right: 8px;
  margin-bottom: 12px;
}
.el-button {
  margin-left: 0px;
  margin-right: 12px;
  margin-bottom: 12px;
}
.labels {
  width: auto;
  height: 50px;
  border: #1f2329 1px;
}
.markdown-editor {
  margin-top: 50px;
}
</style>