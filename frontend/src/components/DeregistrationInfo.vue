<template>
  <v-container fluid>
    <v-row>
      <v-col cols=6>
        <strong>E-Mail:</strong>
      </v-col>
      <v-col>
        <p> {{ email }} </p>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols=6>
        <strong>Stornocode:</strong>
      </v-col>
      <v-col>
        <p> {{ hash }} </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: "DeregistrationInfo",
  computed: {
    ...mapState({
      email: (state) => state.deregisterEmail,
      hash: (state) => state.deregisterHash,
    }),
  },
}
</script>