<template>
  <v-container fluid>
    <v-row v-for="item in items" :key="item.label" :item="item">
      <v-col cols="12" sm="4">
        <strong> {{ item.label }}: </strong>
      </v-col>
      <v-col offset="1" offset-sm="0">
        <v-row>
          <p>{{ item.row1 }}</p>
        </v-row>
        <v-row v-if="item.row2">
          <p>{{ item.row2 }}</p>
        </v-row>
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
    },
  },
}
</script>
