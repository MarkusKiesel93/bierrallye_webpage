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
              v-on:click-next='nextStep'
              v-on:click-back='lastStep'
              :disabled="invalid"
            />
          </validation-observer>
        </v-stepper-content>

        <v-stepper-step step='2' :complete='step > 2'> Spieler </v-stepper-step>
        <v-stepper-content step='2'>
          <validation-observer ref="observer" v-slot="{ invalid }">
            <h3> Spieler 1 </h3>
            <InputName
              :firstName="firstNamePlayer1"
              :lastName="lastNamePlayer1"
              :firstNameSetter="firstName1Setter"
              :lastNameSetter="lastName1Setter"
            />
            <InputSelectBox
              label="Getränke"
              :items="drinksOptions"
              :setter="drinkPref1Setter"
            />
            <h3> Spieler 2 </h3>
            <InputName
              :firstName="firstNamePlayer2"
              :lastName="lastNamePlayer2"
              :firstNameSetter="firstName2Setter"
              :lastNameSetter="lastName2Setter"
            />
            <InputSelectBox
              label="Getränke"
              :items="drinksOptions"
              :setter="drinkPref2Setter"
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
              :items="timesOptions"
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
          <InfoItems :items="infoItems" />
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

import InfoItems from '@/components/InfoItems'
import RegistrationCompletion from '@/components/RegistrationCompletion'
import InputName from '@/components/InputName'
import InputEmail from '@/components/InputEmail'
import InputSelectBox from '@/components/InputSelectBox'
import ButtonsNextBack from '@/components/ButtonsNextBack'

setInteractionMode('lazy')


export default {
  name: 'RegisterForm',
  components: {
    ValidationObserver,
    InputName,
    InputEmail,
    InputSelectBox,
    ButtonsNextBack,
    InfoItems,
    RegistrationCompletion,
  },
  computed: {
    ...mapState({
      email: (state) => state.team.email,
      firstNamePlayer1: (state) => state.team.firstNamePlayer1,
      lastNamePlayer1: (state) => state.team.lastNamePlayer1,
      drinkPrefPlayer1: (state) => state.team.drinkPrefPlayer1,
      firstNamePlayer2: (state) => state.team.firstNamePlayer2,
      lastNamePlayer2: (state) => state.team.lastNamePlayer2,
      drinkPrefPlayer2: (state) => state.team.drinkPrefPlayer2,
      timePref: (state) => state.team.timePref,
      drinksOptions: (state) => state.drinksOptions,
      timesOptions: (state) => state.timesOptions,
      info: (state) => state.createInfo,
    }),
    ...mapGetters({
      infoItems: 'getRegistrationInfo'
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
    invalid: null,
    successAlert: false,
    failedAlert: false,
  }),
  methods: {
    ...mapMutations({
      emailSetter: 'setTeamEmail',
      firstName1Setter: 'setFirstNamePayer1',
      lastName1Setter: 'setLastNamePlayer1',
      drinkPref1Setter: 'setDrinkPrefPlayer1',
      firstName2Setter: 'setFirstNamePayer2',
      lastName2Setter: 'setLastNamePlayer2',
      drinkPref2Setter: 'setDrinkPrefPlayer2',
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