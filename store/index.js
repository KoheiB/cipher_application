export const strict = false

export const state = () => ({
  user: null,
})

export const mutations = {
  setUser(state, payload) {
    state.user = payload
  },
}

export const actions = {
  signUp({ commit }, { email, password }) {
    return this.$fireAuth.createUserWithEmailAndPassword(email, password)
  },

  signInWithEmail({ commit }, { email, password }) {
    return this.$fireAuth.signInWithEmailAndPassword(email, password)
  },

  signInWithTwitter({ commit }) {
    return this.$fireAuth.signInWithPopup(
      new this.$firebase.auth.TwitterAuthProvider()
    )
  },

  signOut() {
    return this.$fireAuth.signOut()
  },
}

export const getters = {
  user(state) {
    return state.user
  },
  isAuthenticated(state) {
    return !!state.user
  },
}
