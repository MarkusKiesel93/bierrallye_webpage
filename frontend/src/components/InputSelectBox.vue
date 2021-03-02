<template>
  <v-container fluid>
    <validation-provider
      v-slot="{ errors }"
      :name="label"
      rules="required"
    >
      <v-select
        v-model="selected"
        :items="items"
        :label="label"
        :error-messages="errors"
      ></v-select>
    </validation-provider>
  </v-container>
</template>

<script>
import { ValidationProvider } from 'vee-validate';
import './validation'

export default {
  name: 'InputSelectBox',
  components: {
    ValidationProvider,
  },
  props: {
    value: {
      type: String,
      default: null
    },
    label: {
      type: String,
      required: true,
    },
    items: {
      type: Array,
      required: true,
    },
    setter: {
      type: Function,
      required: true,
    },
  },
  computed: {
    selected: {
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