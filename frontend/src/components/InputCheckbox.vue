<template>
  <v-container fluid>
    <validation-provider
      v-slot="{ errors }"
      :name="fieldName"
      rules="checked"
    >
      <v-checkbox 
        v-model="checkbox"
        :error-messages="errors"
      >
        <template v-slot:label>
          <div v-if="routerTo">
            Ich akzeptiere die
            <router-link :to="routerTo" active-class>
              {{ text }}
            </router-link>
            .
          </div>
          <div v-else>
            Ich akzeptiere die {{ text }}.
          </div>
        </template>
      </v-checkbox>
    </validation-provider>
  </v-container>
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
    routerTo: {
      type: Object,
      default: null
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