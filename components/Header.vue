<template>
  <v-app-bar app>
    <v-toolbar-title>CipherApp</v-toolbar-title>

    <v-spacer></v-spacer>

    <v-btn nuxt to="buildDeck" class="text-capitalize">Build Deck</v-btn>
    <v-btn nuxt to="myDeckLists" class="text-capitalize">Deck Manager</v-btn>
    <v-btn nuxt to="" class="text-capitalize">Recipe Board</v-btn>
    <div v-show="isLogin" class="mx-5">
      <v-toolbar-items>
        <v-menu offset-y>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" text style="text-transform: none">
              <v-icon> mdi-account</v-icon>
              {{ user.name }}
            </v-btn>
          </template>
          <v-list>
            <v-list-item v-for="user_menu in user_menus" :key="user_menu">
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
      <v-btn class="primary">新規登録</v-btn>
      <v-btn class="info" @click="login">ログイン</v-btn>
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

<style></style>
