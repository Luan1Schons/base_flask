<template>
  <div class="main">
    <div class="container h-100 w-100">
      <div class="row justify-content-center align-items-center h-100">
        <div class="col-md-6">
          <Card title="Autenticação">
            <template #content>
              <form @submit.prevent="handleForm">
                <div class="form-group mb-3">
                  <label for="email">Email:</label>
                  <InputField
                    label="Email:"
                    :value="email"
                    @update:value="email = $event"
                    type="text"
                    class="form-control"
                    required
                  />
                </div>
                <div class="form-group">
                  <label for="password">Senha:</label>
                  <InputField
                    label="Senha:"
                    @update:value="password = $event"
                    v-model="password"
                    type="password"
                    class="form-control"
                    required
                  />
                </div>
                <div class="row justify-content-end align-items-center w-100">
                  <Button type="success" class="mt-3">Enviar</Button>
                </div>
              </form>
            </template>
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
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    handleForm() {
      const postData = {
        email: this.email,
        password: this.password
      }

      this.$axios
        .post('/auth', postData)
        .then((response) => {
          return router.push('/dashboard')
        })
        .catch((error) => {
          console.log(error)
        })
    }
  }
}
</script>

<style></style>
