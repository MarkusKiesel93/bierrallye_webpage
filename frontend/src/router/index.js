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
    path: '/register',
    name: 'RegisterView',
    component: () =>
      import('@/views/RegisterView.vue')
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
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
