<template>
  <Dialog
      v-model:visible="isDisplay"
      :style="{width: '400px'}">
      <template #header>
        <h3 style="font-size: 25px;">上传博客</h3>
      </template>
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
      </el-form>
    <template #footer>
      <Button label="No" icon="pi pi-times" class="p-button-text" @click="addBlogCancel"/>
      <Button label="Yes" icon="pi pi-check" autofocus @click="addBlogSubmit('blogForm')"/>
    </template>
  </Dialog>
  <div id="main">
    <v-md-editor
        :disabled-menus="[]"
        v-model="blogForm.content"
        height="600px"
        @upload-image="handleUploadImage"
    ></v-md-editor>

    <Button class="pi pi-arrow-up" label=" 提交" iconPos="right" @click="editFinished"/>
  </div>

</template>

<script>
import Dialog from "primevue/dialog";
import Button from "primevue/button";
export default {
  name: "BlogCreate",
  components: {
    Dialog,
    Button
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
      isDisplay: false,
      blogForm: {
        headline: '',
        content: '',
      },
      blogRule: {
        headline: [
          {validator: checkBlogHeadline, trigger: 'blur'}
        ],
      },
    }
  },
  methods: {
    editFinished() {
      this.isDisplay = true;
    },
    addBlogSubmit(formName) {
      this.$refs[formName].validate(valid => {
        if(valid) {
          console.log('success submit!');
          console.log(this.blogForm.content);
          this.blogForm.headline = '';
          this.blogForm.content = '';
          this.isDisplay = false;
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
      console.log(files);

      // 此处只做示例
      insertImage({
        url:
          'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1269952892,3525182336&fm=26&gp=0.jpg',
        desc: '七龙珠',
        // width: 'auto',
        // height: 'auto',
      });
    },
  }
}
</script>

<style scoped>
.markdown-editor {
  margin-top: 50px;
}
</style>