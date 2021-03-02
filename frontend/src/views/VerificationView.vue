<template>
  <v-container fluid>
    <LoadingCircle
      :show="loading"
    />
    <AlertField
      type="success"
      :value="success"
      :dismissible="false"
      row1="Gratulation, Ihr seid dabei bei der Bierrallye Irnfritz 2021"
      :row2="successMessage"
    />
    <AlertField
      type="error"
      :value="error"
      row1="Ups, es ist was falsch gelaufen"
      :row2="errorMessage"
    />
    <v-btn 
      color="primary"
      @click="$router.push({ name: 'HomeView' })"
    >
      Startseite
    </v-btn>
  </v-container>
</template>

<script>
import { mapState, mapGetters, mapActions, mapMutations } from 'vuex'

import LoadingCircle from '@/components/LoadingCircle'
import AlertField from '@/components/AlertField'


export default {
  name: 'VerificationView',
  components: {
    LoadingCircle,
    AlertField,
  },
  computed: {
    ...mapState({
      loading: (state) => state.loading,
      success: (state) => state.verificationSuccess,
      error: (state) => state.verificationError,
      errorMessage: (state) => state.verificationErrorMessage,
    }),
    ...mapGetters({
      successMessage: 'getVerifySuccessMessage',
    })
  },
  methods: {
    ...mapMutations({
      setVerifyEmail: 'setVerifyEmail',
      setVerifyHash: 'setVerifyHash',
    }),
    ...mapActions({
      verifyTeam: 'verifyTeam',
    })
  },
  created: function() {
    this.setVerifyEmail(this.$route.params.email)
    this.setVerifyHash(this.$route.params.hash)
    this.verifyTeam()
  }
}
</script>