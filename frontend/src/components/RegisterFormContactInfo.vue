<template>
  <v-form>
    <div>
      <validation-observer ref="observer" v-slot="{ invalid }">
        <InputContact
          :channel="channel"
          :email="email"
          :phoneNumber="phoneNumber"
          :channelSetter="channelSetter"
          :emailSetter="emailSetter"
          :phoneNumberSetter="phoneNumberSetter"
        />
        <v-btn
          color="primary"
          class="mr-4 mt-4"
          @click="verifyNotify()"
          :disabled="invalid"
        >
          code zusenden
        </v-btn>
        <h6 class="text-justify"> *) Mit click auf CODE ZUSENDEN stimmen Sie zu, dass wir Ihnen einen einmaligen Code zur Verifizierung zusenden. </h6>
      </validation-observer>
    </div>
    <div>
      <validation-observer ref="observer" v-slot="{ invalid }">
        <InputCode
          label="Verifizierungs code"
          counter="6"
          :value="hash"
          :setter="hashSetter"
        />
        <AlertField
          :type="alertType"
          :value="alert"
          :message="alertMessage"
        />
        <LoadingCircle :show="loading" />
        <ButtonsSubmitCancel
          v-on:click-submit="verifyNext()"
          v-on:click-cancel="$emit('click-cancel')"
          :disabled="invalid"
          :submitLabel="submitLabel"
        />
      </validation-observer>
    </div>
  </v-form>
</template>

<script>
import { ValidationObserver } from 'vee-validate'
import { mapState, mapMutations, mapActions } from 'vuex'

import InputContact from '@/components/InputContact'
import InputCode from '@/components/InputCode'
import ButtonsSubmitCancel from '@/components/ButtonsSubmitCancel'
import AlertField from '@/components/AlertField'
import LoadingCircle from '@/components/LoadingCircle'

export default {
  name: 'RegisterFormContactInfo',
  components: {
    ValidationObserver,
    InputContact,
    InputCode,
    ButtonsSubmitCancel,
    AlertField,
    LoadingCircle,
  },
   data: () => ({
    invalid: null,
    submitLabel: 'Verifizieren'
  }),
  computed: {
    ...mapState({
      channel: state => state.verifyContact.channel,
      email: state => state.verifyContact.email,
      phoneNumber: state => state.verifyContact.phoneNumber,
      hash: state => state.verifyContact.hash,
      success: state => state.verifyContact.success,
      loading: state => state.verifyContact.loading,
      alert: state => state.verifyContact.alert,
      alertType: state => state.verifyContact.alertType,
      alertMessage: state => state.verifyContact.alertMessage,
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
      if (this.success) {
        this.$emit('click-submit')
      } else {
        this.verifyCheck()
      }
    }
  },
  watch: {
    success() {
      this.submitLabel = 'Weiter'
    }
  }
}
</script>
