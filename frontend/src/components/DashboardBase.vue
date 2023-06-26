<template>
  <div class="main">
    <div class="container h-100 w-100">
      <div class="row justify-content-center align-items-center h-100">
        <div class="col-md-6">
          <Card title="Administração">
            <template #content> Dashboard </template>
          </Card>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import InputField from './inputs/InputField.vue'
import Button from './buttons/Button.vue'
import Card from './Card.vue'
import router from '@/router'

export default {
  components: {
    InputField,
    Button,
    Card
  },
  data() {
    return {}
  },
  methods: {}
}
</script>

<style></style>
