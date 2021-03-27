<template>
  <v-form>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <h3>Spieler 1</h3>
      <InputName
        :firstName="firstNamePlayer1"
        :lastName="lastNamePlayer1"
        :firstNameSetter="firstName1Setter"
        :lastNameSetter="lastName1Setter"
      />
      <InputSelectBox
        label="Getränk Spieler 1"
        :value="drinkPrefPlayer1"
        :items="drinksOptions"
        :setter="drinkPref1Setter"
      />
      <h3>Spieler 2</h3>
      <InputName
        :firstName="firstNamePlayer2"
        :lastName="lastNamePlayer2"
        :firstNameSetter="firstName2Setter"
        :lastNameSetter="lastName2Setter"
      />
      <InputSelectBox
        label="Getränk Spieler 2"
        :value="drinkPrefPlayer2"
        :items="drinksOptions"
        :setter="drinkPref2Setter"
      />
      <ButtonsSubmitCancel
        submitLabel="Weiter"
        :disabled="invalid"
        v-on:click-submit="$emit('click-submit')"
        v-on:click-cancel="$emit('click-cancel')"
      />
    </validation-observer>
  </v-form>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import { ValidationObserver } from 'vee-validate'

import InputName from '@/components/InputName'
import InputSelectBox from '@/components/InputSelectBox'
import ButtonsSubmitCancel from '@/components/ButtonsSubmitCancel'

export default {
  name: 'RegisterFormPlayer',
  components: {
    ValidationObserver,
    InputName,
    InputSelectBox,
    ButtonsSubmitCancel,
  },
  computed: {
    ...mapState({
      drinksOptions: state => state.register.drinksOptions,
      firstNamePlayer1: state => state.register.firstNamePlayer1,
      lastNamePlayer1: state => state.register.lastNamePlayer1,
      drinkPrefPlayer1: state => state.register.drinkPrefPlayer1,
      firstNamePlayer2: state => state.register.firstNamePlayer2,
      lastNamePlayer2: state => state.register.lastNamePlayer2,
      drinkPrefPlayer2: state => state.register.drinkPrefPlayer2,
    }),
  },
   methods: {
    ...mapMutations({
      firstName1Setter: 'register/setFirstNamePayer1',
      lastName1Setter: 'register/setLastNamePlayer1',
      drinkPref1Setter: 'register/setDrinkPrefPlayer1',
      firstName2Setter: 'register/setFirstNamePayer2',
      lastName2Setter: 'register/setLastNamePlayer2',
      drinkPref2Setter: 'register/setDrinkPrefPlayer2',
    }),
    ...mapActions({
      requestDrinkOptions: 'register/requestDrinkOptions',
    }),
   },
   created: function() {
    this.requestDrinkOptions()
  },
}
</script>
