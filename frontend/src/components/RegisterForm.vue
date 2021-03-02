<template>
  <v-form>
    <v-stepper v-model='step'>
      <v-stepper-header>
        <v-stepper-step step='1' :complete='step > 1'> Kontakt </v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step step='2' :complete='step > 2'> Spieler </v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step step='3' :complete='step > 3'> Startzeit </v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step step='4'> Anmeldung abschicken </v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
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
              label="Getränk"
              :value="drinkPrefPlayer1"
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
              label="Getränk"
              :value="drinkPrefPlayer2"
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

        <v-stepper-content step='3'>
          <validation-observer ref="observer" v-slot="{ invalid }">
            <InfoItems :items="timeInfo" />
            <InputSelectBox
                label="Startblock"
                :value="timePref"
                :items="timesOptions"
                :setter="timeSetter"
              />
            <ButtonsNextBack
              :disabled="invalid"
              v-on:click-next='nextStep'
              v-on:click-back='lastStep'
            />
          </validation-observer>
        </v-stepper-content>

        <v-stepper-content step='4'>
          <InfoItems :items="infoItems" />
          <validation-observer ref="observer" v-slot="{ invalid }">
            <InputCheckbox
              :value="acceptedDataLaws"
              :setter="checkboxSetter"
              fieldName="Datenschutzerklärung"
              text="Datenschutzerklärung"
              :routerTo="{ name: 'DataProtectionView' }"
            />
            <AlertField
              type="error"
              :value="error"
              row1="Es gab einen Fehler bei der Anmeldung:"
              :row2="errorMessage"
            />
            <LoadingCircle
              :show="loading"
            />
            <ButtonsNextBack
              :disabled="invalid"
              nextLabel="Anmelden"
              v-on:click-next='createTeam'
              v-on:click-back='lastStep'
            />
          </validation-observer>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-form>
</template>

<script>
import { ValidationObserver, setInteractionMode } from 'vee-validate'
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'

import InfoItems from '@/components/InfoItems'
import InputName from '@/components/InputName'
import InputEmail from '@/components/InputEmail'
import InputSelectBox from '@/components/InputSelectBox'
import InputCheckbox from '@/components/InputCheckbox'
import ButtonsNextBack from '@/components/ButtonsNextBack'
import AlertField from '@/components/AlertField'
import LoadingCircle from '@/components/LoadingCircle'

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
    InputCheckbox,
    AlertField,
    LoadingCircle,
  },
  data: () => ({
    step: 1,
    invalid: null,
  }),
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
      acceptedDataLaws: (state) => state.acceptedDataLaws,
      success: (state) => state.createSuccess,
      error: (state) => state.createError,
      errorMessage: (state) => state.createErrorMessage,
      loading: (state) => state.loading,
    }),
    ...mapGetters({
      timeInfo: 'getTimeInfo',
      infoItems: 'getRegistrationInfo',
    }),
  },
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
      checkboxSetter: 'setAcceptedDataLaws',
      setCreateError: 'setCreateError',
    }),
    ...mapActions({
      createTeam: 'createTeam',
      getPlacesFree: 'getPlacesFree',
    }),
    nextStep() {
      this.step += 1
      if (this.step === 3) {
        this.getPlacesFree()
      }
    },
    lastStep() {
      this.step -= 1
      if (this.step < 1) {
        this.$router.push({ name: 'HomeView' })
      }
    },
  },
  watch: {
    success: function() {
      if (this.success) {
        this.$router.push({ name: 'RegisterSuccessView' })
      }
    },
  }
}
</script>