<template>
  <div>
    <v-alert type="warning" :value="true">
      <h3>ERROR</h3>
      <div>Seite wurde nicht gefunden.</div>
      <v-divider class="my-4"> </v-divider>
      <v-btn color="primary" @click="$router.push({ name: 'HomeView' })">
        zur Startseite
      </v-btn>
    </v-alert>
  </div>
</template>

<script>
export default {
  name: 'PageErrorView',
}
</script>
