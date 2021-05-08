<template>
  <v-app>
    <v-app-bar app color="primary">
      <router-link :to="{ name: 'HomeView' }">
        <v-app-bar-title class="white--text">
          Bierrallye Irnfritz 2021
        </v-app-bar-title>
      </router-link>
      <v-spacer> </v-spacer>
      <router-link :to="{ name: 'HomeView' }">
        <v-icon large color="white"> mdi-home</v-icon>
      </router-link>
    </v-app-bar>
    <!-- Header -->
    <ImageCarousel :images="headerImages" :height="headerHeight" :cycle="true">
    </ImageCarousel>

    <!-- Content -->
    <v-main class="pt-6">
      <v-layout justify-center align-start>
        <v-container fluid class="main-container px-0">
          <router-view></router-view>
        </v-container>
      </v-layout>
    </v-main>

    <!-- Footer -->
    <v-footer app>
      <!-- name and year -->
      <p class="ma-0 pa-0">
        <strong> &copy; {{ this.ccName }} </strong> - {{ this.year }}
      </p>
      <v-spacer></v-spacer>
      <!-- link to impressum -->
      <router-link :to="{ name: 'LegalNoticeView' }" active-class>
        <div>Impressum</div>
      </router-link>
    </v-footer>
  </v-app>
</template>

<script>
import { mapGetters } from 'vuex'

import ImageCarousel from '@/components/ImageCarousel'


export default {
  name: 'App',
  components: {
    ImageCarousel,
  },
  data: () => ({
    ccName: 'Jugend Irnfritz',
    year: new Date().getFullYear(),
    dialog: false,
  }),
  computed: {
    ...mapGetters({
      headerImages: 'images/headerImages',
    }),
    headerHeight () {
      switch (this.$vuetify.breakpoint.name) {
        case 'xs': return 240
        case 'sm': return 300
        case 'md': return 400
        case 'lg': return 500
        case 'xl': return 600
        default: return 300
      }
    },
  },
}
</script>

<style scoped>
a {
  text-decoration: none;
}

.main-container {
  max-width: 1000px;
}
</style>
