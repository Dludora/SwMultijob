<template>
  <el-container style="margin-top: 30px">
    <el-aside class="blog-aside" width="270px">
      <div class="author">
        <el-card class="author-card">
          <template #header>
            <div class="card-header">
              <div class="card-avatar">
                <el-avatar :size="60" :src="blogForm.author.imgSrc" />
              </div>
              <div class="card-message">
                <span>{{blogForm.author.nickName}}</span>
              </div>
            </div>
          </template>
          <el-row :gutter="20" style="margin-bottom: 15px">
            <el-col :span="8" style="text-align: center">1</el-col>
            <el-col :span="8" style="text-align: center">2</el-col>
            <el-col :span="8" style="text-align: center">3</el-col>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="8" style="text-align: center">获赞数</el-col>
            <el-col :span="8" style="text-align: center">收藏数</el-col>
            <el-col :span="8" style="text-align: center">评论数</el-col>
          </el-row>
        </el-card>
      </div>
      <div class="icons">
        <el-row>
          <Avatar size="large" class="avatar-icon" icon="pi pi-thumbs-up" shape="circle"/>
          <!--  <i class="pi pi-heart-fill"></i>-->
        </el-row>
        <el-row>
          <Avatar size="large" class="avatar-icon" icon="pi pi-bookmark" shape="circle"/>
          <!--  <i class="pi pi-heart-fill"></i>-->
        </el-row>
        <el-row>
          <Avatar size="large" class="avatar-icon" icon="pi pi-heart" shape="circle"/>
          <!--  <i class="pi pi-heart-fill"></i>-->
        </el-row>
      </div>
      <el-backtop :right="20" :bottom="100" />
    </el-aside>
    <el-container style="width: 270px;">
      <el-header>
        <p>{{blogForm.headline}}</p>
      </el-header>
      <el-main>
        <div class="blog-view">
          <v-md-preview :text="blogForm.text"></v-md-preview>
        </div>
      </el-main>
      <el-footer>

      </el-footer>
    </el-container>
  </el-container>

</template>

<script>
import Avatar from "primevue/avatar";
import axios from "axios";

