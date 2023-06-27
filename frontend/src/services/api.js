import axios from 'axios';
import { router } from '@/router';
import { base_url } from '../config.js';
import { setTokenInCookie, getTokenFromCookie } from '../utils/authUtils.js';

const api = axios.create({
  baseURL: base_url
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
