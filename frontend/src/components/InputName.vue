<template>
  <v-container fluid>
    <validation-provider
      v-slot="{ errors }"
      name="Vorname"
      rules="required"
    >
      <v-text-field
        label="Vorname"
        v-model="first"
        :counter="20"
        :error-messages="errors"
        required
      ></v-text-field>
    </validation-provider>
    <validation-provider
      v-slot="{ errors }"
      name="Zuname"
      rules="required"
    >
      <v-text-field
        label="Zuname"
        v-model="last"
        :counter="20"
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
  name: 'InputName',
  components: {
    ValidationProvider,
  },
  props: {
    firstName: {
      type: String,
      required: true,
    },
    lastName: {
      type: String,
      required: true,
    },
    firstNameSetter: {
      type: Function,
      required: true,
    },
    lastNameSetter: {
      type: Function,
      required: true,
    }
  },
  computed: {
    first: {
      get () {
        return this.firstName
      },
      set (value) {
        this.firstNameSetter(value)
      }
    },
    last: {
      get () {
        return this.lastName
      },
      set (value) {
        this.lastNameSetter(value)
      }
    },
  }
}
</script>