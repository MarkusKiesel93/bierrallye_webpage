<template>
  <v-card>
    <v-card-title>
      Abmeldung
    </v-card-title>
    <DeregisterForm />
  </v-card>
</template>

<script>
import DeregisterForm from '@/components/DeregisterForm'


export default {
  name: 'DeregisterView',
  components: {
    DeregisterForm,
  },
}
</script>