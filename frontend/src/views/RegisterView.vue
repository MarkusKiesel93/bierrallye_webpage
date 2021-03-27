<template>
  <v-stepper v-model="step">
    <v-stepper-header>
      <v-stepper-step step="1" :complete="step > 1"> Kontakt </v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step step="2" :complete="step > 2"> Spieler </v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step step="3" :complete="step > 3">
        Startzeit
      </v-stepper-step>
      <v-divider></v-divider>
      <v-stepper-step step="4"> Anmeldung abschicken </v-stepper-step>
    </v-stepper-header>

      <v-stepper-content step="1">
        <RegisterFormPlayer 
          v-on:click-submit="nextStep"
          v-on:click-cancel="lastStep"
        />
      </v-stepper-content>

      <v-stepper-content step="2">
        <RegisterFormTime 
          v-on:click-submit="nextStep"
          v-on:click-cancel="lastStep"
        />
      </v-stepper-content>

      <v-stepper-items>
      <v-stepper-content step="3">
        <RegisterFormContactInfo
          v-on:click-submit="nextStep"
          v-on:click-cancel="lastStep"
        />
      </v-stepper-content>
        
      <v-stepper-content step="4">
        <RegisterFormFinalize
          v-on:click-submit="nextStep"
          v-on:click-cancel="lastStep"
        />
      </v-stepper-content>
    </v-stepper-items>
  </v-stepper>
</template>

<script>
import RegisterFormPlayer from '@/components/RegisterFormPlayer'
import RegisterFormTime from '@/components/RegisterFormTime'
import RegisterFormContactInfo from '@/components/RegisterFormContactInfo'
import RegisterFormFinalize from '@/components/RegisterFormFinalize'

export default {
  name: 'RegisterView',
  components: {
    RegisterFormPlayer,
    RegisterFormTime,
    RegisterFormContactInfo,
    RegisterFormFinalize,
  },
  data: () => ({
    step: 1,
  }),
  methods: {
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
}
</script>
