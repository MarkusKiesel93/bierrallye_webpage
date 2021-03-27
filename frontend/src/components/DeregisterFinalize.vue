<template>
  <div>
    <InfoItems :items="infoItems" />
    <AlertField
      :type="alertType"
      :value="alert"
      :message="alertMessage"
    />
    <LoadingCircle :show="loading" />
    <ButtonsSubmitCancel
      submitLabel="Abmelden"
      v-on:click-submit="deleteTeam()"
      v-on:click-cancel="$emit('click-cancel')"
    />
  </div>
</template>

<script>
import { mapState, mapGetters, mapActions } from 'vuex'

import InfoItems from '@/components/InfoItems'
import AlertField from '@/components/AlertField'
import LoadingCircle from '@/components/LoadingCircle'
import ButtonsSubmitCancel from '@/components/ButtonsSubmitCancel'

export default {
  name: 'DeregisterFinalize',
  components: {
    InfoItems,
    ButtonsSubmitCancel,
    AlertField,
    LoadingCircle,
  },
  computed: {
    ...mapState({
      loading: state => state.deregister.loading,
      success: state => state.deregister.success,
      alert: state => state.deregister.alert,
      alertType: state => state.deregister.alertType,
      alertMessage: state => state.deregister.alertMessage,
      
    }),
    ...mapGetters({
      infoItems: 'deregister/info',
    }),
  },
  methods: {
    ...mapActions({
      deleteTeam: 'deregister/deleteTeam',
    }),
  },
  watch: {
    success: function() {
      if (this.success) {
        this.$router.push({ name: 'DeregisterViewSuccess' })
      }
    },
  },
}
</script>
