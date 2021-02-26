<template>
  <v-container fluid>
    <v-select
      v-model="selected"
      :items="items"
      :label="label"
    ></v-select>
  </v-container>
</template>

<script>
export default {
  name: 'InputSelectBox',
  props: {
    value: {
      type: String,
      default: null
    },
    label: {
      type: String,
      required: true,
    },
    items: {
      type: Array,
      required: true,
    },
    setter: {
      type: Function,
      required: true,
    },
  },
  computed: {
    selected: {
      get () {
        return this.value
      },
      set (value) {
        this.setter(value)
      }
    }
  }
}
</script>