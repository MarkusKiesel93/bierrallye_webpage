<template>
  <validation-observer ref="observer" v-slot="{ invalid }">
    <v-form @submit.prevent="submit">
      <validation-provider
        v-slot="{ errors }"
        name="Vorname"
        rules="required"
      >
        <v-text-field
          label="Spieler 1: Vorname"
          v-model="firstName1"
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
          label="Spieler 1: Zuname"
          v-model="lastName1"
          :counter="20"
          :error-messages="errors"
          required
        ></v-text-field>
      </validation-provider>
      <validation-provider
        v-slot="{ errors }"
        name="Vorname"
        rules="required"
      >
        <v-text-field
          label="Spieler 2: Vorname"
          v-model="firstName2"
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
          label="Spieler 2: Zuname"
          v-model="lastName2"
          :counter="20"
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
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from 'vee-validate';
import { required } from 'vee-validate/dist/rules';

setInteractionMode('lazy');

extend('required', {
  ...required,
  message: '{_field_} ist erforderlich!',
});

export default {
  name: 'PlayerForm',
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  computed: {
    firstName1: {
      get () {
        return this.$store.state.team.firstName1
      },
      set (value) {
        this.$store.commit('setTeamValues', {'firstName1': value})
      }
    },
    lastName1: {
      get () {
        return this.$store.state.team.lastName1
      },
      set (value) {
        this.$store.commit('setTeamValues', {'lastName1': value})
      }
    },
    firstName2: {
      get () {
        return this.$store.state.team.firstName2
      },
      set (value) {
        this.$store.commit('setTeamValues', {'firstName2': value})
      }
    },
    lastName2: {
      get () {
        return this.$store.state.team.lastName2
      },
      set (value) {
        this.$store.commit('setTeamValues', {'lastName2': value})
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
};
</script>