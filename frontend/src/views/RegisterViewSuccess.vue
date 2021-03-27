<template>
  <v-container fluid>
    <AlertField
      type="success"
      :value="true"
      message="Gratulation, ihr habt euch erfolgreich angemeldet."
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
  name: 'RegisterViewSuccess',
  components: {
    AlertField,
  },
  computed: {
    ...mapGetters({
      successMessage: 'getCreateSuccessMessage',
    }),
  },
}
</script>
