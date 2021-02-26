<template>
  <v-container fluid>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <v-form @submit.prevent="submit">
        <validation-provider
          v-slot="{ errors }"
          name="Datenschutzerklärung"
          rules="checked"
        >
          <v-checkbox 
            v-model="checkbox"
            :error-messages="errors"
          >
            <template v-slot:label>
              <div>
                Ich akzeptiere die 
                <router-link :to="{ name: 'DataProtectionView' }" active-class>
                  Datenschutzerklärung
                </router-link>
              </div>
            </template>
          </v-checkbox>
        </validation-provider>
        <v-btn
          color="primary"
          class="mr-4 mt-4"
          :disabled="invalid"
          @click="submit"
        >
          Anmelden
        </v-btn>
        <v-btn
          class="mt-4"
          @click="cancel"
        >
          Zurück
        </v-btn>
      </v-form>
    </validation-observer>
  </v-container>
</template>


<script>
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from 'vee-validate';

setInteractionMode('lazy');

extend('checked', {
  validate: value => {
    return value
  },
  message: '{_field_} muss akzeptiert werden!',
});

export default {
  name: 'RegistrationCompletion',
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data: () => ({
    checkbox: false,
  }),
  methods: {
    submit() {
      this.$refs.observer.validate();
      this.$emit('complete-registration');
    },
    cancel() {
      this.$refs.observer.reset()
      this.$emit('last-step');
    },
  },
}
</script>