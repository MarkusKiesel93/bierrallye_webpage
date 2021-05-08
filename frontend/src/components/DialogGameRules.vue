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
      <h2 class="py-4 text-center"> Teilnahmebedingungen Bier-Rallye der JVP Irnfritz (Juni 2021) </h2>
      <v-card-text>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>Die folgenden Teilnahmebedingungen sind von allen Teilnehmern vor dem Start der Bier-Rallye zu lesen und im mutma&szlig;lich n&uuml;chternen Zustand mit einer Unterschrift zu best&auml;tigen. S&auml;mtliche personenbezogenen Bezeichnungen sind geschlechtsneutral zu verstehen. S&auml;mtliche bierbezogenen Regelungen sind in gleicher Anwendung auf den Spritzwein zu beziehen.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>&sect; 1 Grundsatz</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>Der Spa&szlig; sowie die Ehrung des Biers und des Spritzweins stehen im Vordergrund.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>Jeder L&auml;ufer, der w&auml;hrend der Rallye seine Grenzen erkennt und den Lauf abbricht, ist l&ouml;blich zu erw&auml;hnen und gilt nicht als Verlierer.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>&sect; 2 Haftung</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;text-align:justify;'>Jeder Teilnehmer ist f&uuml;r sein Handeln und den eventuell daraus entstehenden Folgen bzw. Sch&auml;den selbst verantwortlich. Sollte eine mutma&szlig;liche Sachbesch&auml;digung erfolgen, hat der Teilnehmer daf&uuml;r selbst aufzukommen, andernfalls wird Anzeige erstattet. Jeder Teilnehmer entbindet den Veranstalter (JVP Irnfritz) von jeglicher Haftung. Die Absolvierung der Rallye sowie die damit verbundene Konsumation von Alkohol erfolgt auf eigene Gefahr.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>&sect; 3 Teilnahmebedingungen</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Alle Teilnehmer m&uuml;ssen mindestens 16 Jahren alt sein. Nach oben hin wird keine Altersgrenze festgelegt, um eine etwaige Altersdiskriminierung zu vermeiden. Seniorenteams sind herzlich willkommen, werden aber auch nach mehrmaliger Anfrage nicht mit mehr oder weniger Alkohol an den Start geschickt als die j&uuml;ngeren Teams! Die JVP Irnfritz vertraut hier auf die Erfahrung, Weisheit und Selbsteinsch&auml;tzung der Teilnehmer. Zum &Uuml;berpr&uuml;fen des Alters werden im Anlassfall Ausweiskontrollen durchgef&uuml;hrt.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Um zur Teilnahme berechtigt zu sein, ist bei der Anmeldung das Startgeld in H&ouml;he von 50,00 &euro; pro Team (Bier, Spritzer und gemischte Kisten) an den Veranstalter zu bezahlen. Im Startgeld inbegriffen sind jeweils 16x Bier 0,33 l bzw. 2 l Wein + bei der Anmeldung angegebenes Beigetr&auml;nk. Gemischte Kisten enthalten 8x Bier 0,33l + 1l Wein + Beigetr&auml;nk.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Jeder Teilnehmer muss vor dem Start im Vollbesitz seiner geistigen Kr&auml;fte sein. Offensichtlich bereits betrunkene Personen sowie Teilnehmern, die vor dem Start ein allseits verhasstes Biermischgetr&auml;nk namens &quot;Radler&ldquo; konsumieren, wird die Teilnahme am Lauf nicht gestattet!</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>&sect; 4 Streckenregeln</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Das Versch&uuml;tten oder &bdquo;sich-nochmal-durch-den-Kopf-gehen-lassen&ldquo; der jeweiligen wegbegleitenden Fl&uuml;ssigkeit w&auml;hrend der Rallye, wird mit Zusatzminuten oder im Extremfall mit Laufdisqualifikation geahndet.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Als Waldviertler ehren wir unsere W&auml;lder! Deshalb wird eine vors&auml;tzliche Verschmutzung dieser mit Disqualifikation geahndet:</p>
        <ul style="list-style-type: disc;">
          <li>Rauchen ist ausschlie&szlig;lich an den auf der Strecke befindlichen Stationen sowie im Bereich des Starts/ Ziels am Sportplatz erlaubt &ndash; dort werden auch entsprechende Beh&auml;ltnisse f&uuml;r die Entsorgung bereitgestellt.</li>
          <li>Alle Kisten, Flaschen sowie Kapseln sind beim Erreichen des Ziels an die Veranstalter zu &uuml;bergeben.</li>
          <li>Die Erledigung der kleinen Notdurft ist in hausverst&auml;ndlichem Abstand zur Rallye-Strecke erlaubt, gr&ouml;&szlig;ere Gesch&auml;fte sind nach Beendigung des Laufes zu erledigen oder in mindestens 1m Tiefe im Wald zu vergraben.</li>
        </ul>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>&sect; 5 Fotografie, Videos und Verarbeitung personenbezogener Daten</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Mit ihrer Unterschrift erteilen alle Teilnehmer dem Veranstalter im Sinne der DSGVO die Erlaubnis, Foto- und Videomaterial w&auml;hrend der Veranstaltung anfertigen und auf Social-Media-Plattformen ver&ouml;ffentlichen zu d&uuml;rfen, um die erlebten Eindr&uuml;cke der Bier-Rallye 2021 f&uuml;r die Nachwelt festzuhalten und die Veranstaltung f&uuml;r die n&auml;chsten Jahre bewerben zu k&ouml;nnen.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Zur Anmeldung wird ein Online-Kontaktformular auf der Website &bdquo;bierrallye-irnfritz.at&ldquo; zur Verf&uuml;gung gestellt, mittels welchem personenbezogene Daten (Name, Telefonnummer und E-Mail Adresse) gespeichert und f&uuml;r die folgende Kommunikation verwendet wird. Die Teilnehmer haben das Recht, der Verwendung Ihrer personenbezogenen Daten zum Zweck der Direktwerbung jederzeit durch schriftliche Mitteilung zu widersprechen. Genauere Informationen dazu k&ouml;nnen der Datenschutzerkl&auml;rung unter bierrallye-irnfritz.at entnommen werden.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>&sect; 6 Vorschriften im Zusammenhang mit Covid 19</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Je nach aktueller Rechtslage im Sinne des &sect; 10 COVID-19-Ma&szlig;nahmengesetz trifft der Veranstalter alle vorgeschriebenen Ma&szlig;nahmen zur Pr&auml;vention vor Corona-Infektionen und erarbeitet zum bestm&ouml;glichen Schutz seiner Teilnehmer und Helfer ein Covid-19-Pr&auml;ventionskonzept.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Zur Steuerung der Besucherstr&ouml;me werden die Teams gestaffelt zu jeweils f&uuml;nf Teams (= zehn Personen) starten.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Um die Hygienevorschriften einzuhalten, werden an den Eing&auml;ngen, bei den Sanit&auml;ranlagen bei der Essens- und Getr&auml;nkeausgabe sowie bei den Stationen auf der Strecke Desinfektionsmittelspender aufgestellt. Gut sichtbar angebrachte Schilder weisen auf die Einhaltung des Mindestabstands sowie auf das regelm&auml;&szlig;ige H&auml;ndewaschen und Desinfizieren hin. Die WC-Anlagen sind einzeln zu betreten und werden w&auml;hrend der Veranstaltung regelm&auml;&szlig;ig desinfiziert.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Die Spiele an den Stationen sind so aufgebaut, dass der Mindestabstand problemlos eingehalten werden kann und die an den Stationen verwendeten Materialien nicht von mehreren Personen ber&uuml;hrt werden m&uuml;ssen. Sollte letzteres doch der Fall sein, werden betreffende Materialen regelm&auml;&szlig;ig von den Veranstaltern desinfiziert. Die Teilnehmer werden au&szlig;erdem dazu angehalten sich beim Ankommen und Verlassen jeder Station die H&auml;nde zu desinfizieren und einer entsprechenden Aufforderung der Veranstalter dazu Folge zu leisten.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Im Falle des Auftretens einer Sars-Cov-2-Infektion unter den Teilnehmern, Besuchern oder Veranstaltern wird die Bezirkshauptmannschaft Horn informiert. Um eine l&uuml;ckenlose R&uuml;ckverfolgung der potenziell infizierten Teilnehmer zu gew&auml;hrleisten, wird eine Besucher- und Personalliste mit allen anwesenden Personen erstellt. Die Angabe der personenbezogenen Daten erfolgt datenschutzkonform auf freiwilliger Basis (mit Zustimmung der Teilnehmer und Helfer).</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>Personen, die die oben genannte Ma&szlig;nahmen missachten, werden von der Veranstaltung ausgeschlossen. Den Anweisungen der Veranstalter ist demnach unbedingt Folge zu leisten.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
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
