<template>
  <v-container fluid>
    <AlertField
      type="success"
      :value="true"
      :dismissible="false"
      row1="Du hast dein Team für die Bierrallye 2021 erfolgreich angebeldet"
      :row2="successMessage"
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
import { mapGetters } from 'vuex'

import AlertField from '@/components/AlertField'

export default {
  name: 'RegisterSuccessView',
  components: {
    AlertField,
  },
  computes: {
    ...mapGetters({
      successMessage: 'getCreateSuccessMessage',
    })
  },
}
</script>