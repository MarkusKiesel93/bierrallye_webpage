<template>
  <v-container fluid>
    <AlertField
      type="success"
      :value="true"
      message="Du hast dein Team erfolgreich abgemeldet von der Bierrallye."
    />
    <v-btn color="primary" @click="$router.push({ name: 'HomeView' })">
      Startseite
    </v-btn>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'

import AlertField from '@/components/AlertField'

export default {
  name: 'DeregisterViewSuccess',
  components: {
    AlertField,
  },
  computed: {
    ...mapGetters({
      successMessage: 'getDeleteSuccessMessage',
    }),
  },
}
</script>
