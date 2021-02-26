<template>
  <validation-observer ref="observer" v-slot="{ invalid }">
    <v-form @submit.prevent="submit">
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
      <validation-provider
        v-slot="{ errors }"
        name="Stornocode"
        rules="required|hash"
      >
        <v-text-field
          label="Stornocode"
          v-model="hash"
          :counter="6"
          :error-messages="errors"
          required
        ></v-text-field>
      </validation-provider>
      <v-btn
        color="primary"
        class="mr-4 mt-4"
        :disabled="invalid"
        @click="submit"
      >
        Weiter
      </v-btn>
      <v-btn
        class="mt-4"
        @click="cancel"
      >
        Zurück
      </v-btn>
    </v-form>
  </validation-observer>
</template>

<script>
// todo: add information for Stornocode and where to find it
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from 'vee-validate';
import { required, email } from 'vee-validate/dist/rules';

setInteractionMode('lazy');

extend('required', {
  ...required,
  message: '{_field_} ist erforderlich!',
})

extend('email', {
  ...email,
  message: 'Gültige E-Mail Adresse angeben!',
})

extend('hash', {
  validate: value => {
    let upperLettersDigits = true
    return value.length === 6 && upperLettersDigits
  },
  message: 'Stornocode besteht genau aus 6 Zeichen (Ziffern und Buchstaben)!',
});

export default {
  name: "DeregistrationForm",
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  computed: {
    email: {
      get () {
        return this.$store.state.deregisterEmail
      },
      set (value) {
        this.$store.commit('setDeregisterEmail',  value)
      }
    },
    hash: {
      get () {
        return this.$store.state.deregisterHash
      },
      set (value) {
        this.$store.commit('setDeregisterHash', value.toUpperCase())
      }
    },
  },
  methods: {
    submit() {
      this.$refs.observer.validate();
      this.$emit('next-step');
    },
    cancel() {
      this.$refs.observer.reset()
      this.$emit('last-step');
    },
  },
}
</script>