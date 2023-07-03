import axios from 'axios'
import jwt_decode from "jwt-decode";
import { getTokenFromCookie, setTokenInCookie } from '../utils/authUtils.js'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL
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
  try {
    const expired = await checkExpires(); // Aguarda a verificação assíncrona do token expirado
    if (expired) {
      // Token expirado, redirecionar para a página de login
      next('/login');
    } else {
      // Token válido, permitir o acesso à rota
      next();
    }
  } catch (error) {
    // Erro ao decodificar o token, redirecionar para a página de login
    next('/login');
  }
}


// Se o token estiver expirado, regenera o token
export async function checkExpires(to, from, next) {
  const token = getTokenFromCookie();
  if (!token) {
    return true;
  }

  try {

    const decoded = jwt_decode(token);
    const expires = decoded.exp;

    // Token expirou
    if (expires && expires < Date.now() / 1000) {
      try {
        const response = await api.post('/auth/regenerate-token', null, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        const data = response.data;
        setTokenInCookie(data.token);
      } catch (error) {
        return true;
      }
    }

    return false;
  } catch (error) {
    return false;
  }
}

