<template>
  <validation-observer ref="observer" v-slot="{ invalid }">
    <v-form @submit.prevent="submit">
      <InputEmail
        :value="email"
        :setter="emailSetter"
      />
      <InputCode
        :value="hash"
        :setter="hashSetter"
        label="Stornocode"
        counter="6"
      />
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
  ValidationObserver,
  setInteractionMode,
} from 'vee-validate';
import './validation'

import { mapState, mapMutations } from 'vuex'
import InputEmail from '@/components/InputEmail'
import InputCode from '@/components/InputCode'

setInteractionMode('lazy');

export default {
  name: "DeregistrationForm",
  components: {
    ValidationObserver,
    InputEmail,
    InputCode,
  },
  computed: {
    ...mapState({
      email: (state) => state.team.email,
      hash: (state) => state.deregisterHash,
    }),
  },
  methods: {
    ...mapMutations({
      emailSetter: 'setDeregisterEmail',
      hashSetter: 'setDeregisterHash',
    }),
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