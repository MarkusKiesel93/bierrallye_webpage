<template>
  <v-form>
    <v-select
      v-model="drinkPref"
      :items="drinks"
      label="Getränke"
    ></v-select>
    <v-select
      v-model="timePref"
      :items="times"
      label="Startzeit"
    ></v-select>
    <v-btn
      color="primary"
      class="mr-4 mt-4"
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
      
</template>

<script>
export default {
  name: 'PreferenceForm',
  computed: {
    drinkPref: {
      get () {
        return this.$store.state.team.drinkPref
      },
      set (value) {
        this.$store.commit('setTeamValues', {'drinkPref': value})
      }
    },
    timePref: {
      get () {
        return this.$store.state.team.timePref
      },
      set (value) {
        this.$store.commit('setTeamValues', {'timePref': value})
      }
    },
  },
  data: () => ({
    drinks: ['Bier', 'Wein', 'Gemischt', 'wissen wir noch nicht'],
    times: ['zu Beginn', 'mittendrin', 'zu Ende', 'ist uns egal'],
  }),
  methods: {
    submit() {
      this.$emit('next-step');
    },
    cancel() {
      this.$emit('last-step');
    },
  },
}
</script>