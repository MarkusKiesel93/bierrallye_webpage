import axios from 'axios'

// todo: move to index state
let BASE_PATH = `https://${process.env.VUE_APP_BACKEND_DOMAIN}`
if (process.env.NODE_ENV === 'development') {
  BASE_PATH = `http://localhost:${process.env.VUE_APP_BACKEND_PORT}`
}

export default {
  namespaced: true,

  state: {
    channel: 'email',
    email: '',
    phoneNumber: '+43',
    hash: '',

    notificationSuccess: false,
    notificationError: '',

    verificationSuccess: false,
    verificationError: false,
    verificationErrorMessage: '',
  },

  getters: {},

  mutations: {
    setChannel: function(state, value) {
      state.channel = value
      console.log(value)
    },
    setPhoneNumber: function(state, value) {
      state.phoneNumber = value
      console.log(value)
    },
    setEmail: function(state, value) {
      state.email = value
      console.log(value)
    },
    setHash: function(state, value) {
      state.hash = value
      console.log(value)
    },

    NOTIFIED: function(state, response) {
      let contact = state.channel === 'email' ? state.email : state.phoneNumber
      if (response.data.to === contact) {
        console.log(response.data)
      }
    },
    FAILED_NOTIFY: function(state, error) {
      // todo: set error message
      state.verificationError = true
      console.log(error)
      if (error.response.status === 409) {
        state.verificationErrorMessage = error.response.data.detail
      } else {
        // todo: input email adress
        state.verificationErrorMessage =
          'Das sollte nicht passieren. Melde dich bei uns ...'
      }
      state.loading = false
    },
    VERIFIED: function(state, response) {
      let contact = state.channel === 'email'
        ? state.email : state.phoneNumber
      if (response.data.to === contact) {
        console.log(response.data)
      }
    },
    FAILED_VERIFY: function(state, error) {
      state.verificationError = true
      if (error.response.status === 409) {
        state.verificationErrorMessage = error.response.data.detail
      } else {
        // todo: input email adress
        state.verificationErrorMessage =
          'Das sollte nicht passieren. Melde dich bei uns ...'
      }
      state.loading = false
    },
  },
  actions: {
    // todo: add loading
    verifyNotify: async store => {
      const data = {
        to: store.state.channel === 'email' ? store.state.email : store.state.phoneNumber,
        channel: store.state.channel,
      }
      console.log(data)
      try {
        const response = await axios.post(`${BASE_PATH}/verify/notify/`, data)
        return store.commit('NOTIFIED', response)
      } catch (error) {
        return store.commit('FAILED_NOTIFY', error)
      }
    },
    // todo: add loading
    verifyCheck: async store => {
      const data = {
        to: store.state.channel === 'email' ? store.state.email : store.state.phoneNumber,
        channel: store.state.channel,
        hash: store.state.hash,
      }
      console.log(data)
      try {
        const response = await axios.post(`${BASE_PATH}/verify/check/`, data)
        return store.commit('VERIFIED', response)
      } catch (error) {
        return store.commit('FAILED_VERIFY', error)
      }
    },
  },
}
