<template>
  <v-container fluid>
    <validation-provider
      v-slot="{ errors }"
      name="Telefonnummer"
      rules="required|phoneNumber"
    >
      <v-text-field
        label="Telefonnummer mit Ländervorwahl"
        v-model="phoneNumber"
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
  name: 'InputPhoneNumber',
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
    phoneNumber: {
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
