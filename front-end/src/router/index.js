import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from "@/store";

const About = () => import('../views/AboutView.vue')
const Login = () => import('../views/LoginView.vue')
const User = () => import('../views/User.vue')
const Editor = () => import('../views/Blog/BlogCreate.vue')
const View = () => import('../views/Blog/BlogView.vue')
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      isLogin: false,
    }
  },
  {
    path: '/about',
    name: 'about',
    component: About,
    meta: {
      isLogin: false,
    }
  },
  {
    path: '/login',
    name: 'login',
    component: Login,
    meta: {
      isLogin: false,
    }
  },
  {
    path: '/editor',
    name: 'editor',
    component: Editor,
    meta: {
      isLogin: true,
    }
  },
  {
    path: '/view:blogId',
    name: 'view',
    component: View,
  },
  {
    path: '/user',
    name: 'user',
    component: User,
    children: [
        {
          path: 'profile',
          name: 'profile',
          component: () => import('../views/User/profile.vue'),
          meta: {
            isLogin: true,
          }
        },
        {
          path: 'collect',
          name: 'collect',
          component: () => import('../views/User/collection-list.vue'),
          children: [

          ],
          meta: {
            isLogin: true,
          },
        },
        {
          path: 'history',
          name: 'history',
          component: () => import('../views/User/history.vue'),
          meta: {
            isLogin: true,
          },
        },
        {
          path: 'concerned',
          name: 'concerned',
          component: () => import('../views/User/concerned.vue'),
          meta: {
            isLogin: true,
          }
        },
        {
          path: 'myBlogs',
          name: 'myBlogs',
          component: () => import('../views/User/myBlogs.vue'),
          meta: {
            isLogin: true,
          }
        },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
