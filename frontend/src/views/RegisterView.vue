<template>
  <v-card>
    <v-card-title> Anmeldung </v-card-title>
    <v-form>
      <v-stepper v-model='step' vertical>
        <v-stepper-step step='1' :complete='step > 1'> Kontakt </v-stepper-step>
          <v-stepper-content step='1'>
            <validation-observer ref="observer" v-slot="{ invalid }">
              <InputEmail
                :value="email"
                :setter="emailSetter"
              />
              <ButtonsNextBack
                :disabled="invalid"
                v-on:click-next='nextStep'
                v-on:click-back='lastStep'
              />
          </validation-observer>
        </v-stepper-content>

        <v-stepper-step step='2' :complete='step > 2'> Spieler </v-stepper-step>

        <v-stepper-content step='2'>
          <validation-observer ref="observer" v-slot="{ invalid }">
            <h3> Spieler 1 </h3>
            <InputName
              :value="name1"
              :setter="player1Setter"
            />
            <InputSelectBox
              label="Getränke"
              :items="drinks_options"
              :setter="player1Setter"
            />
            <h3> Spieler 2 </h3>
            <InputName
              :value="name2"
              :setter="player2Setter"
            />
            <InputSelectBox
              label="Getränke"
              :items="drinks_options"
              :setter="player2Setter"
            />
            <ButtonsNextBack
              :disabled="invalid"
              v-on:click-next='nextStep'
              v-on:click-back='lastStep'
            />
          </validation-observer>
        </v-stepper-content>

        <v-stepper-step step='3' :complete='step > 3'> Startblock </v-stepper-step>

        <v-stepper-content step='3'>
          <InputSelectBox
              label="Startblock"
              :items="times_options"
              :setter="timeSetter"
            />
          <ButtonsNextBack
            :disabled="invalid"
            v-on:click-next='nextStep'
            v-on:click-back='lastStep'
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
    </v-form>
  </v-card>
</template>

<script>
import { ValidationObserver, setInteractionMode } from 'vee-validate'
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'

import RegistrationInfo from '@/components/RegistrationInfo'
import RegistrationCompletion from '@/components/RegistrationCompletion'
import InputName from '@/components/InputName'
import InputEmail from '@/components/InputEmail'
import InputSelectBox from '@/components/InputSelectBox'
import ButtonsNextBack from '@/components/ButtonsNextBack'

setInteractionMode('lazy')


export default {
  name: 'RegisterView',
  components: {
    ValidationObserver,
    InputName,
    InputEmail,
    InputSelectBox,
    ButtonsNextBack,
    RegistrationInfo,
    RegistrationCompletion,
  },
  computed: {
    ...mapState({
      email: (state) => state.team.email,
      drinkPrefPlayer1: (state) => state.team.drinkPrefPlayer1,
      drinkPrefPlayer2: (state) => state.team.drinkPrefPlayer2,
      timePref: (state) => state.team.timePref,
      drinks_options: (state) => state.drinks_options,
      times_options: (state) => state.times_options,
      info: (state) => state.createInfo,
    }),
    ...mapGetters({
      name1: 'getPlayer1Name',
      name2: 'getPlayer2Name',
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
    ...mapMutations({
      emailSetter: 'setTeamEmail',
      player1Setter: 'setPlayer1',
      player2Setter: 'setPlayer2',
      timeSetter: 'setTimePref',
    }),
    ...mapActions({
      createTeam: 'createTeam',
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