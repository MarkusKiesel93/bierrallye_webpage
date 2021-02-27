<template>
  <v-form>
    <v-stepper v-model="step" vertical>
      <v-stepper-step step="1" :complete="step > 1"> Abmeldung angeben </v-stepper-step>
      <v-stepper-content step="1">
        <validation-observer ref="observer" v-slot="{ invalid }">
          <InputEmail
            :value="email"
            :setter="emailSetter"
          />
          <InputCode
            :value="hash"
            :setter="hashSetter"
            label="Stornocode"
            counter="6"
          />
          <ButtonsNextBack
            v-on:click-next='nextStep'
            v-on:click-back='lastStep'
            :disabled="invalid"
          />
        </validation-observer>
      </v-stepper-content>

      <v-stepper-step step="2"> Abmeldung bestätigen </v-stepper-step>

      <v-stepper-content step="2">
        <InfoItems :items="infoItems" />
        <AlertField
          type="success"
          :value="success"
          row1="Du hast dein Team abgemeldet"
          :row2="successMessage"
        />
        <AlertField
          type="error"
          :value="error"
          row1="Es gab einen Fehler bei der Abmeldung:"
          :row2="errorMessage"
        />
        <ButtonsNextBack
          :disabled="invalid"
          nextLabel="Abmelden"
          v-on:click-next='sumbit'
          v-on:click-back='lastStep'
        />
      </v-stepper-content>
    </v-stepper>
  </v-form>
</template>

<script>
import { ValidationObserver, setInteractionMode } from 'vee-validate'
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'

import InfoItems from '@/components/InfoItems'
import InputEmail from '@/components/InputEmail'
import InputCode from '@/components/InputCode'
import ButtonsNextBack from '@/components/ButtonsNextBack'
import AlertField from '@/components/AlertField'

setInteractionMode('lazy');


export default {
  name: "DeregisterForm",
  components: {
    ValidationObserver,
    InputEmail,
    InputCode,
    InfoItems,
    ButtonsNextBack,
    AlertField
  },
  computed: {
    ...mapState({
      email: (state) => state.deregister.email,
      hash: (state) => state.deregister.hash,
      success: (state) => state.deleteSuccess,
      error: (state) => state.deleteError,
      errorMessage: (state) => state.deleteErrorMessage,
    }),
    ...mapGetters({
      infoItems: 'getDeregistrationInfo',
      successMessage: 'getDeleteSuccessMessage',
    }),
  },
  data: () => ({
    step: 1,
    invalid: null,
  }),
  methods: {
    ...mapMutations({
      emailSetter: 'setDeregisterEmail',
      hashSetter: 'setDeregisterHash',
      setDeleteSuccess: 'setDeleteSuccess',
      setDeleteError: 'setDeleteError',
    }),
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
    sumbit() {
      if (!this.success) {
        this.deleteTeam()
      } 
    },
    handleSuccess() {
      this.setDeleteSuccess(false)
      this.$router.push({ name: 'HomeView' })
    },
  },
  watch: {
    success: function() {
      if (this.success) {
        this.setDeleteError(false)
        setTimeout(this.handleSuccess, 5000)
      }
    },
  }
}
</script>