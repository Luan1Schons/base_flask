import router from '@/router';
import axios from 'axios';
import { toast } from 'vue3-toastify';
import { getTokenFromLocalStorage, setTokenFromLocalStorage } from '../utils/authUtils.js';

import 'vue3-toastify/dist/index.css';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000',
});

// Interceptor para adicionar o token JWT ao cabeçalho de todas as requisições
// Interceptor para adicionar o token JWT ao cabeçalho de todas as requisições
api.interceptors.request.use(
  config => {
    const token = getTokenFromLocalStorage();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// Interceptor para tratar todas as respostas de erro
api.interceptors.response.use(
  response => {
    const data = response.data.data;
    if (data && data.message) {
      toast.success(data.message);
    }
    if (data && data.token) {
      toast.success('Usuário autenticado com sucesso');
      setTokenFromLocalStorage(data.token, data.expires);
    }
    return response;
  },
  error => {
    if (error.response) {
      const data = error.response.data;
      if (data && data.message) {
        toast.error(data.message);
      }

      if (error.response.status === 401) {
        router.push('/login');
      }
    } else if (error.request) {
      console.log('Erro de solicitação:', error.request);
    } else {
      console.log('Erro:', error.message);
    }

    return Promise.reject(error);
  }
);

export default {
  install(app) {
    app.config.globalProperties.$axios = api;
  },
};
