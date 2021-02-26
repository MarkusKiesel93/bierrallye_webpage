<template>
  <validation-observer ref="observer" v-slot="{ invalid }">
    <v-form @submit.prevent="submit">
      <h3> Spieler 1 </h3>
      <InputName
        :value="player1"
        :setter="player1Setter"
      />
      <h3> Spieler 2 </h3>
      <InputName
        :value="player2"
        :setter="player2Setter"
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

setInteractionMode('lazy')

import { mapGetters, mapMutations } from 'vuex'
import InputName from '@/components/InputName'


export default {
  name: 'PlayerForm',
  components: {
    ValidationObserver,
    InputName,
  },
  computed: {
    ...mapGetters({
      player1: 'getPlayer1',
      player2: 'getPlayer2',
    }),
  },
  methods: {
    ...mapMutations({
      player1Setter: 'setPlayer1',
      player2Setter: 'setPlayer2',
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