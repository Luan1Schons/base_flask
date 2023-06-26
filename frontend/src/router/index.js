import { createRouter, createWebHistory } from 'vue-router'
import { guardCheckAuth, checkToken } from '../guards/jwt'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
      beforeEnter: (to, from, next) => {
        const token = checkToken()

        if (token) {
          next('/dashboard')
        } else {
          next()
        }
      }
    },
    {
      path: '/',
      name: 'index',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue'),
      beforeEnter: guardCheckAuth
    }
  ]
})

export default router
