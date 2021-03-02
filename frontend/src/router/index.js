import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/legal-notice',
    name: 'LegalNoticeView',
    component: () =>
      import('@/views/LegalNoticeView.vue')
  },
  {
    path: '/data-privacy',
    name: 'DataProtectionView',
    component: () =>
      import('@/views/DataProtectionView.vue')
  },
  {
    path: '/register',
    name: 'RegisterView',
    component: () =>
      import('@/views/RegisterView.vue')
  },
  {
    path: '/register/success',
    name: 'RegisterSuccessView',
    component: () =>
      import('@/views/RegisterSuccessView.vue')
  },
  {
    path: '/verify/:email/:hash',
    name: 'VerificationView',
    component: () =>
      import('@/views/VerificationView.vue')
  },
  {
    path: '/deregister',
    name: 'DeregisterView',
    component: () =>
      import('@/views/DeregisterView.vue')
  },
  {
    path: '/deregister/:email/:hash',
    name: 'DeregisterViewFromLink',
    component: () =>
      import('@/views/DeregisterView.vue')
  },
  {
    path: '/deregister/success',
    name: 'DeregisterSuccessView',
    component: () =>
      import('@/views/DeregisterSuccessView.vue')
  },
  {
    path: '*',
    name: 'PageErrorView',
    component: () => 
      import('@/views/PageErrorView.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
