<template>
  <Dialog
      v-model:visible="isDisplay"
      :style="{width: '400px'}">
     <template #header>
		  <h3 style="font-size: 25px;">新建收藏夹</h3>
     </template>
    <el-form
      :model="addingFavor"
      :rules="rules"
      label-width="50px"
      label-position="top"
      style="max-width: 300px">
      <el-form-item prop="headline" label="标题">
        <el-input type="text" placeholder="请填写收藏夹的名称" v-model="addingFavor.headline"></el-input>
      </el-form-item>
      <el-form-item prop="describe" label="描述(选填)">
        <el-input
            type="textarea"
            v-model="addingFavor.describe"
            :autosize="{ minRows: 2, maxRows: 4 }"
        />
      </el-form-item>
    </el-form>
    <template #footer>
      <Button label="No" icon="pi pi-times" class="p-button-text" @click="addCancel"/>
      <Button label="Yes" icon="pi pi-check" autofocus @click="addSuccess"/>
    </template>
  </Dialog>

  <el-col :span="10">
    <Button label="添加" icon="pi pi-plus" class="p-button-secondary" autofocus @click="addFavor"/>
    <el-menu
        style="width: 200px; min-height: calc(100vh - 80px); margin-left: -21px"
        active-text-color="#ffd04b"
        background-color="#545c64"
        class="el-menu-vertical-demo"
        default-active="2"
        text-color="#fff"
        router
    >
      <div style="height: 20px"></div>
      <el-menu-item v-for="item in Favors" :index="item.to">
        <i class="pi pi-folder"></i>
        <span> {{item.headline}}</span>
      </el-menu-item>
    </el-menu>
  </el-col>
</template>

<script>
import Dialog from 'primevue/dialog';
import Button from "primevue/button";
export default {
  name: "collect",
  components: {
    Dialog,
    Button,
  },
  data() {
    let checkHeadline = (rule, value, callback) => {
      if(!value) {
        return callback(new Error('标题不能空'));
      } else if(value.length > 10) {
        return callback(new Error('长度在1-10个字符之间'));
      } else {
        callback();
      }
    };
    let checkDescribe = (rule, value, callback) => {
      callback();
    }
    return {
      isDisplay: false,
      Favors: [
        {
          headline: '收藏夹一',
          describe: '一个傻逼的收藏夹',

        },
        {
          headline: '收藏夹二',
          describe: '一个傻逼的收藏夹',
        },
      ],
      addingFavor: {
        headline: '',
        describe: '',
      },
      rules: {
        headline: [
          {required: true, message: '必填项'},
          {min: 1, max: 10, message: '长度在1到10个字符'}
        ],
        describe: [
          {required: false, message: '请填写描述内容'},
        ],
      },
    }
  },
  methods: {
    addFavor() {
      this.isDisplay = true;
    },
    addSuccess() {
      this.Favors.push({
        headline: this.addingFavor.headline,
        describe: this.addingFavor.describe
      });
      this.addingFavor.describe = '';
      this.addingFavor.headline = '';
      this.isDisplay = false;
    },
    addCancel() {
      this.addingFavor.describe = '';
      this.addingFavor.headline = '';
      this.isDisplay = false;
    },
  },

}
</script>

<style scoped>

</style>