import axios from 'axios'

export default {
  namespaced: true,

  state: {
    firstNamePlayer1: '',
    lastNamePlayer1: '',
    drinkPrefPlayer1: '',
    firstNamePlayer2: '',
    lastNamePlayer2: '',
    drinkPrefPlayer2: '',
    startBlock: '',

    drinksOptions: [],
    blockOptions: [],

    acceptedGameRules: false,
    acceptedDataLaws: false,

    success: false,

    loading: false,

    alert: false,
    alertType: 'success',
    alertMessage: '',
  },

  getters: {
    team: function(state, getters, rootState, rootGetters) {
      const team = {
        contact: rootGetters['verifyContact/contact'],
        channel: rootState.verifyContact.channel,
        firstNamePlayer1: state.firstNamePlayer1,
        lastNamePlayer1: state.lastNamePlayer1,
        drinkPrefPlayer1: state.drinkPrefPlayer1,
        firstNamePlayer2: state.firstNamePlayer2,
        lastNamePlayer2: state.lastNamePlayer2,
        drinkPrefPlayer2: state.drinkPrefPlayer2,
        startBlock: state.startBlock,
      }
      return team
    },
    blockOptions: function(state) {
      let items = []
      for (const blockOption of state.blockOptions) {
        if (blockOption.free > 0) {
          items.push(blockOption)
        }
      }
      return items
    },
    blockInfo: function(state) {
      let items = []
      for (let blockOption of state.blockOptions) {
        items.push({
          label: blockOption.text,
          row1: `Anmeldung (vor Ort) ${blockOption.time} Uhr`,
          row2: `Frei Plätze: ${blockOption.free}`,
        })
      }
      return items
    },
    block: function(state) {
      if (state.startBlock.length > 0) {
        const startBlock = state.blockOptions.filter(
          item => item.value === state.startBlock,
        )
        return startBlock[0].text
      } else {
        return ''
      }
    },
    registrationInfo: function(state, getters, rootState, rootGetters) {
      let items = [
        {
          id: 1,
          label: 'Kontakt',
          row1: rootGetters['verifyContact/contact'],
        },
        {
          id: 2,
          label: 'Spieler 1',
          row1: `${state.firstNamePlayer1} ${state.lastNamePlayer1}`,
        },
        {
          id: 3,
          label: 'Getränk',
          row1: state.drinkPrefPlayer1,
        },
        {
          id: 4,
          label: 'Spieler 2',
          row1: `${state.firstNamePlayer2} ${state.lastNamePlayer2}`,
        },
        {
          id: 5,
          label: 'Getränk',
          row1: state.drinkPrefPlayer2,
        },
        {
          id: 6,
          label: 'Startzeit',
          row1: getters.block,
        },
      ]
      return items
    },
  },

  mutations: {
    setContact: function(state, value) {
      state.contact = value
    },
    setFirstNamePayer1: function(state, value) {
      state.firstNamePlayer1 = value
    },
    setLastNamePlayer1: function(state, value) {
      state.lastNamePlayer1 = value
    },
    setDrinkPrefPlayer1: function(state, value) {
      state.drinkPrefPlayer1 = value
    },
    setFirstNamePayer2: function(state, value) {
      state.firstNamePlayer2 = value
    },
    setLastNamePlayer2: function(state, value) {
      state.lastNamePlayer2 = value
    },
    setDrinkPrefPlayer2: function(state, value) {
      state.drinkPrefPlayer2 = value
    },
    setStartBlock: function(state, value) {
      state.startBlock = value
    },
    setAcceptedGameRules: function(state, value) {
      state.acceptedGameRules = value
    },
    setAcceptedDataLaws: function(state, value) {
      state.acceptedDataLaws = value
    },

    TEAM_CREATED: function(state, response) {
      state.loading = false
      if (response.data) {
        state.success = true
      }
    },
    FAILED_CREATION: function(state, error) {
      state.loading = false
      state.alertType = 'error'
      if (error.response.status === 409) {
        state.alertMessage = error.response.data.detail
      } else {
        state.errorMessage = 'Das sollte nicht passieren, versuche es erneut.'
      }
      state.alert = true
    },
    BLOCK_OPTIONS: function(state, response) {
      state.blockOptions = response.data
    },
    DRINK_OPTIONS: function(state, response) {
      state.drinksOptions = response.data
    },
  },

  actions: {
    async createTeam (context) {
      context.state.loading = true
      try {
        const response = await axios.post(
          `${context.rootGetters.getApiPath}/team/`,
          context.getters.team,
        )
        return context.commit('TEAM_CREATED', response)
      } catch (error) {
        return context.commit('FAILED_CREATION', error)
      }
    },
    async requestBlockOptions(context) {
      try {
        const response = await axios.get(`${context.rootGetters.getApiPath}/options/blocks/`)
        return context.commit('BLOCK_OPTIONS', response)
      } catch (error) {
        console.log(error.response)
      }
    },
    async requestDrinkOptions(context) {
      try {
        const response = await axios.get(`${context.rootGetters.getApiPath}/options/drinks/`)
        return context.commit('DRINK_OPTIONS', response)
      } catch (error) {
        console.log(error.response)
      }
    },
  },
}