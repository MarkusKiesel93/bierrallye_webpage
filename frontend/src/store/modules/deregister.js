import axios from 'axios'

export default {
  namespaced: true,

  state: {
    team: {
      contact: '',
      firstNamePlayer1: '',
      lastNamePlayer1: '',
      firstNamePlayer2: '',
      lastNamePlayer2: '',
    },

    channel: 'email',
    email: '',
    phoneNumber: '+43',
    hash: '',

    success: false,

    loading: false,

    alert: false,
    alertType: 'success',
    alertMessage: '',
  },
  getters: {
    contact: function(state) {
      let contact = state.channel === 'email' ? state.email : state.phoneNumber
      return contact.replace(/\s/g,'')
    },
    info: function(state) {
      let items = [
        {
          id: 1,
          label: 'Kontakt',
          row1: state.team.contact,
        },
        {
          id: 2,
          label: 'Spieler 1',
          row1: `${state.team.firstNamePlayer1} ${state.team.lastNamePlayer1}`,
        },
        {
          id: 3,
          label: 'Spieler 2',
          row1: `${state.team.firstNamePlayer1} ${state.team.lastNamePlayer1}`,
        },
        {
          id: 4,
          label: 'Stornonummer',
          row1: state.hash,
        },
      ]
      return items
    },
  },
  mutations: {
    setContact: function(state, obj) {
      state.channel = obj.channel
      if (obj.channel === 'email') {
        state.email = obj.contact
      } else {
        state.phoneNumber = obj.contact
      }
    },
    setChannel: function(state, value) {
      state.channel = value
    },
    setPhoneNumber: function(state, value) {
      state.phoneNumber = value.replace(' ', '')
    },
    setEmail: function(state, value) {
      state.email = value
    },
    setHash: function(state, value) {
      state.hash = value.toUpperCase()
    },

    GET_TEAM: function(state, response) {
      state.loading = false
      if (response.data) {
        state.team = response.data
      }
      state.alert = false
    },
    TEAM_DELETED: function(state, response) {
      state.loading = false
      if (response.data) {
        state.success = true
      }
    },
    FAILED: function(state, error) {
      state.loading = false
      state.alertType = 'error'
      if (error.response.status === 400) {
        state.alertMessage = error.response.data.detail
      } else {
        state.errorMessage = 'Das sollte nicht passieren, versuche es erneut.'
      }
      state.alert = true
    },
  },

  actions: {
    async requestTeam(context) {
      context.state.loading = true
      try {
        const response = await axios.get(`${context.rootGetters.getApiPath}/team/${context.getters.contact}`)
        return context.commit('GET_TEAM', response)
      }  catch (error) {
        return context.commit('FAILED', error)
      }
    },
    async deleteTeam(context) {
      context.state.loading = true
      try {
        const response = await axios.delete(
          `${context.rootGetters.getApiPath}/team/${context.getters.contact}/${context.state.hash}/`,
        )
        return context.commit('TEAM_DELETED', response)
      } catch (error) {
        return context.commit('FAILED', error)
      }
    },
  }
}