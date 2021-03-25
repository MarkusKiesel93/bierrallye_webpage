<template>
  <v-form>
    <v-stepper v-model="step">
      <v-stepper-header>
        <v-stepper-step step="1" :complete="step > 1">
          Abmeldung angeben
        </v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step step="2"> Abmeldung abschicken </v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <validation-observer ref="observer" v-slot="{ invalid }">
            <InputEmail :value="email" :setter="emailSetter" />
            <InputCode
              :value="hash"
              :setter="hashSetter"
              label="Stornocode"
              counter="6"
            />
            <ButtonsSubmitCancel
              v-on:click-submit="nextStep"
              v-on:click-cancel="lastStep"
              :disabled="invalid"
            />
          </validation-observer>
        </v-stepper-content>

        <v-stepper-content step="2">
          <InfoItems :items="infoItems" />
          <AlertField
            type="error"
            :value="error"
            row1="Es gab einen Fehler bei der Abmeldung:"
            :row2="errorMessage"
          />
          <LoadingCircle :show="loading" />
          <ButtonsSubmitCancel
            :disabled="invalid"
            submitLabel="Abmelden"
            v-on:click-submit="deleteTeam"
            v-on:click-cancel="lastStep"
          />
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-form>
</template>

<script>
import { ValidationObserver, setInteractionMode } from 'vee-validate'
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'

import InfoItems from '@/components/InfoItems'
import InputEmail from '@/components/InputEmail'
import InputCode from '@/components/InputCode'
import ButtonsSubmitCancel from '@/components/ButtonsSubmitCancel'
import AlertField from '@/components/AlertField'
import LoadingCircle from '@/components/LoadingCircle'

setInteractionMode('lazy')

export default {
  name: 'DeregisterForm',
  components: {
    ValidationObserver,
    InputEmail,
    InputCode,
    InfoItems,
    ButtonsSubmitCancel,
    AlertField,
    LoadingCircle,
  },
  data: () => ({
    step: 1,
    invalid: null,
  }),
  computed: {
    ...mapState({
      email: state => state.deregister.email,
      hash: state => state.deregister.hash,
      success: state => state.deleteSuccess,
      error: state => state.deleteError,
      errorMessage: state => state.deleteErrorMessage,
      loading: state => state.loading,
    }),
    ...mapGetters({
      infoItems: 'getDeregistrationInfo',
    }),
  },
  methods: {
    ...mapMutations({
      emailSetter: 'setDeregisterEmail',
      hashSetter: 'setDeregisterHash',
      setDeleteError: 'setDeleteError',
    }),
    ...mapActions({
      deleteTeam: 'deleteTeam',
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
  },
  watch: {
    success: function() {
      if (this.success) {
        this.$router.push({ name: 'DeregisterSuccessView' })
      }
    },
  },
}
</script>
