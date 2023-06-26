import router from '@/router'
import axios from 'axios'
import { base_url } from '../config.js'
import { toast } from 'vue3-toastify'
import { setTokenInCookie, getTokenFromCookie } from '../utils/authUtils.js'

import 'vue3-toastify/dist/index.css'

const api = axios.create({
  baseURL: base_url
})

// Interceptor para adicionar o token JWT ao cabeçalho de todas as requisições
// Não é necessário enviar o token dessa forma em todas as requisições por conta do token estar em cookie,
// mas por motivos de personalização e flexibilidade sobre os interceptors do axios, realizei dessa forma.
api.interceptors.request.use(
  (config) => {
    const token = getTokenFromCookie()
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// Interceptor para tratar todas as respostas de erro
api.interceptors.response.use(
  (response) => {
    const data = response.data.data
    if (typeof data.message !== 'undefined') {
      toast.success(data.message)
    }
    if (typeof data.token !== 'undefined') {
      toast.success('Usuário autenticado com sucesso')
      // Set the JWT in a secure HttpOnly cookie
      console.log(data.token)
      setTokenInCookie(data.token, data.expires)

      console.log(getTokenFromCookie())
    }
    return response
  },
  (error) => {
    if (error.response) {
      const data = error.response.data
      toast.error(data.message)

      if (error.response.status === 401) {
        router.push('/login')
      }
    } else if (error.request) {
      console.log('Erro de solicitação:', error.request)
    } else {
      console.log('Erro:', error.message)
    }

    return Promise.reject(error)
  }
)

export default {
  install(app) {
    app.config.globalProperties.$axios = api
  }
}
