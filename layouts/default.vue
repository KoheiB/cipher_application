<template>
  <v-app>
    <Header :isLogin="isLogin" @login="login()" @logout="logout()" />
    <v-main>
      <Nuxt />
      {{ loginUser }}
    </v-main>
    <BottomNav />
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      loginUser: [],
      isLogin: false,
    }
  },
  async mounted() {
    this.loginUser = await this.$auth()
    if (!this.loginUser) {
      const userCredential = await this.$fireAuth.signInAnonymously()
      this.loginUser = userCredential.user
      console.log('匿名認証')
    }
  },
  methods: {
    login() {
      const provider = new this.$firebase.auth.TwitterAuthProvider()

      try {
        const { user } = this.$fireAuth.currentUser.linkWithPopup(provider)
        this.isLogin = true
      } catch (e) {
        console.error(e)
      }
    },
    logout() {
      this.$fireAuth.signOut().then(() => {
        this.isLogin = false
        this.$router.go({ path: this.$router.currentRoute.path, force: true })
      })
    },
  },
}
</script>
