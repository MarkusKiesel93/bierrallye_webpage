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
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;"><strong>Regelwerk Bier-Rallye der JVP Irnfritz (September 2020)&nbsp;</strong></p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Das folgende Regelwerk ist von allen Teilnehmern vor Start der Bier-Rallye zu lesen und im mutma&szlig;lich n&uuml;chternen Zustand mit einer Unterschrift zu best&auml;tigen. S&auml;mtliche personenbezogenen Bezeichnungen sind geschlechtsneutral zu verstehen. S&auml;mtliche bierbezogenen Regelungen sind in gleicher Anwendung auf den Spritzwein zu beziehen.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;"><strong>&sect;1 Grundsatz</strong></p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Der Spa&szlig; sowie die Ehrung des Biers und des Spritzweins stehen im Vordergrund.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Jeder L&auml;ufer, der w&auml;hrend der Rallye seine Grenzen erkennt und den Lauf abbricht, ist l&ouml;blich zu erw&auml;hnen und gilt nicht als Verlier.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;"><strong>&sect;2 Haftung</strong></p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Jeder Teilnehmer ist f&uuml;r sein Handeln und den eventuell daraus entstehenden Folgen bzw. Sch&auml;den selbst verantwortlich. Sollte eine mutma&szlig;liche Sachbesch&auml;digung erfolgen, hat der Teilnehmer daf&uuml;r selbst aufzukommen, andernfalls wird Anzeige erstattet. Jeder Teilnehmer entbindet den Veranstalter (JVP Irnfritz) von jeglicher Haftung.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;"><strong>&sect;3 Teilnahmebedingungen</strong></p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Ale Teilnehmer m&uuml;ssen mindestens 16 Jahren alt sein. Nach oben hin wird keine Altersgrenze festgelegt um eine etwaige Altersdiskriminierung zu vermeiden. Seniorenteams sind herzlich willkommen! Zum &Uuml;berpr&uuml;fen des Alters werden im Anlassfall Ausweiskontrollen durchgef&uuml;hrt.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Um zur Teilnahme berechtigt zu sein, ist bei der Anmeldung das Startgeld in H&ouml;he von 50,00 &euro; Team (Bier und gemischte Kisten) bzw. von 45,00 &euro;/ Team (Spritzwein) an den Veranstalter zu bezahlen. Im Startgeld inbegriffen sind jeweils 16x Bier 0,33l bzw. 2l Wein + bei der Anmeldung angegebenes Beigetr&auml;nk enthalten. Gemischte Kisten enthalten 8x Bier 0,33l + 1l Wein + Beigetr&auml;nk.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Jeder Teilnehmer muss vor dem Start im Vollbesitz seiner geistigen Kr&auml;fte sein. Offensichtlich bereits betrunkene Personen sowie Teilnehmer, die vor dem Start ein allseits verhasstes Biermischgetr&auml;nk namens &quot;Radler&ldquo; konsumieren, wird die Teilnahme am Lauf nicht gew&auml;hrt.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;"><strong>&sect;4 Streckenregeln</strong></p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Das Versch&uuml;tten oder &bdquo;sich-nochmal-durch-den-Kopf-gehen-lassen&ldquo; der jeweiligen wegbegleitenden Fl&uuml;ssigkeit w&auml;hrend der Rallye, wird mit Zusatzminuten oder im Extremfall mit Laufdisqualifikation geahndet.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Als Waldviertler ehren wir unsere W&auml;lder! Deshalb wird eine vors&auml;tzliche Verschmutzung dieser mit Disqualifikation geahndet:</p>
        <ul>
            <li>
                <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Rauchen ist ausschlie&szlig;lich an den auf der Strecke befindlichen Stationen sowie im Bereich des Starts/ Ziels am Sportplatz erlaubt &ndash; dort werden auch entsprechende Beh&auml;ltnisse f&uuml;r die Entsorgung bereitgestellt.</p>
            </li>
            <li>
                <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Alle Kisten, Flaschen sowie Kapseln sind beim Erreichen des Ziels an die Veranstalter zu &uuml;bergeben.</p>
            </li>
            <li>
                <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Die Erledigung der kleinen Notdurft ist in hausverst&auml;ndlichem Abstand zur Rallye-Strecke erlaubt, gr&ouml;&szlig;ere Gesch&auml;fte sind nach Beendigung des Laufes zu erledigen.</p>
            </li>
        </ul>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;"><strong>&sect;5 Fotografie und Videos</strong></p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Mit ihrer Unterschrift erteilen alle Teilnehmer dem Veranstalter die Erlaubnis Foto- und Videomaterial der Veranstaltung anzufertigen und diese zu ver&ouml;ffentlichen, um die erlebten Eindr&uuml;cke der Bier-Rallye 2020 f&uuml;r die Nachwelt festzuhalten.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;"><strong>&sect;6 Vorschriften bzgl. der aktuell g&uuml;ltigen Covid19-Verordnung (&sect;10 Veranstaltungen)&nbsp;</strong></p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Zur Steuerung der Besucherstr&ouml;me werden die Teams gestaffelt zu jeweils f&uuml;nf Teams (= zehn Personen) starten.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Um die Hygienevorschriften einzuhalten, werden an den Eing&auml;ngen, bei den Sanit&auml;ranlagen bei der Essens- und Getr&auml;nkeausgabe sowie bei den Stationen auf der Strecke Desinfektionsmittelspender aufgestellt. Gut sichtbar angebrachte Schilder weisen auf die Einhaltung des Mindestabstands sowie auf das regelm&auml;&szlig;ige H&auml;ndewaschen und Desinfizieren hin. Die WC-Anlagen sind einzeln zu betreten und werden w&auml;hrend der Veranstaltung regelm&auml;&szlig;ig desinfiziert.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Die Spiele an den Stationen sind so aufgebaut, dass der Mindestabstand problemlos eingehalten werden kann und die an den Stationen verwendeten Materialien zum gr&ouml;&szlig;ten Teil nicht von mehreren Personen ber&uuml;hrt werden m&uuml;ssen. Sollte letzteres doch der Fall sein, werden betreffende Materialen regelm&auml;&szlig;ig von den Veranstaltern desinfiziert. Die Teilnehmer werden au&szlig;erdem dazu angehalten sich beim Ankommen und Verlassen jeder Station die H&auml;nde zu desinfizieren und einer entsprechenden Aufforderung der Veranstalter dazu Folge zu leisten.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Im Falle des Auftretens einer Sars-Cov-2-Infektion unter den Teilnehmern, Besuchern oder Veranstaltern wird die Bezirkshauptmannschaft Horn informiert. Um eine l&uuml;ckenlose R&uuml;ckverfolgung der potentiell infizierten Teilnehmer zu gew&auml;hrleisten, wird eine Besucher- und Personalliste mit allen anwesenden Personen erstellt. Die Angabe der Daten erfolgt datenschutzkonform und somit auf freiwilliger Basis.</p>
        <p style="margin-bottom: 0.35cm;line-height: 115%;text-align: left;background: transparent;">Personen, die die oben genannten Ma&szlig;nahmen missachten, werden von der Veranstaltung ausgeschlossen. Den Anweisungen der Veranstalter ist demnach unbedingt Folge zu leisten.</p>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-btn color="primary" @click="dialog = false">
          OK
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: 'DialogGameRules',
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
