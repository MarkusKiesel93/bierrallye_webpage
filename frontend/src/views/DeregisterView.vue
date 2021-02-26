<template>
  <v-card>
    <v-card-title>
      Abmeldung
    </v-card-title>
    <v-stepper v-model="step" vertical>
      <v-stepper-step step="1" :complete="step > 1">
        Abmeldung angeben
      </v-stepper-step>

      <v-stepper-content step="1">
        <DeregistrationForm 
          v-on:next-step='nextStep'
          v-on:last-step='lastStep'
        />
      </v-stepper-content>

      <v-stepper-step step="2">
        Abmeldung bestätigen
      </v-stepper-step>

      <v-stepper-content step="2">
        <DeregistrationInfo />
        <v-alert
          type='success'
          :value="successAlert"
        >
          <v-row>
            <div> Du hast dein Team für die <strong>Bierralley 2021</strong> erfolgreich abgemeldet </div>
          </v-row>
          <v-row>
            <div> Eine Bestätigung bekommst du in den nächsten Minuten an: <strong>{{ info }}</strong> </div>
          </v-row>
        </v-alert>
        <v-alert
          type='error'
          dismissible
          :value="failedAlert"
        >
          <v-row>
            <div> Es gab einen <strong>Fehler</strong> bei der Abmeldung: </div>
          </v-row>
          <v-row>
            {{ info }}
          </v-row>
        </v-alert>
        <v-btn
          color="primary"
          class="mr-4 mt-4"
          @click="completeDeregistration"
        >
          Abmelden
        </v-btn>
        <v-btn
          class="mt-4"
          @click="lastStep"
        >
          Zurück
        </v-btn>
      </v-stepper-content>
    </v-stepper>
  </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import DeregistrationForm from '@/components/DeregistrationForm'
import DeregistrationInfo from '@/components/DeregistrationInfo'

export default {
  name: "DeregisterView",
  components: {
    DeregistrationForm,
    DeregistrationInfo,
  },
  computed: {
    ...mapState({
      info: (state) => state.deleteInfo,
    }),
    status: {
      get () {
        return this.$store.state.deleteStatus
      },
      set (value) {
        this.$store.commit('setStatus', {'deleteStatus': value})
      }
    },
  },
  data: () => ({
    step: 1,
    successAlert: false,
    failedAlert: false,
  }),
  created: function () {
    if (this.$route.params.email) {
      this.$store.commit('setDeregisterEmail', this.$route.params.email)
    } 
    if (this.$route.params.hash) {
      this.$store.commit('setDeregisterHash', this.$route.params.hash)
    } 
  },
  methods: {
    ...mapActions({
      deleteTeam: 'deleteTeam'
    }),
    nextStep() {
      this.step += 1
    },
    lastStep() {
      this.step -= 1
      if (this.step < 1) {
        this.$router.push({ name: 'HomeView' })
      }
    },
    completeDeregistration() {
      if (!this.status) {
        this.deleteTeam()
      } 
    },
    handleSuccess() {
      this.status = null
      this.successAlert = false
      this.$router.push({ name: 'HomeView' })
    },
  },
  watch: {
    status: function() {
      if (this.status == 'success') {
        this.successAlert = true
        this.failedAlert = false
        setTimeout(this.handleSuccess, 4000)
      } else if (this.status == 'failed') {
        this.successAlert = false
        this.failedAlert = true
        this.status = null
      }
    },
  }
}
</script>