<template>
  <v-form>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <v-radio-group v-model="channelValue" mandatory column>
        <v-radio
          label="E-Mail"
          value="email"
        ></v-radio>
        <v-radio
          label="SMS"
          value="sms"
        ></v-radio>
      </v-radio-group>
      <InputEmail
        v-if="channelValue==='email'"
        :value="email"
        :setter="emailSetter"
      />
      <InputPhoneNumber 
        v-if="channelValue==='sms'"
        :value="phoneNumber"
        :setter="phoneNumberSetter"
      />
      <v-btn
        color="primary"
        class="mr-4 mt-4"
        @click="verifyNotify()"
      >
        code zusenden
      </v-btn>
      <InputCode
        label="Verifizierungs code"
        counter="6"
        :value="hash"
        :setter="hashSetter"
      />
      <ButtonsSubmitCancel
        v-on:click-submit="verifyNext()"
        v-on:click-cancel="$emit('click-cancel')"
        :disabled="invalid"
      />
    </validation-observer>
  </v-form>
</template>

<script>
import { ValidationObserver } from 'vee-validate'
import { mapState, mapMutations, mapActions } from 'vuex'

import InputEmail from '@/components/InputEmail'
import InputPhoneNumber from '@/components/InputPhoneNumber'
import InputCode from '@/components/InputCode'
import ButtonsSubmitCancel from '@/components/ButtonsSubmitCancel'

export default {
  name: 'InputContactForm',
  components: {
    ValidationObserver,
    InputEmail,
    InputPhoneNumber,
    InputCode,
    ButtonsSubmitCancel,
  },
   data: () => ({
    invalid: null,
  }),
  computed: {
    ...mapState({
      channel: state => state.verifyContact.channel,
      email: state => state.verifyContact.email,
      phoneNumber: state => state.verifyContact.phoneNumber,
      hash: state => state.verifyContact.hash,
    }),
    channelValue: {
      get() {
        return this.channel
      },
      set(value) {
        this.channelSetter(value)
      },
    },
  },
  methods: {
    ...mapMutations({
      channelSetter: 'verifyContact/setChannel',
      emailSetter: 'verifyContact/setEmail',
      phoneNumberSetter: 'verifyContact/setPhoneNumber',
      hashSetter: 'verifyContact/setHash',
    }),
    ...mapActions({
      verifyNotify: 'verifyContact/verifyNotify',
      verifyCheck: 'verifyContact/verifyCheck',
    }),

    verifyNext() {
      this.verifyCheck()
      // todo: check for error
      this.$emit('click-submit')
    }
  },
}
</script>
