import axios from 'axios'
import { getTokenFromCookie } from '../utils/authUtils.js'
import { base_url } from '../config.js'

const api = axios.create({
  baseURL: base_url
})

// Verifica se o token é valido e retorna um booleano
export async function checkToken() {
  const token = getTokenFromCookie()

  if (!token) {
    return false
  }

  try {
    const response = await api.post('/auth/validate', null, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    return true
  } catch (error) {
    return false
  }
}

// Guarda de rota para verificar a autenticação
export async function guardCheckAuth(to, from, next) {
  const token = await checkToken()
  if (token) {
    next()
  } else {
    next('/login')
  }
}
