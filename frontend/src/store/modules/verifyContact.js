import axios from 'axios'

export default {
  namespaced: true,

  state: {
    channel: 'email',
    email: '',
    phoneNumber: '+43',
    hash: '',

    success: false,

    laoding: false,

    alert: false,
    alertType: 'success',
    alertMessage: '',
  },

  getters: {
    contact: function(state) {
      let contact = state.channel === 'email' ? state.email : state.phoneNumber
      return contact.replace(' ', '')
    },
    notifyData: function(state, getters) {
      return {
        to: getters.contact,
        channel: state.channel,
      }
    },
    verifyData: function(state, getters) {
      return {
        to: getters.contact,
        channel: state.channel,
        hash: state.hash,
      }
    }
  },

  mutations: {
    setChannel: function(state, value) {
      state.channel = value
    },
    setPhoneNumber: function(state, value) {
      state.phoneNumber = value
    },
    setEmail: function(state, value) {
      state.email = value
    },
    setHash: function(state, value) {
      state.hash = value
    },

    NOTIFIED: function(state, response) {
      state.loading = false
      state.alertType = 'success'
      state.alertMessage = `Code gesendet an ${response.data.to}`
      state.alert = true
    },
    FAILED_NOTIFY: function(state, error) {
      state.loading = false
      const status = error.response.status
      if (status === 409 || status === 403 || status === 429) {
        state.alertMessage = error.response.data.detail
        if (status === 429) {
          state.alertType = 'warning'
        } else {
          state.alertType = 'error'
        }
      } else {
        state.alertType = 'error'
        state.alertMessage = 'Das sollte nicht passieren, verusche es erneut.'
      }
      state.alert = true
    },
    VERIFIED: function(state, response) {
      state.loading = false
      state.alertType = 'success'
      state.alertMessage = `${response.data.to} erfolgreich verifiziert`
      state.success = true
      state.alert = true
    },
    FAILED_VERIFY: function(state, error) {
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
    async verifyNotify(context) {
      context.state.loading = true
      try {
        const response = await axios.post(`${context.rootGetters.getApiPath}/verify/notify/`, context.getters.notifyData)
        return context.commit('NOTIFIED', response)
      } catch (error) {
        return context.commit('FAILED_NOTIFY', error)
      }
    },
    async verifyCheck(context) {
      context.state.loading = true
      try {
        const response = await axios.post(`${context.rootGetters.getApiPath}/verify/check/`, context.getters.verifyData)
        return context.commit('VERIFIED', response)
      } catch (error) {
        return context.commit('FAILED_VERIFY', error)
      }
    },
  },
}
