<template>
  <v-app-bar app dense clipped-left>
    <v-toolbar-title>CipherApp</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-toolbar-items class="hidden-mobile-and-down">
      <v-btn-toggle borderless>
        <v-btn text nuxt to="buildDeck" class="text-capitalize">
          <v-icon> mdi-file-edit-outline </v-icon>
          <span class="hidden-ipad-and-down header-menu-text">
            Build Deck
          </span>
        </v-btn>
        <v-btn text nuxt to="myDeckLists" class="text-capitalize">
          <v-icon> mdi-file-cog-outline </v-icon>
          <span class="hidden-ipad-and-down header-menu-text">
            Deck Manager
          </span>
        </v-btn>
        <v-btn text nuxt to="" class="text-capitalize">
          <v-icon> mdi-file-find-outline </v-icon>
          <span class="hidden-ipad-and-down header-menu-text"
            >Recipe Board
          </span>
        </v-btn>
      </v-btn-toggle>
    </v-toolbar-items>

    <div v-show="this.$store.getters.isAuthenticated" class="ml-5">
      <v-toolbar-items>
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn style="text-transform: none" text v-on="on">
              <!-- <v-img
                :src="$store.getters.user.providerData[0].photoURL"
                position="top"
              /> -->
              <v-icon> mdi-account</v-icon>
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="user_menu in user_menus"
              :key="user_menu.index"
              link
            >
              <v-list-item-content>
                <v-list-item-title
                  @click="
                    {
                      {
                        user_menu.method()
                      }
                    }
                  "
                  >{{ user_menu.label }}</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-toolbar-items>
    </div>
    <div v-show="!this.$store.getters.isAuthenticated" class="mx-5">
      <v-btn small nuxt to="login" class="info">
        <v-icon>mdi-login</v-icon>
        <span class="hidden-ipad-and-down">ログイン</span>
      </v-btn>
    </div>
  </v-app-bar>
</template>

<script>
export default {
  data() {
    return {
      isLogin: false,
      user: {
        name: 'buruso3',
      },
      user_menus: [
        {
          label: 'Setting',
          method: null,
        },
        {
          label: 'Logout',
          method: () => this.signOut(),
        },
      ],
    }
  },
  methods: {
    signOut() {
      this.$store.dispatch('signOut').then(() => {
        this.$router.push({
          name: 'index',
        })
      })
    },
  },
}
</script>

<style>
.header-menu-text {
  letter-spacing: -0.5px;
}
</style>
