<template>
  <Dialog
      v-model:visible="isDisplay"
      :style="{width: '400px'}">
     <template #header>
		  <h3 style="font-size: 25px;">新建收藏夹</h3>
     </template>
    <el-form
      :model="addingFavor"
      ref="addingFavor"
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
      <Button label="Yes" icon="pi pi-check" autofocus @click="addSubmit('addingFavor')"/>
    </template>
  </Dialog>
  <el-aside width="200px">
    <el-scrollbar
        height="700px">
      <el-menu
          style="min-height: calc(100vh - 80px);"
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
          <span> {{item.headline}} + {{item.id}}</span>
        </el-menu-item>
      </el-menu>
    </el-scrollbar>
  </el-aside>
  <el-container>
    <el-header class="header" height="100px">
      <el-row>
        {{Favors[0].headline}}
      </el-row>
      <el-row>
        <el-col v-if="unEditing">
          <span >{{Favors[0].describe}}</span>
          <Button label="edit" class="p-button-link p-button-sm" @click="unEditing=false"/>
        </el-col>
        <el-col v-else>
          <el-input style="max-width: 200px" v-model="Favors[0].describe"></el-input>
          <Button label="提交" class="p-button-sm p-button-rounded"
                  style="margin-left:20px"/>
          <Button label="取消" class="p-button-sm p-button-secondary p-button-rounded"
                  style="margin-left:20px"
                  @click="unEditing=true"/>
        </el-col>
      </el-row>
<!--      <Button label="添加" icon="pi pi-plus" class="p-button-secondary" autofocus @click="addFavor"/>-->
    </el-header>
    <el-main>
      <el-card></el-card>
    </el-main>
  </el-container>

</template>

<script>
import Dialog from 'primevue/dialog';
import Button from "primevue/button";
import router from "@/router";
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
      unEditing: true,
      favorsNum: 2,
      Favors: [
        {
          headline: '收藏夹一',
          describe: '一个傻逼的收藏夹',
          id: 0,
        },
        {
          headline: '收藏夹二',
          describe: '一个傻逼的收藏夹',
          id: 1,
        },
      ],
      addingFavor: {
        headline: '',
        describe: '',
      },
      rules: {
        headline: [
          {validator: checkHeadline, trigger: 'blur'}
        ],
        describe: [
          {required: false, message: '请填写描述内容'},
        ],
      },
      collected: [
        {

        },
        {

        },
        {

        },
      ]
    }
  },
  methods: {
    addFavor() {
      this.isDisplay = true;
    },
    addSubmit(formName) {
      this.$refs[formName].validate(valid => {
        if(valid) {
          console.log('success submit!');
          this.Favors.push({
            headline: this.addingFavor.headline,
            describe: this.addingFavor.describe,
            id: this.favorsNum++
          });
          this.addingFavor.describe = '';
          this.addingFavor.headline = '';
          this.isDisplay = false;
        } else {
          console.log("error submit!!");
        }
      })
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