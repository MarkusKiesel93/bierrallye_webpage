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
      firstNamePlayer2: '',
      lastNamePlayer2: '',
      drinkPref: '',
      timePref: '',
    },

    createStatus: null,
    createInfo: '',

    deregisterEmail: '',
    deregisterHash: '',


    deleteStatus: null,
    deleteInfo: '',
  },
  getters: {
    getPlayer1: function (state) {
      let player = {
        firstName: state.team.firstNamePlayer1,
        lastName: state.team.lastNamePlayer1,
      } 
      return player
    },
    getPlayer2: function (state) {
      let player = {
        firstName: state.team.firstNamePlayer2,
        lastName: state.team.lastNamePlayer12
      } 
      return player
    },
  },
  mutations: {
    setTeamEmail: function (state, email) {
      state.team.email = email
    },
    setPlayer1: function (state, player) {
      state.team.firstNamePlayer1 = player.firstName
      state.team.lastNamePlayer1 = player.lastName
    },
    setPlayer2: function (state, player) {
      state.team.firstNamePlayer2 = player.firstName
      state.team.lastNamePlayer2 = player.lastName
    },
    setDeregisterEmail: function (state, value) {
      state.deregisterEmail = value
    },
    setDeregisterHash: function (state, value) {
      state.deregisterHash = value.toUpperCase()
    },
    setStatus: function(state, obj) {
      let key = Object.keys(obj)[0]
      let value = Object.values(obj)[0]
      state[key] = value
    },
    'TEAM_CREATED': function (state, response) {
      state.createStatus = 'success'
      state.createInfo = response.data.email
    },
    'FAILED_CREATION': function (state, error) {
      state.createStatus = 'failed'
      state.createInfo = error.response.data.detail
    },
    'TEAM_DELETED': function (state, response) {
      state.deleteStatus = 'success'
      state.deleteInfo = response.data.email
    },
    'FAILED_DELETION': function (state, error) {
      state.deleteStatus = 'failed'
      state.deleteInfo = error.response.data.detail
    },
  },
  actions: {
    createTeam: function (store) {
      return axios.post(`${BASE_PATH}/teams/`, store.state.team)
        .then((response) => store.commit('TEAM_CREATED', response))
        .catch((error) => store.commit('FAILED_CREATION', error))
    },
    deleteTeam: function (store) {
      return axios.delete(`${BASE_PATH}/teams/${store.state.deregisterEmail}/${store.state.deregisterHash}/`)
        .then((response) => store.commit('TEAM_DELETED', response))
        .catch((error) => store.commit('FAILED_DELETION', error))
    },
  },
  modules: {}
})
