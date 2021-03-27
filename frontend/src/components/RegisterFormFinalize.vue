<template>
  <v-form>  
    <validation-observer ref="observer" v-slot="{ invalid }">
      <InfoItems :items="infoItems" />
      <DialogGameRules />
      <DialogDataProtection />
      <InputCheckbox
        :value="acceptedGameRules"
        :setter="gameRulesSetter"
        fieldName="Teilnahmebedingung"
        text="Teilnahmebedingung"
        :routerTo="{ name: 'GameRulesView' }"
      />
      <InputCheckbox
        :value="acceptedDataLaws"
        :setter="dataLawsSetter"
        fieldName="Datenschutzerklärung"
        text="Datenschutzerklärung"
        :routerTo="{ name: 'DataProtectionView' }"
      />
      <AlertField
        :type="alertType"
        :value="alert"
        :message="alertMessage"
      />
      <LoadingCircle :show="loading" />
      <ButtonsSubmitCancel
        :disabled="invalid"
        submitLabel="Anmelden"
        v-on:click-submit="createTeam()"
        v-on:click-cancel="$emit('click-cancel')"
      />
    </validation-observer>
  </v-form>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'
import { ValidationObserver } from 'vee-validate'

import InfoItems from '@/components/InfoItems'
import InputCheckbox from '@/components/InputCheckbox'
import AlertField from '@/components/AlertField'
import LoadingCircle from '@/components/LoadingCircle'
import DialogGameRules from '@/components/DialogGameRules'
import DialogDataProtection from '@/components/DialogDataProtection'
import ButtonsSubmitCancel from '@/components/ButtonsSubmitCancel'

export default {
  name: 'RegisterFormFinalize',
  components: {
    ValidationObserver,
    InfoItems,
    InputCheckbox,
    AlertField,
    LoadingCircle,
    DialogGameRules,
    DialogDataProtection,
    ButtonsSubmitCancel,
  },
  data: () => ({
    showDialog: true,
  }),
  computed: {
    ...mapState({
      acceptedGameRules: state => state.register.acceptedGameRules,
      acceptedDataLaws: state => state.register.acceptedDataLaws,
      loading: state => state.register.loading,
      success: state => state.register.success,
      alert: state => state.register.alert,
      alertType: state => state.register.alertType,
      alertMessage: state => state.register.alertMessage,
    }),
    ...mapGetters({
      infoItems: 'register/registrationInfo',
    }),
  },
  methods: {
    ...mapMutations({
      gameRulesSetter: 'register/setAcceptedGameRules',
      dataLawsSetter: 'register/setAcceptedDataLaws',
      setCreateError: 'register/setCreateError',
    }),
    ...mapActions({
      createTeam: 'register/createTeam',
    }),
   },
  watch: {
    success: function() {
      if (this.success) {
        this.$router.push({ name: 'RegisterViewSuccess' })
      }
    },
  },
}
</script>