export default {
  name: "BlogView",
  components: {
    Avatar,
  },
  data() {
    return {
      blogId: null,
      blogForm: {
        author: {
          nickName: 'Dludora',
          imgSrc: require('../../assets/head.png')
        },
        headline: '题目',
        text: '## 1、前后端项目合并\n' +
            '\n' +
            '### 后端项目\n' +
            '\n' +
            '#### 项目创建/运行\n' +
            '\n' +
            '​\t在前端项目同级命令行中打开终端，输入`django-admin startproject 项目名称`\n' +
            '\n' +
            '​\tcd进该目录，输入 `python manage.py runserver`，运行该项目，终端上出现链接\n' +
            '\n' +
            '#### 配置数据库\n' +
            '\n' +
            '​\t找到第一次创建出的文件夹下，找到`settings.py`文件，找到如下代码\n' +
            '\n' +
            '```python\n' +
            'DATABASES = {\n' +
            '    \'default\': {\n' +
            '        \'ENGINE\': \'django.db.backends.sqlite3\',\n' +
            '        \'NAME\': BASE_DIR / \'db.sqlite3\',\n' +
            '    }\n' +
            '}\n' +
            '```\n' +
            '\n' +
            '​\t如果想要更换为自己的`mysql`数据库，可以参考以下设置进行更改\n' +
            '\n' +
            '```python\n' +
            'DATABASES = {\n' +
            '    \'default\': {\n' +
            '        \'ENGINE\': \'django.db.backends.mysql\',\n' +
            '        \'NAME\': \'xxx\',\t\t\t\t# 数据库名称\n' +
            '        \'USER\': \'root\'\t\t\t\t# 连接数据库的用户名称\n' +
            '        \'PASSWORD\': \'xxxx\'\t\t\t# 用户密码\n' +
            '        \'HOST\': \'127.0.0.1\'\t\t\t # 访问的数据库的主机ip地址\n' +
            '        \'PORT\': \'3306\'\t\t\t\t# 默认mysql访问端口\n' +
            '    }\n' +
            '}\n' +
            '```\n' +
            '\n' +
            '运行 `python manage.py migrate`\n' +
            '\n' +
            '#### 新建应用\n' +
            '\n' +
            '​\t再次在终端上输入`python manage.py startapp xxx`，创建出`xxx`应用\n' +
            '\n' +
            '​\t找到第一次创建出的文件夹下，找到`settings.py`文件，找到如下代码\n' +
            '\n' +
            '```python\n' +
            'INSTALLED_APPS = [\n' +
            '    \'django.contrib.admin\',\n' +
            '    \'django.contrib.auth\',\n' +
            '    \'django.contrib.contenttypes\',\n' +
            '    \'django.contrib.sessions\',\n' +
            '    \'django.contrib.messages\',\n' +
            '    \'django.contrib.staticfiles\',\n' +
            '    \'backend.apps.BackendConfig\',\n' +
            ']\n' +
            '```\n' +
            '\n' +
            '​\t把新建的应用添加进去,修改如下\n' +
            '\n' +
            '```\n' +
            'INSTALLED_APPS = [\n' +
            '    \'django.contrib.admin\',\n' +
            '    \'django.contrib.auth\',\n' +
            '    \'django.contrib.contenttypes\',\n' +
            '    \'django.contrib.sessions\',\n' +
            '    \'django.contrib.messages\',\n' +
            '    \'django.contrib.staticfiles\',\n' +
            '    \'backend.apps.BackendConfig\',\n' +
            '    \'xxx.apps.XxxConfig\',\n' +
            ']\n' +
            '```\n' +
            '\n' +
            '在`models.py`文件中添加好自己想要的内容后，运行`python manage.py makemigrations`, `python manage.py migrate`\n' +
            '\n' +
            '#### 超级管理员\n' +
            '\n' +
            '在终端中，输入`python manage.py createsuperuser`后，按照提示创建超级管理员账号\n' +
            '\n' +
            '在服务端口后加`/admin`，即可进入超级管理员界面，如果想要在该界面管理新建出的xxx应用，则修改改应用目录下的admin.py文件\n' +
            '\n' +
            '`admin.py`文件\n' +
            '\n' +
            '```python\n' +
            'from django.contrib import admin\n' +
            'from .models import Author\n' +
            '# Register your models here.\n' +
            '\n' +
            '\n' +
            'class AuthorAdmin(admin.ModelAdmin):\n' +
            '    list_display = [\'username\', \'password\', \'email\']\n' +
            '\n' +
            '\n' +
            'admin.site.register(Author, AuthorAdmin)\n' +
            '\n' +
            '```\n' +
            '\n' +
            '`models.py`文件\n' +
            '\n' +
            '```python\n' +
            'from django.db import models\n' +
            'class Author(models.Model):\n' +
            '    # Author表项，含用户名和密码，均为字符串属性，并设置最大长度\n' +
            '    username = models.CharField(max_length=50,primary_key=False)\n' +
            '    password = models.CharField(max_length=20)\n' +
            '    email = models.EmailField()\n' +
            '```\n' +
            '\n' +
            '#### 安装def-rest-framework\n' +
            '\n' +
            '##### 终端依次输入指令\n' +
            '\n' +
            '`pip install djangorestframework`\n' +
            '\n' +
            '`pip install markdown`\n' +
            '\n' +
            '`pip install django-filter`\n' +
            '\n' +
            '##### 配置`drf settings.py`文件\n' +
            '\n' +
            '###### 引入app\n' +
            '\n' +
            '```python\n' +
            'INSTALLED_APPS = [\n' +
            '    \'django.contrib.admin\',\n' +
            '    \'django.contrib.auth\',\n' +
            '    \'django.contrib.contenttypes\',\n' +
            '    \'django.contrib.sessions\',\n' +
            '    \'django.contrib.messages\',\n' +
            '    \'django.contrib.staticfiles\',\n' +
            '    \'rest_framework\',\t// 写在所有自定义模块之上\n' +
            '    \'backend.apps.BackendConfig\',\n' +
            ']\n' +
            '```\n' +
            '\n' +
            '###### 引入drf\n' +
            '\n' +
            '放在DATA_BASE以下\n' +
            '\n' +
            '```\n' +
            'REST_FRAMEWORK = {\n' +
            '    \'DEFAULT_PERMISSION_CLASSES\': [\n' +
            '        \'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly\'\n' +
            '    ]\n' +
            '}\n' +
            '```\n' +
            '\n' +
            '#### 实现cors跨域\n' +
            '\n' +
            '命令行输入`pip install django-cors-headers`\n' +
            '\n' +
            '在`settings.py` 中的`INSTALED_APPS`中引入`corsheaders` , `MIDDLEWARE`中的第三位引入`corsheaders.middleware.CorsMiddleware`\n' +
            '\n' +
            '文件最下方加入\n' +
            '\n' +
            '```python\n' +
            'CORS_ORIGIN_WHITELIST = (\n' +
            '    \'http://127.0.0.1:8080\',\n' +
            '    \'http://localhost:8080\',\n' +
            ')\n' +
            'CORS_ALLOW_CREDENTIALS = True  # 指明在跨域访问中，后端是否支持对cookie的操作。\n' +
            '\n' +
            'CORS_ALLOW_METHODS = (\n' +
            ' \'DELETE\',\n' +
            ' \'GET\',\n' +
            ' \'OPTIONS\',\n' +
            ' \'PATCH\',\n' +
            ' \'POST\',\n' +
            ' \'PUT\',\n' +
            ' \'VIEW\',\n' +
            ')\n' +
            'CORS_ALLOW_HEADERS = (\n' +
            ' \'XMLHttpRequest\',\n' +
            ' \'X_FILENAME\',\n' +
            ' \'accept-encoding\',\n' +
            ' \'authorization\',\n' +
            ' \'content-type\',\n' +
            ' \'dnt\',\n' +
            ' \'origin\',\n' +
            ' \'user-agent\',\n' +
            ' \'x-csrftoken\',\n' +
            ' \'x-requested-with\',\n' +
            ' \'Pragma\',\n' +
            ')\n' +
            '```\n' +
            '\n' +
            '![desc](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1269952892,3525182336&fm=26&gp=0.jpg)'
      }
    }
  },
  created() {
    this.load()
  },
  methods: {
    load() {
      this.blogId = this.$route.params.blogId
      console.log(this.blogId)
      const formData = new FormData()
      formData.append('blogId',this.blogId)
      formData.append('token', this.$store.state.user.token)
      // axios({
      //   method: 'post',
      //   url: 'getBlog'
      // }).then(res => {
      //   this.blogForm.text = res.data.blog;
      //   // console.log(res)
      // }).catch(err => {
      //   console.log(err)
      // })
    }
  }
}
</script>

<style scoped>
p {
  font-size: 30px;
  font-weight: bold;
}
.blog-aside {
  border: 1px #1f2329;
  position: relative;
}
.author {
  width: 300px;
  height: 250px;

}
.author-card {
  margin-left: 20px;
  width: 250px;
  margin-bottom: 50px;
  position: fixed;
}

.icons {
  width: 300px;
  position: fixed;
}
.el-row {
  margin-bottom: 20px;
}
.avatar-icon {
  cursor: pointer;
  background-color: #ffffff;
  box-shadow: 0 0 10px 2px rgb(0 0 0 / 6%);
  margin-left: 100px;
}
.blog-view {
  background-color: #ffffff;
}
</style>

