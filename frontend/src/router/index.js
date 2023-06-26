import { createRouter, createWebHistory } from 'vue-router'
import { guardCheckAuth, checkExpires } from '../guards/jwt'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
      beforeEnter: async (to, from, next) => {
        const expired = await checkExpires(); // Aguarda a verificação assíncrona do token expirado
        if (!expired) {
          next('/dashboard'); // Redireciona para '/dashboard' se o token não estiver expirado
        } else {
          next(); // Continua a navegação normalmente se o token estiver expirado
        }
      }
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
