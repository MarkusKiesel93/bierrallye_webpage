<template>
  <v-container fluid>
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
  </v-container>
</template>

<script>
import InputEmail from '@/components/InputEmail'
import InputPhoneNumber from '@/components/InputPhoneNumber'

export default {
  name: 'InputContact',
  components: {
    InputEmail,
    InputPhoneNumber,
  },
  props: {
    channel: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
    },
    phoneNumber: {
      type: String,
      required: true,
    },
    channelSetter: {
      type: Function,
      required: true,
    },
    emailSetter: {
      type: Function,
      required: true,
    },
    phoneNumberSetter: {
      type: Function,
      required: true,
    },
  },
  computed: {
    channelValue: {
      get() {
        return this.channel
      },
      set(value) {
        this.channelSetter(value)
      },
    },
  },
}
</script>
