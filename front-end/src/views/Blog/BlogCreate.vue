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
          <el-input type="text" placeholder="请填写收藏夹的名称" v-model="blogForm.headline" />
        </el-form-item>
      </el-form>
    <template #footer>
      <Button label="No" icon="pi pi-times" class="p-button-text" @click="addBlogCancel"/>
      <Button label="Yes" icon="pi pi-check" autofocus @click="addBlogSubmit('blogForm')"/>
    </template>
  </Dialog>
  <div id="main">
    <MdEditor
        class="markdown-editor"
        v-model="content">
    </MdEditor>
    <Button class="pi pi-arrow-up" label=" 提交" iconPos="right" @click="editFinished"/>
  </div>

</template>

<script>
import Dialog from "primevue/dialog";
import MdEditor from 'md-editor-v3';
import Button from "primevue/button";
import 'md-editor-v3/lib/style.css';
export default {
  name: "BlogCreate",
  components: {
    MdEditor,
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
      content: '',
      blogForm: {
        headline: '',
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
          this.blogForm.headline = '';
          this.isDisplay = false;
        } else {
          console.log("error submit!!");
        }
      })
    },
    addBlogCancel() {
      this.blogForm.headline = '';
      this.isDisplay = false;
    }
  }
}
</script>

<style scoped>
.markdown-editor {
  margin-top: 50px;
}
</style>