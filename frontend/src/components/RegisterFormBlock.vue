<template>
  <v-form>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <InfoItems :items="blockInfo" />
      <InputSelectBox
        label="Startblock"
        :value="startBlock"
        :items="blockOptions"
        :setter="blockSetter"
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
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex'
import { ValidationObserver } from 'vee-validate'

import InfoItems from '@/components/InfoItems'
import InputSelectBox from '@/components/InputSelectBox'
import ButtonsSubmitCancel from '@/components/ButtonsSubmitCancel'

export default {
  name: 'RegisterFormBlock',
  components: {
    ValidationObserver,
    InfoItems,
    InputSelectBox,
    ButtonsSubmitCancel,
  },
  computed: {
    ...mapState({
      startBlock: state => state.register.startBlock,
    }),
    ...mapGetters({
      blockInfo: 'register/blockInfo',
      blockOptions: 'register/blockOptions',
    }),
  },
  methods: {
    ...mapMutations({
      blockSetter: 'register/setStartBlock',
    }),
    ...mapActions({
      requestBlockOptions: 'register/requestBlockOptions',
    }),
   },
   created: function() {
    this.requestBlockOptions()
  },
}
</script>

<style>

</style>