<template>
  <v-container fluid>
    <v-btn
      color="primary"
      class="mr-4 mt-4"
      :disabled="disabled"
      @click="$emit('click-next')"
    >
      {{ nextLabel }}
    </v-btn>
    <v-btn class="mt-4" @click="$emit('click-back')">
      {{ backLabel }}
    </v-btn>
  </v-container>
</template>

<script>
export default {
  name: 'ButtonsNextBack',
  props: {
    disabled: {
      type: Boolean,
      default: false,
    },
    nextLabel: {
      type: String,
      default: 'Weiter',
    },
    backLabel: {
      type: String,
      default: 'Zurück',
    },
  },
}
</script>
