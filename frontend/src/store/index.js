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
      player1: {
        firstName: '',
        lastName: '',
      },
      player2: {
        firstName: '',
        lastName: '',
      },
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
  mutations: {
    setTeamValues: function (state, obj) {
      for (let [key, value] of Object.entries(obj)) {
        state.team[key] = value
      }
    },
    setPlayer1: function (state, player) {
      state.team.player1.firstName = player.firstName
      state.team.player1.lastName = player.lastName
    },
    setPlayer2: function (state, player) {
      state.team.player2.firstName = player.firstName
      state.team.player2.lastName = player.lastName
    },
    setDeregisterEmail: function (state, value) {
      state.deregisterEmail = value
    },
    setDeregisterHash: function (state, value) {
      state.deregisterHash = value
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
