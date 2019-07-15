import Vue from 'vue'
import Router from 'vue-router'

import Login from '@/views/Login.vue'
import Home from './views/Home.vue'

import MyNaire from '@/views/content/MyNaire.vue';
import CreateNewNaire from '@/views/content/CreateNewNaire.vue';
import UserManage from '@/views/content/UserManage.vue';
import SystemManage from '@/views/content/SystemManage.vue';

Vue.use(Router)

export default new Router({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    // {
    //   path: '/',
    //   name: 'home',
    //   component: Home
    // },
    {
      path: '/',
      name: 'login',
      component: Login
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      children:[
        {
          path: 'mn',
          name: 'myNaire',
          component: MyNaire
        },
        {
          path: 'cnn',
          name: 'createNewNaire',
          component: CreateNewNaire
        },
        {
          path: 'um',
          name: 'userManage',
          component: UserManage
        },
        {
          path: 'sm',
          name: 'systemManage',
          component: SystemManage
        }
      ]
    },
    // {
    //   path: '/',
    //   name: 'login',
    //   component: Login
    // },
    // {
    //   path: '/',
    //   name: 'login',
    //   component: Login
    // },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (about.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    // }
  ]
})
