import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView,
  },
  {
    path: '/legal-notice',
    name: 'LegalNoticeView',
    component: () => import('@/views/LegalNoticeView.vue'),
  },
  {
    path: '/register',
    name: 'RegisterView',
    component: () => import('@/views/RegisterView.vue'),
  },
  {
    path: '/register/success',
    name: 'RegisterViewSuccess',
    component: () => import('@/views/RegisterViewSuccess.vue'),
  },
  {
    path: '/deregister',
    name: 'DeregisterView',
    component: () => import('@/views/DeregisterView.vue'),
  },
  {
    path: '/deregister/:channel/:contact/:hash',
    name: 'DeregisterViewFromLink',
    component: () => import('@/views/DeregisterView.vue'),
  },
  {
    path: '/deregister/success',
    name: 'DeregisterViewSuccess',
    component: () => import('@/views/DeregisterViewSuccess.vue'),
  },
  {
    path: '*',
    name: 'PageErrorView',
    component: () => import('@/views/PageErrorView.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router
