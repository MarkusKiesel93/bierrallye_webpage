<template>
  <validation-observer ref="observer" v-slot="{ invalid }">
    <v-form @submit.prevent="submit">
      <InputEmail
        :value="email"
        :setter="emailSetter"
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
import {
  ValidationObserver,
  setInteractionMode,
} from 'vee-validate';
import './validation'

import { mapState, mapMutations } from 'vuex'
import InputEmail from '@/components/InputEmail'

setInteractionMode('lazy');


export default {
  name: 'ContactForm',
  components: {
    ValidationObserver,
    InputEmail,
  },
  computed: {
    ...mapState({
      email: (state) => state.team.email
    }),
  },
  methods: {
    ...mapMutations({
      emailSetter: 'setTeamValues'
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
};
</script>