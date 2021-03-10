<template>
  <v-container fluid>
    <validation-provider
      v-slot="{ errors }"
      name="E-Mail"
      rules="required|email"
    >
      <v-text-field
        label="E-Mail"
        v-model="email"
        :counter="100"
        :error-messages="errors"
        required
      ></v-text-field>
    </validation-provider>
  </v-container>
</template>

<script>
import { ValidationProvider } from 'vee-validate'
import './validation'

export default {
  name: 'InputEmail',
  components: {
    ValidationProvider,
  },
  props: {
    value: {
      type: String,
      required: true,
    },
    setter: {
      type: Function,
      required: true,
    },
  },
  computed: {
    email: {
      get() {
        return this.value
      },
      set(value) {
        this.setter(value)
      },
    },
  },
}
</script>
