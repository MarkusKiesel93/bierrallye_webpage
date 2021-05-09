<template>
  <div>
    <v-card>
      <h2 class="py-8 text-center"> Infos </h2>

      <v-card-text>
        <h4> Liebe Freunde des Hopfens und der Rebe! </h4>
        <p>
          Die legendäre Irnfritzer Bierrallye geht (voraussichtlich) am 19.06.2021 am Sportplatz Irnfritz in die 3. Runde.
        </p>
        <h4> Hardfacts: </h4>
        <p>
          <ul>
            <li>8 Stationen auf rund 5 km</li>
            <li>2 Personen pro Team</li>
            <li>Startgeld €50,00 / Team</li>
            <li>pro Person 8x Bier 0,33l bzw. 1l Wein + gewünschtes Beigetränk</li>
            <li>gemischte Kisten möglich</li>
            <li>Wegbegleiter</li>
            <ul>
              <li>Bier</li>
              <li>Spritzer-Weiß</li>
              <li>Alm-Weß</li>
              <li>Frucade-Weiß</li>
              <li>Cola-Weiß</li>
              <li>Radler (Achtung: Aufpreis € 200,00 !!)</li>
            </ul>
            <li> Anmeldezeit (vor Ort) </li>
            <ul>
              <li>Block A: 13:00</li>
              <li>Block B: 13:30</li>
              <li>Block C: 14:00</li>
              <li>Block D: 14:30</li>
              <li>Block E: 15:00</li>
              <li>Block F: 15:30</li>
            </ul>
            
            <li>verkleidete Teams bekommen einen Spritzer-Gutschein pro Person</li>
          </ul>
        </p>

        <p>
          Die Veranstaltung wird unter Berücksichtigung der aktuellen Lage und damit auch nach den Vorschriften der Regierung durchgeführt. <br>
          Siehe: <router-link :to="{ name: 'CovidConceptView' }"> Covid-19 Präventionskonzept </router-link>
        </p>

        <p>
          Wenn dir alles klar ist, ab zur Anmeldung <br>
          Wir freuen uns auf Euer Kommen!
        </p>
      
      </v-card-text>
    </v-card>
    <v-card>
      <h2 class="py-4 text-center"> Anmeldung & Abmeldung </h2>

      <v-card-text>
        <p>Freie Plätze: {{ placesFree }} Teams</p>
        <p>
          Wir bitten um euer Verständns, dass die Bierrallye, wenn notwendigt, auch kurzfristig abgesagt werden kann! <br>
          Was uns abhalten kann: Wetter, Corona, Atomkrieg, Konkurs der Brauerei
        </p>
        <p>
          Bitte vergesst nicht euch abzumelden wenn ihr doch nicht kommen könnt, damit wir den Platz an ein wartendes Team vergeben können. <br>
          Bei Fragen oder Problemen meldet euch gerne per Email unter <a href="mailto:bierrallye.irnfritz@gmail.com">bierrallye.irnfritz@gmail.com</a> 
        </p>
      </v-card-text>

      <v-card-actions>
        <v-btn v-if="placesFree>0" color="primary" class="my-4 mr-4" :to="{ name: 'RegisterView' }">
          Anmelden
        </v-btn>
        <v-btn class="my-4" :to="{ name: 'DeregisterView' }">
          Abmelden
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
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
      requestPlacesFree: 'requestPlacesFree',
    }),
  },
  created: function() {
    this.requestPlacesFree()
  },
}
</script>
