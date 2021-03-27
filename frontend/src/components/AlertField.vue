<template>
  <v-alert :type="type" :value="value" :dismissible="dismissible">
      {{ message }}
  </v-alert>
</template>

<script>
export default {
  name: 'AlertField',
  props: {
    type: {
      type: String,
      required: true,
    },
    value: {
      type: Boolean,
      default: false,
    },
    dismissible: {
      type: Boolean,
      default: false,
    },
    message: {
      type: String,
      required: true,
    },
  },
}
</script>
