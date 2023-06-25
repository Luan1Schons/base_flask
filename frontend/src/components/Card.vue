<template>
    <div class="card">
      <div class="card-header">
        <h2>{{ title }}</h2>
      </div>
      <div class="card-body">
        <slot name="content"></slot>
      </div>
      <div class="card-footer">
        {{ footer }}
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    props: {
      title: {
        type: String,
        required: true,
      },
      footer: {
        type: String,
        required: false,
      },
    },
  };
  </script>
  
  <style>
  .card {
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    border-radius: 4px;
    background-color: #fff;
  }
  
  .card-header {
    background-color: #f7f7f7;
    border-bottom: 1px solid #ddd;
    padding: 8px 16px;
    font-weight: bold;
    color: rgb(15, 15, 15);
  }
  
  .card-body {
    padding: 16px;
  }
  
  .card-footer {
    border-top: 1px solid #ddd;
    padding: 8px 16px;
  }
  </style>
  