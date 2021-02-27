<template>
  <v-container fluid>
    <v-row
      v-for="item in items"
      :key="item.label"
      :item="item">
      <v-col cols=3>
        <strong> {{ item.label }}: </strong>
      </v-col>
      <v-col>
        <p> {{ item.value }} </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'InfoItems',
  props: {
    items: {
      type: Array,
      required: true,
    }
  }
}
</script>