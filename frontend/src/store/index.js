import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

let BASE_PATH = `https://${process.env.VUE_APP_BACKEND_DOMAIN}`
if (process.env.NODE_ENV === 'development') {
  BASE_PATH = `http://localhost:${process.env.VUE_APP_BACKEND_PORT}`
}


export default new Vuex.Store({
  state: {
    team: {
      email: '',
      firstNamePlayer1: '',
      lastNamePlayer1: '',
      drinkPrefPlayer1: '',
      firstNamePlayer2: '',
      lastNamePlayer2: '',
      drinkPrefPlayer2: '',
      timePref: '',
    },

    drinksOptions: [
      'Bier',
      'Spritzer',
      'Kaiserspritzer',
      'Almweiss',
    ],

    timesOptions: [
      {
        value: 'block1',
        text: 'Block 1',
      },
      {
        value: 'block2',
        text: 'Block 2',
      },
      {
        value: 'block3',
        text: 'Block 3',
      },
      {
        value: 'block4',
        text: 'Block 4',
      }
    ],

    acceptedDataLaws: false,

    loading: false,

    createSuccess: false,
    createError: false,
    createErrorMessage: '',

    verify: {
      email: '',
      hash: '',
    },

    verificationSuccess: false,
    verificationError: false,
    verificationErrorMessage: '',

    deregister: {
      email: '',
      hash: '',
    },

    deleteSuccess: false,
    deleteError: false,
    deleteErrorMessage: '',

    placesAvailable: 0,
    placesFree: {
      block1: 0,
      block2: 0,
      block3: 0,
      block4: 0,
    },
  },
  getters: {
    getTimeInfo: function (state) {
      let items = [
        {
          label: 'Block 1',
          row1: 'Startzeit ca. zwischen 15:00 bis 15:30',
          row2: `${state.placesFree.block1} / 30 Plätze`,
        },
        {
          label: 'Block 2',
          row1: 'Startzeit ca. zwischen 15:00 bis 15:30',
          row2: `${state.placesFree.block2} / 30 Plätze`,
        },
        {
          label: 'Block 3',
          row1: 'Startzeit ca. zwischen 15:00 bis 15:30',
          row2: `${state.placesFree.block3} / 30 Plätze`,
        },
        {
          label: 'Block 4',
          row1: 'Startzeit ca. zwischen 15:00 bis 15:30',
          row2: `${state.placesFree.block4} / 30 Plätze`,
        },
      ]
      return items
    },
    getRegistrationInfo: function (state) {
      let items = [
        {
          label: 'Kontakt',
          row1: state.team.email,
        },
        {
          label: 'Spieler 1',
          row1: `${state.team.firstNamePlayer1} ${state.team.lastNamePlayer1}`
        },
        {
          label: 'Spieler 1 Getränk',
          row1: state.team.drinkPrefPlayer1,
        },
        {
          label: 'Spieler 2',
          row1: `${state.team.firstNamePlayer2} ${state.team.lastNamePlayer2}`
        },
        {
          label: 'Spieler 2 Getränk',
          row1: state.team.drinkPrefPlayer2,
        },
        {
          label: 'Startzeit',
          row1: state.team.timePref,
        }
      ]
      return items
    },
    getCreateSuccessMessage: function (state) {
      return `Verifiziere noch deine Email adresse ${state.team.email} um die Anmldung abzuschließen`
    },
    getVerifySuccessMessage: function (state) {
      return `Eine Bestätigung mit allen Eckdaten bekommst du in den nächsten Minuten an: ${state.verify.email}`
    },
    getDeregistrationInfo: function (state) {
      let items = [
        {
          label: 'E-Mail',
          row1: state.deregister.email,
        },
        {
          label: 'Stornonummer',
          row1: state.deregister.hash,
        }
      ]
      return items
    },
    getDeleteSuccessMessage: function (state) {
      return `Eine Bestätigung bekommst du in den nächsten Minuten an: ${state.deregister.email}`
    }
  },
  mutations: {
    setTeamEmail: function (state, email) {
      state.team.email = email
    },
    setFirstNamePayer1: function (state, firstName) {
      state.team.firstNamePlayer1 = firstName
    },
    setLastNamePlayer1: function (state, lastName) {
      state.team.lastNamePlayer1 = lastName
    },
    setDrinkPrefPlayer1: function (state, drinkPref) {
      state.team.drinkPrefPlayer1 = drinkPref
    },
    setFirstNamePayer2: function (state, firstName) {
      state.team.firstNamePlayer2 = firstName
    },
    setLastNamePlayer2: function (state, lastName) {
      state.team.lastNamePlayer2 = lastName
    },
    setDrinkPrefPlayer2: function (state, drinkPref) {
      state.team.drinkPrefPlayer2 = drinkPref
    },
    setTimePref: function (state, timePref) {
      state.team.timePref = timePref
    },
    setAcceptedDataLaws: function (state, checkbox) {
      state.acceptedDataLaws = checkbox
    },
    setVerifyEmail: function (state, email) {
      state.verify.email = email
    },
    setVerifyHash: function (state, hash) {
      state.verify.hash = hash
    },
    setDeregisterEmail: function (state, value) {
      state.deregister.email = value
    },
    setDeregisterHash: function (state, value) {
      state.deregister.hash = value.toUpperCase()
    },
    'TEAM_CREATED': function (state, response) {
      if (response.data.email == state.team.email) {
        state.createError = false
        state.createSuccess = true
        state.loading = false
      }
    },
    'FAILED_CREATION': function (state, error) {
      state.createError = true
      if (error.response.data.detail) {
        state.createErrorMessage = error.response.data.detail
      }
      state.loading = false
    },
    'TEAM_VARIFIED': function (state, response) {
      if (response.data.email == state.verify.email) {
        state.verificationError = false
        state.verificationSuccess = true
        state.loading = false
      }
    },
    'FAILED_VERIFY': function (state, error) {
      state.verificationError = true
      if (error.response.status === 409) {
        state.verificationErrorMessage = error.response.data.detail
      } else {
        state.verificationErrorMessage = 'Wir werden uns darum kümmern, probiere es später nochmal.'
      }
      state.loading = false
    },
    'TEAM_DELETED': function (state, response) {
      if (response.data.email == state.deregister.email) {
        state.deleteError = false
        state.deleteSuccess = true
        state.loading = false
      }
    },
    'FAILED_DELETION': function (state, error) {
      state.deleteError = true
      if (error.response.data.detail) {
        state.deleteErrorMessage = error.response.data.detail
      }
      state.loading = false
    },
    'PLACES_FREE': function (state, response) {
      let placesAvailable = 0
      for (let [key, value] of Object.entries(response.data)) {
        state.placesFree[key] = value
        placesAvailable += value
      }
      state.placesAvailable = placesAvailable
    },
    'FAILED': function (state, error) {
      console.log(error.response.data)
    }
  },
  actions: {
    createTeam: async (store) => {
      store.state.loading = true
      try {
        const response = await axios.post(`${BASE_PATH}/team/`, store.state.team)
        return store.commit('TEAM_CREATED', response)
      } catch (error) {
        return store.commit('FAILED_CREATION', error)
      }
    },
    verifyTeam: async (store) => {
      store.state.loading = true
      try {
        const response = await axios.post(`${BASE_PATH}/team/verify`, store.state.verify)
        return store.commit('TEAM_VARIFIED', response)
      } catch (error) {
        return store.commit('FAILED_VERIFY', error)
      }
    },
    deleteTeam: async (store) => {
      store.state.loading = true
      try {
        const response = await axios.delete(`${BASE_PATH}/team/${store.state.deregister.email}/${store.state.deregister.hash}/`)
        return store.commit('TEAM_DELETED', response)
      } catch (error) {
        return store.commit('FAILED_DELETION', error)
      }
    },
    getPlacesFree: async (store) => {
      try {
        const response = await axios.get(`${BASE_PATH}/places/free/`)
        return store.commit('PLACES_FREE', response)
      } catch (error) {
        return store.commit('FAILED', error)
      }
    }
  },
})
