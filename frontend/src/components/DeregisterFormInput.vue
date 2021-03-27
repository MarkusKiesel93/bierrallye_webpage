<template>
  <v-form>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <!-- here now also input contact maby without test -->
      <InputContact
        :channel="channel"
        :email="email"
        :phoneNumber="phoneNumber"
        :channelSetter="channelSetter"
        :emailSetter="emailSetter"
        :phoneNumberSetter="phoneNumberSetter"
      />
      <InputCode
        :value="hash"
        :setter="hashSetter"
        label="Stornocode"
        counter="6"
      />
      <ButtonsSubmitCancel
        :disabled="invalid"
        v-on:click-submit="getTeamSubmit()"
        v-on:click-cancel="$emit('click-cancel')"
      />
    </validation-observer>
  </v-form>
</template>

<script>
import { ValidationObserver } from 'vee-validate'
import { mapState, mapMutations, mapActions } from 'vuex'

import InputContact from '@/components/InputContact'
import InputCode from '@/components/InputCode'
import ButtonsSubmitCancel from '@/components/ButtonsSubmitCancel'

export default {
  name: 'DeregisterFormInput',
  components: {
    ValidationObserver,
    InputContact,
    InputCode,
    ButtonsSubmitCancel,
  },
  computed: {
    ...mapState({
      channel: state => state.deregister.channel,
      email: state => state.deregister.email,
      phoneNumber: state => state.deregister.phoneNumber,
      hash: state => state.deregister.hash,
    }),
  },
  methods: {
    ...mapMutations({
      channelSetter: 'deregister/setChannel',
      emailSetter: 'deregister/setEmail',
      phoneNumberSetter: 'deregister/setPhoneNumber',
      hashSetter: 'deregister/setHash',
    }),
    ...mapActions({
      requestTeam: 'deregister/requestTeam'
    }),

    getTeamSubmit() {
      this.requestTeam()
      this.$emit('click-submit')
    }
  },
}
</script>
