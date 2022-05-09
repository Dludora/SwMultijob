<template>
  <div class="login-register">
    <div class="contain">
      <div class="big-box" :class="{active:isLogin}">
        <div class="big-contain" v-if="isLogin">
          <div class="btitle">账户登录</div>
          <div class="bform">
            <el-form :model="formSignIn" ref="formSignIn" class="demo-ruleForm form-of-el">
              <el-form-item prop="email">
                <el-input type="email" placeholder="邮箱" v-model="formSignIn.email"></el-input>
              </el-form-item>
              <el-form-item prop="password">
                <el-input type="password" placeholder="密码" v-model="formSignIn.password"></el-input>
              </el-form-item>
            </el-form>
          </div>
          <button class="bbutton" @click="login">登录</button>
        </div>
        <div class="big-contain" v-else>
          <div class="btitle">创建账户</div>
          <div class="bform">
            <el-form :model="formRegister" :rules="rules" ref="formRegister" class="demo-ruleForm form-of-el">
              <el-form-item prop="username">
                <el-input type="text" placeholder="用户名" v-model="formRegister.username"></el-input>
              </el-form-item>
              <el-form-item prop="email">
                <el-input type="email" placeholder="邮箱" v-model="formRegister.email"></el-input>
              </el-form-item>
              <el-form-item prop="pass">
                <el-input type="password" placeholder="密码" v-model="formRegister.pass"></el-input>
              </el-form-item>
              <el-form-item prop="checkPass">
                <el-input type="password" placeholder="确认密码" v-model="formRegister.checkPass"></el-input>
              </el-form-item>
            </el-form>
          </div>
          <button class="bbutton" @click="register">注册</button>
        </div>
      </div>
      <div class="small-box" :class="{active:isLogin}">
        <div class="small-contain" v-if="isLogin">
          <div class="stitle">你好，朋友！</div>
          <p class="scontent">快来开始一段新的旅程吧</p>
          <button class="sbutton" @click="changePage">注册</button>
        </div>
        <div class="small-contain" v-else>
          <div class="stitle">欢迎回来！</div>
          <p class="scontent">继续您的旅程吧</p>
          <button class="sbutton" @click="changePage">登录</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  data(){
    var checkUsername = (rule, value, callback) => {
      const reg=/^[\u4e00-\u9fa5_a-zA-Z0-9]+$/;
      if (!value) {
        return callback(new Error('用户名不能为空'));
      } else if (!reg.test(value)) {
        callback(new Error('用户名由中英文、数字或下划线组成'))
      } else {
        callback();
      }
    };
    var checkEmail = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('邮箱不能为空'));
      } else {
        var reg=/^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
        if (!reg.test(value)) {
          callback(new Error('请输入有效的邮箱'));
        } else {
          callback();
        }
      }
    };
    var validatePass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'));
      } else {
        var reg_pwd=/^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$/;
        if (!reg_pwd.test(value)) {
          callback(new Error('密码至少同时包含字母和数字，且长度为8-18'));
        } else {
          if (this.form.checkPass !== '') {
            this.$refs.ruleForm.validateField('checkPass');
          }
          callback();
        }
      }
    };
    var validatePass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'));
      } else if (value !== this.form.pass) {
        callback(new Error('两次输入密码不一致!'));
      } else {
        callback();
      }
    };
    return {
      isLogin:false,
      emailError:false,
      passwordError:false,
      usernameExist:false,
      formRegister:{
        username:'',
        email:'',
        pass:'',
        checkPass:''
      },
      formSignIn:{
        email:'',
        password:''
      },
      rules: {
        username: [
            { validator: checkUsername, trigger: 'blur' }
        ],
        email: [
          { validator: checkEmail, trigger: 'blur' }
        ],
        pass: [
          { validator: validatePass, trigger: 'blur'}
        ],
        checkPass: [
          { validator: validatePass2, trigger: 'blur'}
        ],
      }
    }
  },
  methods:{
    changePage() {
      this.isLogin = !this.isLogin;
      this.form.userpwd = '';
      this.form.useremail = '';
      this.form.username = '';
    },
    login() {
      const self = this;

    },
    register() {

    }
  }
}
</script>

<style scoped="scoped">
.login-register{
  width: 100vw;
  height: 100vh;
  box-sizing: border-box;
}
.contain{
  width: 60%;
  height: 60%;
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  background-color: #fff;
  border-radius: 20px;
  box-shadow: 0 0 3px #f0f0f0,
  0 0 6px #f0f0f0;
}
.big-box{
  width: 70%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 30%;
  transform: translateX(0%);
  transition: all 1s;
}
.big-contain{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.btitle{
  font-size: 1.5em;
  font-weight: bold;
  color: #66a6ff;
  /*color: rgb(57,167,176);*/
}
.bform{
  width: 100%;
  height: 40%;
  padding: 2em 0;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
.form-of-el{
  width: 50%;
}
.el-input >>> .el-input__inner {
  width: 100%;
  height: 30px;
  border: none;
  outline: none;
  border-radius: 10px;
  padding-left: 2em!important;
  background-color: #f0f0f0;
  color: black;
}

.bform .errTips{
  display: block;
  width: 50%;
  text-align: left;
  color: red;
  font-size: 0.7em;
  margin-left: 1em;
}
.bform input{
  width: 50%;
  height: 30px;
  border: none;
  outline: none;
  border-radius: 10px;
  padding-left: 2em;
  background-color: #f0f0f0;
}
.bbutton{
  width: 20%;
  height: 40px;
  border-radius: 24px;
  border: none;
  outline: none;
  background-color: #66a6ff;
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}
.small-box{
  width: 30%;
  height: 100%;
  /*background: linear-gradient(135deg,rgb(57,167,176),rgb(56,183,145));*/
  background-image: linear-gradient(-225deg, #5D9FFF 0%, #B8DCFF 48%, #6BBBFF 100%);
  position: absolute;
  top: 0;
  left: 0;
  transform: translateX(0%);
  transition: all 1s;
  border-top-left-radius: inherit;
  border-bottom-left-radius: inherit;
}
.small-contain{
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.stitle{
  font-size: 1.5em;
  font-weight: bold;
  color: #fff;
}
.scontent{
  font-size: 0.8em;
  color: #fff;
  text-align: center;
  padding: 2em 4em;
  line-height: 1.7em;
}
.sbutton{
  width: 60%;
  height: 40px;
  border-radius: 24px;
  border: 1px solid #fff;
  outline: none;
  background-color: transparent;
  color: #fff;
  font-size: 0.9em;
  cursor: pointer;
}

.big-box.active{
  left: 0;
  transition: all 0.5s;
}
.small-box.active{
  left: 100%;
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
  border-top-right-radius: inherit;
  border-bottom-right-radius: inherit;
  transform: translateX(-100%);
  transition: all 1s;
}
</style>
