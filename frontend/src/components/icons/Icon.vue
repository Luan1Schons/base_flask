<template>
    <span :class="['icon', `icon-${name}`]"></span>
  </template>
  
  <script>
  export default {
    name: 'Icon',
    props: {
      name: {
        type: String,
        required: true
      }
    }
  }
  </script>
  
  <style scoped>
  .icon {
    display: inline-block;
    width: 24px;
    height: 24px;
    background-size: contain;
    background-repeat: no-repeat;
  }
  </style>
  