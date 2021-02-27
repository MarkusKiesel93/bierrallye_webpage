<template>
  <v-container fluid>
    <validation-provider
      v-slot="{ errors }"
      :name="label"
      rules="required|hash"
    >
      <v-text-field
        :label="label"
        v-model="code"
        :counter="counter"
        :error-messages="errors"
        required
      ></v-text-field>
    </validation-provider>
  </v-container>
  
</template>

<script>
import { ValidationProvider } from 'vee-validate';
import './validation'

export default {
  name: 'InputCode',
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
    label: {
      type: String,
      required: true,
    },
    counter: {
      type: String,
      default: "0",
    }
  },
  computed: {
    code: {
      get () {
        return this.value
      },
      set (value) {
        this.setter(value)
      }
    }
  }
}
</script>