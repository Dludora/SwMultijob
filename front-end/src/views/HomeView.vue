<template>
<div class="main">
  <div class="home-wrap">
    <div class="user-recommend">推荐</div>
    <div class="floor-blog-index">
      <div class="blog-content">
        <ul v-infinite-scroll="load" class="infinite-list" style="overflow: auto">
          <li v-for="i in userRecommendedBlogs" :key="i" class="infinite-list-item">
            <div >
              <div class="blog-tag">
                <a target="_blank" :href="i.blogSrc">
                  {{i.blogTitle}}
                </a>
              </div>
                <div class="blog-show">
                  <div class="blog-brief">
                    {{i.blogBrief}}
                  </div>
                </div>

            </div>
          </li>
        </ul>
      </div>
      <div class="blog-hot">

      </div>
    </div>
  </div>
</div>

</template>

<script>
import {ref} from 'vue';

export default {
  name: 'HomeView',
  components: {
    ref,
  },
  data() {
    return {
      userRecommendedBlogs: [
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
        {
          blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
          blogTitle: '标题',
          blogBrief: '简介啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        },
      ]
    }
  },
  methods: {
    load () {
      this.userRecommendedBlogs.push({blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
      blogTitle: 'hh', blogBrief: 'sssssssss'});
      this.userRecommendedBlogs.push({blogSrc: 'https://blog.csdn.net/m0_59140023/article/details/124871328?spm=1001.2100.3001.7377&utm_medium=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase&depth_1-utm_source=distribute.pc_feed_blog_category.none-task-blog-classify_tag-2-124871328-null-null.nonecase',
        blogTitle: 'hh', blogBrief: 'sssssssss'});
    }
  }
}
</script>

<style scoped>
.main {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.home-wrap {
  width: 1380px;
  margin: 0 auto;
  padding: 16px;
  -webkit-font-smoothing: antialiased;
}
.user-recommend {
  font-size: 40px;
  font-weight: 500;
  line-height: 50px;
}
.floor-blog-index {
  display: flex;
  -webkit-box-pack: justify;
  justify-content: space-between;
  margin-top: 14px;
}
.floor-blog-index .blog-content {
  width: 990px;
}
.floor-blog-index .blog-hot {
  width: 338px;
}
.infinite-list {
  height: 800px;
  padding: 0;
  margin: 0;
  list-style: none;
}
.infinite-list .infinite-list-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 180px;
  background: white;
  margin: 20px;
  border-radius: 20px;
}
.infinite-list .infinite-list-item + .list-item {
  margin-top: 10px;
}
.blog-tag {
  font-size: 25px;
  font-weight: 500;
  color: #222226;
  overflow: hidden;
  white-space: normal;
  word-break: break-word;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  line-height: 30px;
  width: 800px;
}
.blog-show {
  padding-bottom: 15px;
  border-bottom: 1px solid #f0f0f2;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: reverse;
  flex-flow: row-reverse;
}
.blog-img-wrap {
  margin-right: 16px;
  display: flex;
  -webkit-box-align: start;
  align-items: flex-start;
  padding-top: 2px;
}
.blog-img {
  position: relative;
  border-radius: 2px;
  width: 134px;
  height: 84px;
  display: inline-block;
  border: 1px solid #f5f6f7;
  background: #f5f6f7 50%;
}
.blog-brief-wrap {

}
.blog-brief {
  overflow: hidden;
  font-size: 15px;
  font-weight: 400;
  -webkit-box-flex: 1;
  flex: 1;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -webkit-box-pack: justify;
  justify-content: space-between;
  height: 100px;
  background-color: #f5f6f7;
  border-radius: 10px;
  margin-top: 10px;
  width: 650px;
  line-height: 20px;
}
a {
  text-decoration: none;
  color: #222226;
}

a:link {
  text-decoration: none;
}
/*去除已经被访问过的a标签的下划线*/
a:visited {
  text-decoration: none;
}
/*去除鼠标悬停时的a标签的下划线*/
a:hover {
  text-decoration: none;
}
/*去除正在点击的a标签的下划线（鼠标按下，尚未松开）*/
a:active {
  text-decoration: none;
}
/*去除获得焦点的a标签的下划线（被鼠标点击过）*/
a:focus {
  text-decoration: none;
}
</style>
