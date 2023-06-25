<template>
  <div class="input-field">
    <input :type="type" :class="className" :value="inputValue" @input="handleInput" />
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  props: {
    className: {
      type: String,
      default: 'input',
    },
    type: {
      type: String,
      default: 'text',
    },
    value: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      inputValue: this.value,
    };
  },
  methods: {
    handleInput(event) {
      this.inputValue = event.target.value;
      this.$emit('update:value', this.inputValue);
    },
  },
};
</script>

<style scoped>
/* Estilos específicos do componente */
.input {
  border: 1px solid #ccc;
  padding: 10px;
  width: 100%;
  border-radius: 4px;
  box-sizing: border-box;
}

.input:focus {
  outline: none;
  border-color: #6c757d;
  box-shadow: 0 0 5px rgba(108, 117, 125, 0.5);
}
</style>
