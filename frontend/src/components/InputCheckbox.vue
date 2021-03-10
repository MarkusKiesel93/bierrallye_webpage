<template>
  <validation-provider
    v-slot="{ errors }"
    :name="fieldName"
    rules="checked"
  >
    <v-checkbox 
      v-model="checkbox"
      :error-messages="errors"
      dense
      class="mt-1"
    >
      <template v-slot:label>
        Ich akzeptiere die {{ text }}
      </template>
    </v-checkbox>
  </validation-provider>
</template>

<script>
import { ValidationProvider } from 'vee-validate';
import './validation'

export default {
  name: 'InputCheckbox',
  components: {
    ValidationProvider,
  },
  props: {
    value: {
      type: Boolean,
      default: false,
    },
    setter: {
      type: Function,
      required: true,
    },
    fieldName: {
      type: String,
      required: true,
    },
    text: {
      type: String,
      required: true,
    },
  },
  computed: {
    checkbox: {
      get () {
        return this.value
      },
      set (value) {
        this.setter(value)
      }
    }
  },
}
</script>