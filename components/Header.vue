<template>
  <v-app-bar app dense clipped-left>
    <v-toolbar-title>CipherApp</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-toolbar-items class="hidden-mobile-and-down">
      <v-btn-toggle v-model="icon" borderless>
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

    <div v-show="isLogin" class="ml-5">
      <v-toolbar-items>
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" style="text-transform: none" text>
              <v-icon> mdi-account</v-icon>
              {{ user.name }}
            </v-btn>
          </template>
          <v-list>
            <v-list-item v-for="user_menu in user_menus" :key="user_menu" link>
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
    <div v-show="!isLogin" class="mx-5">
      <v-btn small class="primary">
        <v-icon> mdi-account-plus</v-icon>
        <span class="hidden-ipad-and-down">新規登録</span>
      </v-btn>
      <v-btn small class="info" @click="login">
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
      isLogin: true,
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
          method: () => this.logout(),
        },
      ],
    }
  },
  methods: {
    login() {
      this.isLogin = true
    },
    logout() {
      this.isLogin = false
    },
  },
}
</script>

<style>
.header-menu-text {
  letter-spacing: -0.5px;
}
</style>
