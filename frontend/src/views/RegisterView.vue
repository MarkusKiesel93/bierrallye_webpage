<template>
  <v-card>
    <v-card-title> Anmeldung </v-card-title>
    <v-stepper v-model='step' vertical>
      <v-stepper-step step='1' :complete='step > 1'> Kontakt </v-stepper-step>
      <v-stepper-content step='1'>
        <ContactForm
          v-on:next-step='nextStep'
          v-on:last-step='lastStep'
        />
      </v-stepper-content>

      <v-stepper-step step='2' :complete='step > 2'> Spieler </v-stepper-step>

      <v-stepper-content step='2'>
        <PlayerForm
          v-on:next-step='nextStep'
          v-on:last-step='lastStep'
        />
      </v-stepper-content>

      <v-stepper-step step='3' :complete='step > 3'> Preferenzen </v-stepper-step>

      <v-stepper-content step='3'>
        <PreferenceForm
          v-on:next-step='nextStep'
          v-on:last-step='lastStep'
        />
      </v-stepper-content>

      <v-stepper-step step='4'> Daten bestätigen </v-stepper-step>

      <v-stepper-content step='4'>
        <RegistrationInfo />
        <v-alert
          type='success'
          :value="successAlert"
        >
          <v-row>
            <div> Du hast dein Team für die <strong>Bierralley 2021</strong> erfolgreich angebeldet </div>
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
            <div> Es gab einen <strong>Fehler</strong> bei der Anmeldung: </div>
          </v-row>
          <v-row>
            {{ info }}
          </v-row>
        </v-alert>
        <RegistrationCompletion
          v-on:complete-registration='completeRegistration'
          v-on:last-step='lastStep'
        />
      </v-stepper-content>
    </v-stepper>
  </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex'

import ContactForm from '@/components/ContactForm'
import PlayerForm from '@/components/PlayerForm'
import PreferenceForm from '@/components/PreferenceForm'
import RegistrationInfo from '@/components/RegistrationInfo'
import RegistrationCompletion from '@/components/RegistrationCompletion'

export default {
  name: 'RegisterView',
  components: {
    ContactForm,
    PlayerForm,
    PreferenceForm,
    RegistrationInfo,
    RegistrationCompletion,
  },
  computed: {
    ...mapState({
      info: (state) => state.createInfo,
    }),
    status: {
      get () {
        return this.$store.state.createStatus
      },
      set (value) {
        this.$store.commit('setStatus', {'createStatus': value})
      }
    },
  },
  data: () => ({
    step: 1,
    successAlert: false,
    failedAlert: false,
  }),
  methods: {
    ...mapActions({
      createTeam: 'createTeam'
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
    completeRegistration() {
      if (!this.status) {
        this.createTeam()
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