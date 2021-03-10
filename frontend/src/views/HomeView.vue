<template>
  <v-card>
    <v-card-title>
      Informationen
    </v-card-title>

    <v-card-text>
      <p>
        Wann: 01.08.2021
      </p>
      <p>
        Wo: Sportplatz Irnfritz
      </p>
      <p>Freie Plätze: {{ placesFree }}</p>
      <p>
        Beschreibung: Lorem ipsum dolor sit amet, consectetur adipiscing elit,
        sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Eget
        arcu dictum varius duis at consectetur lorem. A pellentesque sit amet
        porttitor eget dolor morbi. Ut faucibus pulvinar elementum integer enim
        neque volutpat ac. Mattis molestie a iaculis at erat pellentesque
        adipiscing commodo. Fermentum posuere urna nec tincidunt praesent semper
        feugiat nibh. Massa massa ultricies mi quis. Porttitor eget dolor morbi
        non arcu risus quis varius quam. Morbi tristique senectus et netus et
        malesuada fames ac turpis. Et leo duis ut diam quam nulla porttitor
        massa. Sit amet purus gravida quis blandit. Auctor urna nunc id cursus.
        Tempus urna et pharetra pharetra. Amet consectetur adipiscing elit ut
        aliquam. Consequat id porta nibh venenatis cras sed felis. In fermentum
        et sollicitudin ac orci phasellus egestas.
      </p>
    </v-card-text>

    <v-card-actions>
      <v-btn color="primary" class="my-4 mr-4" :to="{ name: 'RegisterView' }">
        Anmelden
      </v-btn>
      <v-btn class="my-4" :to="{ name: 'DeregisterView' }">
        Abmelden
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import { mapState, mapActions } from 'vuex'

export default {
  name: 'HomeView',
  computed: {
    ...mapState({
      placesFree: state => state.placesFree,
    }),
  },
  methods: {
    ...mapActions({
      getPlacesFree: 'getPlacesFree',
    }),
  },
  created: function() {
    this.getPlacesFree()
  },
}
</script>
