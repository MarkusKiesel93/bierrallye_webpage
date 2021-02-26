<template>
  <v-container fluid>
    <validation-provider
      v-slot="{ errors }"
      name="Vorname"
      rules="required"
    >
      <v-text-field
        label="Vorname"
        v-model="name.firstName"
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
        v-model="name.lastName"
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
    value: {
      type: Object,
      required: true,
    },
    setter: {
      type: Function,
      required: true,
    }
  },
  computed: {
    name: {
      get () {
        return this.value
      },
      set (value) {
        this.setter(this.name)
      }
    }
  }
}
</script>