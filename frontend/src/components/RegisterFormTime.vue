<template>
  <v-form>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <InfoItems :items="timeInfo" />
      <InputSelectBox
        label="Startblock"
        :value="timePref"
        :items="timeOptions"
        :setter="timeSetter"
      />
      <ButtonsSubmitCancel
        submitLabel="Weiter"
        :disabled="invalid"
        v-on:click-submit="$emit('click-submit')"
        v-on:click-cancel="$emit('click-cancel')"
      />
    </validation-observer>
  </v-form>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'
import { ValidationObserver } from 'vee-validate'

import InfoItems from '@/components/InfoItems'
import InputSelectBox from '@/components/InputSelectBox'
import ButtonsSubmitCancel from '@/components/ButtonsSubmitCancel'

export default {
  name: 'RegisterFormTime',
  components: {
    ValidationObserver,
    InfoItems,
    InputSelectBox,
    ButtonsSubmitCancel,
  },
  computed: {
    ...mapState({
      timePref: state => state.register.timePref,
    }),
    ...mapGetters({
      timeInfo: 'register/timeInfo',
      timeOptions: 'register/timeOptions',
    }),
  },
  methods: {
    ...mapMutations({
      timeSetter: 'register/setTimePref',
    }),
    ...mapActions({
      requestTimeOptions: 'register/requestTimeOptions',
    }),
   },
   created: function() {
    this.requestTimeOptions()
  },
}
</script>

<style>

</style>