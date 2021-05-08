<template>
  <v-dialog
    v-model="dialog"
    scrollable
    max-width="1000"
    :fullscreen="fullscreen"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn v-bind="attrs" v-on="on" color="primary" class="ma-1">
        Datenschutzbestimmungen
      </v-btn>
    </template>
    <v-card>
      <h2 class="pt-4 text-center"> Datenschutzerkl&auml;rung Bier-Rallye 2021 </h2> 
      <h3 class="pb-4 text-center"> gem&auml;&szlig; der Datenschutz-Grundverordnung (EU) 2016/679 </h3>
      <v-card-text>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:6.0pt;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;text-align:center;'><strong><span style="font-size:16px;"></span></strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>&nbsp;</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>A. Name und Kontaktdaten des f&uuml;r die Verarbeitung Verantwortlichen:</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>JVP Irnfritz</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Vereinsobmann: Daniel Siegl</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Telefonnummer: 0664/2527279</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>B. Datenverarbeitungen/Datenverarbeitungszwecke:</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Fotografie und Videos:</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Zum Zwecke des Marketings beh&auml;lt sich der Veranstalter vor, Foto- und Videomaterial von den Teilnehmern w&auml;hrend der Bierrallye anzufertigen und auf den Social-Media-Kan&auml;len der JVP Irnfritz (Facebook und Instagram), zu posten.&nbsp;</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Contact-Tracing:</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Zur Erm&ouml;glichung eines l&uuml;ckenlosen Contact-Tracings im Falle des Auftretens einer Sars-Cov2-Infektion unter den teilnehmenden Personen innerhalb eines Zeitraums von 3 Tagen nach der Veranstaltung, werden folgende personenbezogene Daten schriftlich aufgezeichnet: Vorname, Nachname und Mobiltelefonnummer des Teilnehmers. Tritt eine Covid-19-Infektion bei einer teilnehmenden bzw. einer helfenden Person im kritischen Zeitraum auf, wird die Bezirkshauptmannschaft Horn umgehend informiert und die Teilnehmerliste an die Beh&ouml;rde weitergegeben.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Kontaktformular/ Anmeldeformular</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Nach Absenden des Kontaktformulars &uuml;ber die Website (bierrallye-irnfritz.at) erfolgt eine Verarbeitung der von Ihnen eingegebenen personenbezogenen Daten zum Zweck der Bearbeitung der Anmeldung zur Veranstaltung auf Grundlage, der durch das Absenden des Formulars erteilten Daten-Bereitstellung. Des Weiteren dienen Ihre Daten zur Kontaktaufnahme in Form von News&amp;Updated, Direktmarketing und Werbung und Erinnerungsnachrichten in Bezug auf die auf dieser Website pr&auml;sentierten Veranstaltung. Es besteht keine gesetzliche oder vertragliche Bereitstellungsverpflichtung. Die Nichtbereitstellung hat lediglich zur Folge, dass eine Anmeldung nicht &uuml;bermittelt wird und daher nicht bearbeitet werden kann.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Es besteht das Recht, Ihre Einwilligung jederzeit durch schriftliche Mitteilung zu widerrufen, ohne dass die Rechtm&auml;&szlig;igkeit, der aufgrund der Einwilligung bis zum Widerruf erfolgten Verarbeitung ber&uuml;hrt wird. Es erfolgt eine Weiterverarbeitung der Daten, welche mit dem urspr&uuml;nglichen Verarbeitungszweck vereinbar ist, auf derselben Rechtsgrundlage zum Zweck des Direktmarketings in nicht einwilligungspflichtigen Formen, wie dem adressierten postalischen Versand von Werbung, bis auf Widerspruch.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Sie haben das Recht, der Verwendung Ihrer personenbezogenen Daten zum Zweck der Direktwerbung jederzeit durch schriftliche Mitteilung zu widersprechen. Im Fall des Widerspruchs werden Ihre personenbezogenen Daten nicht mehr zum Zweck der Direktwerbung verarbeitet und aus unseren Systemen gel&ouml;scht.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><strong><u>C. Detailangaben zur Datenverarbeitung:</u></strong></p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u><span style="text-decoration:none;">&nbsp;</span></u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Rechtsgrundlage:</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Die Teilnehmer sind verpflichtet, den Teilnahmebedingungen der Bierrallye vor Beginn der Veranstaltung mit ihrer Unterschrift zuzustimmen. Die in diesem Regelwerk enthaltenen &sect;&sect; 5 und 6 beinhalten die f&uuml;r die Anfertigung des Bildmaterials, der Verwendung personenbezogener Daten, die &uuml;ber das auf der Website integrierte Kontaktformular zur Verf&uuml;gung gestellt werden und den Bestimmungen zum Contact-Tracing erforderlichen Einverst&auml;ndniserkl&auml;rungen.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Speicher- und Aufbewahrungsfristen:</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Als Kommunikationsdaten unterliegen die von den Teilnehmern angegebenen Daten (Name, E-Mail-Adresse und Telefonnummer) der Aufbewahrungsfrist von 7 Jahren. Nach Ablauf der Frist erfolgt eine routinem&auml;&szlig;ige L&ouml;schung der Daten.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Schutz der personenbezogenen Daten:</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Der Veranstalter verpflichtet sich dazu, sorgsam mit den personenbezogenen Daten der Teilnehmer umzugehen und diese au&szlig;er f&uuml;r die in Punkt B angef&uuml;hrten Zwecken nicht zu verwenden oder weiterzugeben.&nbsp;</p>
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
  name: 'DialogDataProtection',
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
