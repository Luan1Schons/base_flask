import axios from 'axios';
import { setTokenInCookie, getTokenFromCookie } from '../utils/authUtils.js';
import router  from '@/router';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL
});

api.interceptors.request.use(
  (config) => {
    const token = getTokenFromCookie();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

api.interceptors.response.use(
  (response) => {
    const data = response.data.data;
    if (data && data.token) {
      setTokenInCookie(data.token);
    }
    return response;
  },
  (error) => {
    if (error.response) {
      const data = error.response.data;
      // Faça alguma coisa com a mensagem de erro
      if (error.response.status === 401) {
        router.push('/login');
      }
    } else if (error.request) {
      console.error('Erro de solicitação:', error.request);
    } else {
      console.error('Erro:', error.message);
    }

    return Promise.reject(error);
  }
);

export default {
  install(app) {
    app.config.globalProperties.$axios = api;
  }
};
