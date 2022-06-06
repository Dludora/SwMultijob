<template>
  <Dialog header="上传头像" v-model:visible="display">
    <el-upload
        class="upload-demo"
        drag
        action="https://jsonplaceholder.typicode.com/posts/"
    >
      <el-icon class="el-icon--upload"><upload-filled /></el-icon>
      <div class="el-upload__text">
        将图片拖拽至此 或 <em>点击进行上传</em>
      </div>
      <template>
        <div class="el-upload__tip">
          图片宽度*高度至少为150*150像素，大小不超过2MB
        </div>
      </template>
    </el-upload>
  </Dialog>
  <div class="container-profile">
    <div class="general-info">
      <div class="general-info-avatar" @click="()=>{this.display=true}">
        <img :src=formPersonal.imgSrc>
        <div class="avatar-hover">
          <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAFC0lEQVR4Xu2ba8ilUxTHf39J5H6NQiQSii80bjENNeEDmtw1Jb64jhqF1AwJZcow+EJqmnJLzIeZmkJoxMQXComkjCL3cckk+WvpOdM++33OOc9znufMeY9zVp0v77P22mv991prr7X3fsWUk6bcfmYAzDxgyhGYhcCUO8DOTYK2d6kCuKR/qvC1wTPSELB9CHAVcA5wGLBrRaX/Br4B3gKelfRdxXG12UYGgO3TgQeAvWtr1T3gN+BuSe82lFM6fCQA2D4eeBrYvSWltwPXS/q0JXk7xLQOgO3dwm2Bo1pW9kvgakl/tSl3FAAsA67JlHwKeB4Id65CETZXADdkzOskPVpFQFWeVgGwfXLh+qncjZJWVFUo5bN9H3BB8jcXofDhMPLKxrQGgO2I9+eAI5KJvgcuk1R15bt0tB2e8CJwcPJhK3ClpMgLjakyAIWBC4ATC4X2zGaPLS++pXSrpHeaaGn7TCB3+4+BfGv8AwjA49uWqgANBMD2PsB1wJKaWX29pPubGN8Za/se4OIassI7XgKekfRrv3F9AShi+mHggBqTB+u3wOWSYlUak+3wtheAQ2sK+wm4Q1LPnNETANvh7qtrVG8d3QL9myV9UFPZvuy2TwEer+mFITOqymWStlROgrYjka0D9soG/Qi8CnwBlK1uTPbRqErXorQ+qceihJccA5wPHJjp/TtwraRIoF1U6gG2HwHOzng3AKskhbB5S7Zj0ZYDF2VKbpZ0+0AAbEcmX5sxRjJ5ct5aXaKY7RuL5J1+XSopdokdNMcDbN8W7pLwfF64T7j3xJDt6DwjjI9NlJ5TSZYBEHX8ccmguyRF3E8c2Y588GCi+GeSoj3v6wGvA/smPIsl/dCG9cWqnAvE74SkwosC5hPgzfhJasXbbB8EbEp03yZpUU8AbIdHvJ8Zu6ANhWwvBCK8Dh8A5tdR+Ul6oynoBeD59neqpOgp/qOuECiOrN7LJj6tyRFVIfOWLK9UsS3id00Lc/e1Z2cAkCfVKsZ3eBq1v1UWdKQAFG4fpXROUVOsB+KQI+jootbP9+74FqXsUOEwVgCK+IuGJI35n4EVvTpE22cA9wL7J4hFTlgyTB4aNwDnAQ9lSz+wPS5AeCwbd6ek1+rETvCOG4BohRcnSm+QtLKKEbaDLw2HTZKiJa5F4wbgZeDIROM41a3UIRadX5wqd+grSZfWsn4eeMBmYI9E6UWStlUxwnYUYlGQdehPSXlzNlDUuD1g6gGY+hCY+iQ49dtg9OPTWwgVhUh0gNNZCnf2qJITpoHbV8Iw2c1QUo5ObzuceMI4DkTiSc54zwNSfx/Dkdj8AqBO8LfBO9ZSuA0DmsqoDUCRtN7O7t8WDnu/39SApuOL9wXpadJ2SWelcsvuBV7JHjlUbmObKtz2+JK2equkSwYBkNfwQz9xaduguvJsx/Hahcm4OQcrZR5QVsPH9XKExsSQ7XD1uN5Pac7RWhkAZTX8L8DKSQGhMD6O1fZLrC89XO11PR5XV6tKlnsjEDmi1/uAcXpI531AxHjq9h2dlkuKq7cu6vdCJMrXpeO0qMW510paUyavHwBRRd30PwAh3jo80euKrcorsQiHeP056FKzxQVrRVTE/Ooyt++7DZZNndXwnXeCbT2EbsVaIB5ndd4JVr5mH+gBvbSr+s8PbVk3SM6wt8hDAzBIoUn5PgNgUlZqVHrOPGBUyE6K3JkHTMpKjUrPfwGerYtf3LH0qAAAAABJRU5ErkJggg==">
        </div>
      </div>
      <div class="general-info-name">
        <span>{{formPersonal.nickName}}</span>
      </div>
    </div>
    <div class="base-info">
      <div class="base-info-head">个人信息</div>
      <div class="base-info-content">
        <div class="base-info-content-show">
          <el-form
              :model="formEdit"
              label-width="120px">
            <el-form-item label="昵称: ">
              <el-col v-if="unEditing[0]">
                <span>{{formPersonal.nickName}}</span>
                <Button label="edit" class="p-button-link p-button-sm"
                        @click="()=>{unEditing[0]=false}"/>
              </el-col>
              <el-col v-else>
                <el-input v-model="formEdit.nickName"
                        style="max-width: 300px"/>
                <Button label="提交" class="p-button-sm p-button-rounded"
                        style="margin-left:20px"
                        @click="submitSex"/>
                <Button label="取消" class="p-button-sm p-button-secondary p-button-rounded"
                        style="margin-left:20px"
                        @click="()=>{unEditing[0]=true;
                                    formEdit.nickName=formPersonal.nickName}"/>
              </el-col>
            </el-form-item>
            <el-form-item label="邮箱: ">
              <el-col v-if="unEditing[1]">
                <span>{{formEdit.email}}</span>
                <Button label="edit" class="p-button-link p-button-sm"
                        @click="()=>{this.unEditing[1]=false}"/>
              </el-col>
              <el-col v-else>
                <el-input v-model="formPersonal.email"
                        style="max-width: 300px"/>
                <Button label="提交" class="p-button-sm p-button-rounded"
                        style="margin-left:20px"
                        @click="submitSex"/>
                <Button label="取消" class="p-button-sm p-button-secondary p-button-rounded"
                        style="margin-left:20px"
                        @click="()=>{this.unEditing[1]=true;
                                     this.formEdit.email = this.formPersonal.email;}"/>
              </el-col>
            </el-form-item>
            <el-form-item label="性别: ">
              <el-col v-if="unEditing[2]">
                <span >{{formPersonal.sex}}</span>
                <Button
                  label="edit" class="p-button-link p-button-sm"
                  @click="()=>this.unEditing[2]=false"/>
              </el-col>
              <el-col v-else>
                <el-radio-group
                    v-model="formEdit.sex">
                  <el-radio label="男">男</el-radio>
                  <el-radio label="女">女</el-radio>
                  <el-radio label="未知">未知</el-radio>
                </el-radio-group>
                <Button label="提交" class="p-button-sm p-button-rounded"
                        style="margin-left:20px"
                        @click="submitSex"/>
                <Button label="取消" class="p-button-sm p-button-secondary p-button-rounded"
                        style="margin-left:20px"
                        @click="()=>{this.unEditing[2]=true;
                                      this.formEdit.sex = this.formPersonal.sex;}"/>
              </el-col>
            </el-form-item>
            <el-form-item label="出生日期: ">
              <el-col v-if="unEditing[4]">
                {{formPersonal.birthday}}
                  <Button label="edit" class="p-button-link p-button-sm"
                          @click="()=>{this.unEditing[4]=false}"/>
                </el-col>
              <el-col v-else>
                <el-date-picker v-model="formEdit.birthday"
                              type="date"
                              placeholder="选择出生日期"/>
                  <Button label="提交" class="p-button-sm p-button-rounded"
                          style="margin-left:20px"
                          @click="submitSex"/>
                  <Button label="取消" class="p-button-sm p-button-secondary p-button-rounded"
                          style="margin-left:20px"
                          @click="()=>{this.unEditing[4]=true;
                                      formEdit.birthday=formPersonal.birthday;}"/>
                </el-col>
            </el-form-item>
            <el-form-item label="个人简介: ">
              <el-input
                  v-model="formEdit.resume"
                  :autosize="{ minRows: 2, maxRows: 4 }"
                  style="max-width: 400px"
                  type="textarea"
                  placeholder="Please input"
                  :disabled=unEditing[5]
              />
              <div v-if="unEditing[5]">
                <Button label="edit" class="p-button-link p-button-sm"
                        @click="()=>{this.unEditing[5]=false}"/>
              </div>
              <div v-else>
                <Button label="提交" class="p-button-sm p-button-rounded"
                        style="margin-left:20px"
                        @click="submitSex"/>
                <Button label="取消" class="p-button-sm p-button-secondary p-button-rounded"
                        style="margin-left:20px"
                        @click="()=>{this.unEditing[5]=true;
                                    formEdit.resume=formPersonal.resume}"/>
              </div>
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {Hide} from "@element-plus/icons-vue";
import { UploadFilled } from '@element-plus/icons-vue'
import Button from 'primevue/button';
import Dialog from 'primevue/dialog'
export default {
  name: "profile",
  components: {
    Hide,
    Button,
    Dialog,
    UploadFilled,
  },
  data() {
    return {
      display: false,
      formPersonal: {
        imgSrc: '',
        nickName: '',
        sex: '',
        birthday: '',
        resume: '',
        email: ''
      },
      formEdit: {
        imgSrc: '',
        nickName: '',
        sex: '',
        birthday: '',
        resume: '',
        email: ''
      },
      unEditing: [true, true, true, true, true, true],
    }
  },
  methods: {

  },
  created() {
    console.log('登录信息');
    this.formPersonal = {
      imgSrc: require('../../assets/head.png'),
      nickName: '和影子玩拳击的男人',
      sex: '男',
      birthday: '2022-05-01',
      resume: '一个煞笔',
      email: 'koushurui@outlook.com'
    };
    this.formEdit = {
      imgSrc: require('../../assets/head.png'),
      nickName: '和影子玩拳击的男人',
      sex: '男',
      birthday: '2022-05-01',
      resume: '一个煞笔',
      email: 'koushurui@outlook.com'
    };
  }
}
</script>

