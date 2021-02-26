<template>
  <v-container fluid>
    <v-row>
      <v-col cols=6>
        <strong>Kontakt:</strong>
      </v-col>
      <v-col>
        <p> {{ team.email }} </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols=6>
        <strong>Spieler 1:</strong>
      </v-col>
      <v-col>
        <p> {{ team.firstName1 }} {{ team.lastName1 }} </p>
      </v-col>
    </v-row>
      <v-row>
      <v-col cols=6>
        <strong> Spieler 2:</strong>
      </v-col>
      <v-col>
        <p> {{ team.firstName2 }} {{ team.lastName2 }} </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols=6>
        <strong> Getränke: </strong>
      </v-col>
      <v-col>
        <p> {{ team.drinkPref }} </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols=6>
        <strong> Startzeit: </strong>
      </v-col>
      <v-col>
        <p> {{ team.timePref }} </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: "RegistrationInfo",
  computed: {
    ...mapState({
      team: (state) => state.team,
    }),
  },
}
</script>