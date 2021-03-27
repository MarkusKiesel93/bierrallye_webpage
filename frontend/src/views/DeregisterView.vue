<template>
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
        <DeregisterFormInput 
          v-on:click-submit="nextStep"
          v-on:click-cancel="lastStep"
        />
      </v-stepper-content>

      <v-stepper-content step="2">
        <DeregisterFinalize 
          v-on:click-submit="nextStep"
          v-on:click-cancel="lastStep"
        />
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</template>

<script>
import { mapMutations } from 'vuex'

import DeregisterFormInput from '@/components/DeregisterFormInput'
import DeregisterFinalize from '@/components/DeregisterFinalize'

export default {
  name: 'DeregisterView',
  components: {
    DeregisterFormInput,
    DeregisterFinalize,
  },
  data: () => ({
    step: 1,
  }),
  methods: {
    ...mapMutations({
      setContact: 'deregister/setContact',
      setHash: 'deregister/setHash',
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
  created: function() {
    if (this.$route.params.channel && this.$route.params.contact) {
      this.setContact({
        channel: this.$route.params.channel,
        contact: this.$route.params.contact,
      })
    }
    if (this.$route.params.hash) {
      this.setHash(this.$route.params.hash)
    }
  },
}
</script>
