<template>
  <v-container fluid>
    <v-alert
      :type='type'
      :value="value"
      :dismissible='dismissible'
    >
      <v-row>
        <div> {{ row1 }} </div>
      </v-row>
      <v-row>
        <div> {{ row2 }} </div>
      </v-row>
    </v-alert>
  </v-container>
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
      default: true,
    },
    row1: {
      type: String,
      required: true,
    },
    row2: {
      type: String,
      default: null,
    }
  },
}
</script>