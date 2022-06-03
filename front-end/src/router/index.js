import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const About = () => import('../views/AboutView.vue')
const Login = () => import('../views/LoginView.vue')
const User = () => import('../views/User.vue')
const Editor = () => import('../views/Blog/BlogCreate.vue')
const View = () => import('../views/Blog/BlogView.vue')
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/editor',
    name: 'editor',
    component: Editor
  },
  {
    path: '/view',
    name: 'view',
    component: View
  },
  {
    path: '/user',
    name: 'user',
    component: User,
    children: [
        {
          path: 'profile',
          name: 'profile',
          component: () => import('../views/User/profile.vue')
        },
        {
          path: 'collect',
          name: 'collect',
          component: () => import('../views/User/collection-list.vue'),
          children: [

          ]
        },
        {
          path: 'history',
          name: 'history',
          component: () => import('../views/User/history.vue')
        },
        {
          path: 'concerned',
          name: 'concerned',
          component: () => import('../views/User/concerned.vue')
        },
        {
          path: 'myBlogs',
          name: 'myBlogs',
          component: () => import('../views/User/myBlogs.vue')
        },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
