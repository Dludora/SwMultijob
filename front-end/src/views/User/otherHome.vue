<template>
  <div class="container-profile">
    <div class="user-profile-head">
      <div class="user-profile-head-banner"></div>
      <div class="user-profile-head-info">
        <div class="user-profile-head-info-t">
          <div class="user-profile-head-info-l">
            <div class="user-profile-avatar">
              <img :src=formPersonal.imgSrc>
            </div>
          </div>
          <div class="user-profile-head-info-r">
            <div class="user-profile-head-info-r-t">
              <div class="user-profile-head-name">
                <div>昵称</div>
              </div>
            </div>
            <div class="user-profile-head-info-r-c">
              <ul>
                <li>
                  <div class="user-profile-statistics-num">0</div>
                  <div class="user-profile-statistics-name">粉丝</div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <el-main style="min-height: calc(100vh - 80px);">
    <el-card
        :body-style="{padding: '20px'}"
        style="margin-top: 20px; margin-left: 80px; margin-right: 80px"

        v-for="blog in blogs.slice((currentPage-1)*pageSize, currentPage*pageSize)">

      <div class="user-blog-title">{{blog.title}}</div>

    </el-card>
    <div class="pagination-margin">
      <el-pagination
          v-model:currentPage=currentPage
          background
          v-model:page-size=pageSize
          v-model:total=total
          layout="total, prev, pager, next, jumper"
          @current-change="handleCurrentChange"
      />
    </div>


  </el-main>
</template>

<script>
export default {
  name: "otherHome",
  data() {
    return {
      formPersonal: {
        imgSrc: '',
        nickName: '',
        sex: '',
        birthday: '',
        resume: '',
        email: ''
      },
      blogs: [
        {
          id: 1,
          title: 'xxx'
        },
        {
          id: 2,
          title: 'xxx'
        },
        {
          id: 3,
          title: 'xxx'
        },
        {
          id: 4,
          title: 'xxx'
        },
        {
          id: 5,
          title: 'xxx'
        },
        {
          id: 6,
          title: 'xxx'
        },
        {
          id: 7,
          title: 'xxx'
        },
        {
          id: 8,
          title: 'xxx'
        },
      ],
      currentPage: 1,
      total: 20,
      pageSize: 5,
    }
  },
  methods: {
    handleCurrentChange(newSize) {
      this.currentPage = newSize;
    },
  }
}
</script>

<style scoped>
.container-profile {
  width: 100%;
}
.user-profile-head {
  background-repeat: no-repeat;
  background-position: top;
  background-size: 1920px 100px;
}
.user-profile-head .user-profile-head-banner {
  padding-top: 16px;
  margin: auto;
  height: 70px;
  background-repeat: no-repeat;
  background-position: 50%;
  background-size: cover;
}
.user-profile-head .user-profile-head-info {
  padding-left: 70px;
  padding-right: 24px;
  background: white;
  margin: 0 auto;
  border-radius: 2px;
}
.user-profile-head .user-profile-head-info .user-profile-head-info-t {
  display: flex;
  -webkit-box-pack: justify;
  justify-content: space-between;
}
.user-profile-head .user-profile-head-info .user-profile-head-info-l {
  position: relative;
  width: 180px;
  height: 180px;
}
.user-profile-head .user-profile-head-info .user-profile-head-info-l .user-profile-avatar {
  position: absolute;
  top: 0px;
  width: 180px;
  height: 180px;
  border: 4px solid #f0f0f2;
  border-radius: 50%;
  background: white;
}
.user-profile-head .user-profile-head-info .user-profile-head-info-r {
  -webkit-box-flex: 1;
  flex: 1;
  margin-left: 60px;
}
.user-profile-head .user-profile-head-info .user-profile-head-info-r .user-profile-head-info-r-t {
  margin-top: 16px;
}
.user-profile-head .user-profile-head-info .user-profile-head-info-r .user-profile-head-info-r-t .user-profile-head-name {
  color: #222226;
  font-size: 30px;
  font-weight: 500;
  line-height: 34px;
  display: flex;
  word-break: break-all;
  -webkit-box-align: start;
  align-items: flex-start;
}
.user-profile-head .user-profile-head-info .user-profile-head-info-r .user-profile-head-info-r-c {
  margin-top: 50px;
}
.user-profile-head .user-profile-head-info .user-profile-head-info-r .user-profile-head-info-r-c .user-profile-statistics-num {
  color: #222226;
  font-weight: 600;
  font-size: 25px;
  line-height: 28px;
  margin-right: 4px;
}
.user-profile-head .user-profile-head-info .user-profile-head-info-r .user-profile-head-info-r-c .user-profile-statistics-name {
  color: #555666;
  font-size: 20px;
  line-height: 25px;
  margin-right: 2px;
}
.user-blog-title {
  font-size: 35px;
  font-weight: 300;
  margin-left: 80px;
}
.pagination-margin {
  margin-left: 80px;
}
</style>