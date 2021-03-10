<template>
  <v-dialog
    v-model="dialog"
    scrollable
    max-width="1000"
    :fullscreen="fullscreen"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" color="primary" class="ma-1">
        Teilnahmebedingung
      </v-btn>
    </template>
    <v-card>
      <v-card-title>
        Teilnahmebedingung
      </v-card-title>
      <v-card-text>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Eget arcu dictum
        varius duis at consectetur lorem. A pellentesque sit amet porttitor eget
        dolor morbi. Ut faucibus pulvinar elementum integer enim neque volutpat
        ac. Mattis molestie a iaculis at erat pellentesque adipiscing commodo.
        Fermentum posuere urna nec tincidunt praesent semper feugiat nibh. Massa
        massa ultricies mi quis. Porttitor eget dolor morbi non arcu risus quis
        varius quam. Morbi tristique senectus et netus et malesuada fames ac
        turpis. Et leo duis ut diam quam nulla porttitor massa. Sit amet purus
        gravida quis blandit. Auctor urna nunc id cursus. Tempus urna et
        pharetra pharetra. Amet consectetur adipiscing elit ut aliquam.
        Consequat id porta nibh venenatis cras sed felis. In fermentum et
        sollicitudin ac orci phasellus egestas.
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn color="primary" @click="dialog = false">
          Schließen
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'GameRulesDialog',
  data: () => ({
    dialog: false,
  }),
  computed: {
    fullscreen: function() {
      if (this.$vuetify.breakpoint.xsOnly) {
        return true
      } else {
        return false
      }
    },
  },
}
</script>
