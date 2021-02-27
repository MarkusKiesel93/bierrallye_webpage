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
      drinkPrefPlayer1: 'unentschlossen',
      firstNamePlayer2: '',
      lastNamePlayer2: '',
      drinkPrefPlayer2: 'unentschlossen',
      timePref: 'allzeit bereit',
    },

    drinksOptions: [
      'unentschlossen',
      'Bier',
      'Spritzer',
      'Kaiserspritzer',
      'Almweiss',
    ],
    timesOptions: [
      'allzeit bereit',
      'Block 1',
      'Block 2',
      'Block 3',
      'Block 4',
    ],

    acceptedDataLaws: false,

    createSuccess: false,
    createError: false,
    createErrorMessage: '',

    deregister: {
      email: '',
      hash: '',
    },

    deleteSuccess: false,
    deleteError: false,
    deleteErrorMessage: '',
  },
  getters: {
    getRegistrationInfo: function (state) {
      let items = [
        {
          label: 'Kontakt',
          value: state.team.email,
        },
        {
          label: 'Name Spieler 1',
          value: `${state.team.firstNamePlayer1} ${state.team.lastNamePlayer1}`
        },
        {
          label: 'Getränk Spieler 1',
          value: state.team.drinkPrefPlayer1,
        },
        {
          label: 'Name Spieler 2',
          value: `${state.team.firstNamePlayer2} ${state.team.lastNamePlayer2}`
        },
        {
          label: 'Getränk Spieler 2',
          value: state.team.drinkPrefPlayer2,
        },
        {
          label: 'Startzeit',
          value: state.team.timePref,
        }
      ]
      return items
    },
    getCreateSuccessMessage: function (state) {
      return `Eine Bestätigung bekommst du in den nächsten Minuten an: ${state.team.email}`
    },
    getDeregistrationInfo: function (state) {
      let items = [
        {
          label: 'E-Mail',
          value: state.deregister.email,
        },
        {
          label: 'Stornonummer',
          value: state.deregister.hash,
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
    setCreateSuccess: function (state, status) {
      state.createSuccess = status
    },
    setCreateError: function (state, status) {
      state.createError = status
    },
    setDeregisterEmail: function (state, value) {
      state.deregister.email = value
    },
    setDeregisterHash: function (state, value) {
      state.deregister.hash = value.toUpperCase()
    },
    setDeleteSuccess: function (state, status) {
      state.deleteSuccess = status
    },
    setDeleteError: function (state, status) {
      state.deleteError = status
    },
    'TEAM_CREATED': function (state, response) {
      if (response.data.email == state.team.email) {
        state.createSuccess = true
      }
    },
    'FAILED_CREATION': function (state, error) {
      state.createError = true
      if (error.response.data.detail) {
        state.createErrorMessage = error.response.data.detail
      }
    },
    'TEAM_DELETED': function (state, response) {
      if (response.data.email == state.deregister.email) {
        state.deleteSuccess = true
      }
    },
    'FAILED_DELETION': function (state, error) {
      state.deleteError = true
      if (error.response.data.detail) {
        state.deleteErrorMessage = error.response.data.detail
      }
    },
  },
  actions: {
    createTeam: function (store) {
      return axios.post(`${BASE_PATH}/teams/`, store.state.team)
        .then((response) => store.commit('TEAM_CREATED', response))
        .catch((error) => store.commit('FAILED_CREATION', error))
    },
    deleteTeam: function (store) {
      return axios.delete(`${BASE_PATH}/teams/${store.state.deregister.email}/${store.state.deregister.hash}/`)
        .then((response) => store.commit('TEAM_DELETED', response))
        .catch((error) => store.commit('FAILED_DELETION', error))
    },
  },
  modules: {}
})
