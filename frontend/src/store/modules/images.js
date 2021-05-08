export default {
  namespaced: true,

  state: {},

  getters: {
    headerImages (state, getters, rootState, rootGetters) {
      return [
        {
          id: 1,
          src: `${rootGetters.getStaticPath}team.jpg`,
        },
        {
          id: 2,
          src: `${rootGetters.getStaticPath}fun.jpg`,
        },
        {
          id: 3,
          src: `${rootGetters.getStaticPath}games.jpg`,
        },
        {
          id: 4,
          src: `${rootGetters.getStaticPath}start.jpg`,
        },
        {
          id: 5,
          src: `${rootGetters.getStaticPath}sporthaus.jpg`,
        },
      ]
    }
  }
}