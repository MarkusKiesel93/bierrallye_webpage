<template>
  <v-container fluid>
    <v-btn
      color="primary"
      class="mr-4 mt-4"
      :disabled="disabled"
      @click="$emit('click-submit')"
    >
      {{ submitLabel }}
    </v-btn>
    <v-btn class="mt-4" @click="$emit('click-cancel')">
      {{ cancelLabel }}
    </v-btn>
  </v-container>
</template>

<script>
export default {
  name: 'ButtonsSubmitCancel',
  props: {
    disabled: {
      type: Boolean,
      default: false,
    },
    submitLabel: {
      type: String,
      default: 'ok',
    },
    cancelLabel: {
      type: String,
      default: 'zurück',
    },
  },
}
</script>
