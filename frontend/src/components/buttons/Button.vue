<template>
  <button :class="buttonClass" @click="handleClick">
    <slot></slot>
  </button>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  props: {
    type: {
      type: String,
      default: 'default'
    }
  },
  setup(props, { emit }) {
    const buttonClass = computed(() => {
      return {
        btn: true,
        'btn-success': props.type === 'success',
        'btn-warning': props.type === 'warning',
        'btn-info': props.type === 'info'
      }
    })

    const handleClick = () => {
      emit('click')
    }

    return {
      buttonClass,
      handleClick
    }
  }
}
</script>

<style scoped>
.btn {
  display: inline-block;
  padding: 10px 20px;
  font-size: 14px;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  border-radius: 4px;
  cursor: pointer;
  border: none;
}

.btn:hover {
  opacity: 0.8;
}

.btn:focus {
  outline: none;
}
.btn-info {
  background-color: #5bc0de;
  color: #ffffff;
}

.btn-warning {
  background-color: #f0ad4e;
  color: #ffffff;
}

.btn-success {
  background-color: #5cb85c;
  color: #ffffff;
}
</style>
