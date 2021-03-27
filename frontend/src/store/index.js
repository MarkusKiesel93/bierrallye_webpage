import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import VueAxios from 'vue-axios'

import register from './modules/register'
import deregister from './modules/deregister'
import verifyContact from './modules/verifyContact'

Vue.use(Vuex)
Vue.use(VueAxios, axios)

export default new Vuex.Store({
  modules: {
    register,
    deregister,
    verifyContact,
  },

  state: {
    placesFree: 0,
  },

  getters: {
    getApiPath: function() {
      let apiPath = `https://${process.env.VUE_APP_BACKEND_DOMAIN}`
      if (process.env.NODE_ENV === 'development') {
        apiPath = `http://localhost:${process.env.VUE_APP_BACKEND_PORT}`
      }
      return apiPath
    }
  },

  mutations: {    
    PLACES_FREE: function(state, response) {
      state.placesFree = response.data
    },
  },

  actions: { 
    async requestPlacesFree(store) {
      try {
        const response = await axios.get(`${store.getters.getApiPath}/places/free/`)
        return store.commit('PLACES_FREE', response)
      } catch (error) {
        console.log(error.response)
      }
    },
  },
})
