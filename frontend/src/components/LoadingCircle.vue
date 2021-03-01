<template>
  <v-container
    fluid
    v-if="show"
  >
    <v-progress-circular
      :size="30"
      color="primary"
      indeterminate
    ></v-progress-circular>
  </v-container>
</template>

<script>
export default {
  name: 'LoadingCircle',
  props: {
    show: {
      type: Boolean,
      required: true
    }
  }
}
</script>