<style scoped>
.container-profile {
  width: 100%;
}
.general-info {
  display: flex;
  width: 1200px;
  height: 160px;
  margin: 10px 0;
  padding: 24px 24px 40px;
  background-color: #ffffff;
}
.hide {
  /*display: none;*/
}
.general-info-avatar {
  flex-shrink: 0;
  position: relative;
  width: 96px;
  height: 96px;
  margin-right: 16px;
  box-shadow: 0 0 10px 2px rgb(0 0 0 / 6%);
  border: 2px solid #fff;
  border-radius: 50%;
  cursor: pointer;
}
.general-info-avatar img{
  width: 92px;
  height: 92px;
  border-radius: 50%;
}
.avatar-hover {
  display: none;
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,.5);
  -webkit-box-pack: center;
  -ms-flex-pack: center;
  justify-content: center;
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  border-radius: 50%;
}
.avatar-hover img {
  display: block;
  border-radius: 50%;
  width: 32px;
  height: 32px;
}
.general-info-avatar:hover .avatar-hover{
  display: flex;
}


.general-info-name {
  padding: 24px;
}
.general-info-name span {
  font-weight: 900;
  font-size: 30px;
  line-height: 48px;
}

.base-info {
  width: 1200px;
  height: 48px;
  background-color: #ffffff;
}
.base-info-head {
  box-sizing: border-box;
  line-height: 48px;
  padding-left: 16px;
  font-size: 18px;
  font-weight: 600;
  color: #2e2e2e;
  border-bottom: 1px solid #f0f0f2;
}
.base-info-content {
  width: 100%;
  padding: 16px;
}
.base-info-content-show {
  width: 1168px;
  padding: 16px 58px 16px 0;
}

.el-form-item {
  width: 700px;
  height: 35px;
}
.el-form-item label {
  line-height: 35px;
}
.el-form-item span {
  line-height: 35px;
}
.el-form-item:hover .p-button-link{
  display: inline-block;
}
.p-button-link {
  display: none;
}
</style>