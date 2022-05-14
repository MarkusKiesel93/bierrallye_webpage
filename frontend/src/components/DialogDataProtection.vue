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
      <h2 class="pt-4 text-center"> Datenschutzerkl&auml;rung Bier-Rallye 2022 </h2> 
      <h3 class="pb-4 text-center"> gem&auml;&szlig; der Datenschutz-Grundverordnung (EU) 2016/679 </h3>
      <v-card-text>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>&nbsp;</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>A. Name und Kontaktdaten des f&uuml;r die Verarbeitung Verantwortlichen:</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>JVP Irnfritz</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Vereinsobmann: Simon Hummel</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Telefonnummer: 0650/2203935</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:10.0pt;margin-left:0cm;line-height:115%;font-size:15px;font-family:"Calibri",sans-serif;'><strong>B. Datenverarbeitungen/Datenverarbeitungszwecke:</strong></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Fotografie und Videos:</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Zum Zwecke des Marketings beh&auml;lt sich der Veranstalter vor, Foto- und Videomaterial von den Teilnehmern w&auml;hrend der Bierrallye anzufertigen und auf den Social-Media-Kan&auml;len der JVP Irnfritz (Facebook und Instagram), zu posten.&nbsp;</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Kontaktformular/ Anmeldeformular</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Nach Absenden des Kontaktformulars &uuml;ber die Website (bierrallye-irnfritz.at) erfolgt eine eingegrenzte Verarbeitung der von Ihnen eingegebenen personenbezogenen Daten zum Zweck der Bearbeitung der Anmeldung/Abmeldung zur Veranstaltung sowie einer einmaligen Erinnerung auf Grundlage, der durch das Absenden des Formulars erteilten Daten-Bereitstellung. Es besteht keine gesetzliche oder vertragliche Bereitstellungsverpflichtung. Die Nichtbereitstellung hat lediglich zur Folge, dass eine Anmeldung nicht &uuml;bermittelt wird und daher nicht bearbeitet werden kann.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Es besteht das Recht, Ihre Einwilligung jederzeit durch schriftliche Mitteilung zu widerrufen, ohne dass die Rechtm&auml;&szlig;igkeit, der aufgrund der Einwilligung bis zum Widerruf erfolgten Verarbeitung ber&uuml;hrt wird. Im Fall des Widerspruchs werden Ihre personenbezogenen Daten nicht mehr f&uuml;r oben angef&uuml;hrte Zwecke verwendet und aus unseren Systemen gel&ouml;scht.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><strong><u>C. Detailangaben zur Datenverarbeitung:</u></strong></p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u><span style="text-decoration:none;">&nbsp;</span></u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Rechtsgrundlage:</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Die Teilnehmer sind verpflichtet, den Teilnahmebedingungen der Bierrallye vor Beginn der Veranstaltung mit ihrer Unterschrift zuzustimmen. Die in diesem Regelwerk enthaltenen &sect;&sect; 5 und 6 beinhalten die f&uuml;r die Anfertigung des Bildmaterials, der Verwendung personenbezogener Daten, die &uuml;ber das auf der Website integrierte Kontaktformular zur Verf&uuml;gung gestellt werden und den Bestimmungen zum Contact-Tracing erforderlichen Einverst&auml;ndniserkl&auml;rungen.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Speicher- und Aufbewahrungsfristen:</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Als Kommunikationsdaten unterliegen die von den Teilnehmern angegebenen Daten (Name, E-Mail-Adresse und Telefonnummer) der Aufbewahrungsfrist von 7 Jahren. Nach Ablauf der Frist erfolgt eine routinem&auml;&szlig;ige L&ouml;schung der Daten.</p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>&nbsp;</p>
        <p style='margin-top:0.5cm;margin-right:0.5cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'><u>Schutz der personenbezogenen Daten:</u></p>
        <p style='margin-top:0cm;margin-right:0cm;margin-bottom:0cm;margin-left:0cm;line-height:normal;font-size:15px;font-family:"Calibri",sans-serif;'>Der Veranstalter verpflichtet sich dazu, sorgsam mit den personenbezogenen Daten der Teilnehmer umzugehen und diese au&szlig;er f&uuml;r die in Punkt B angef&uuml;hrten Zwecken nicht zu verwenden oder weiterzugeben.&nbsp;</p>
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
