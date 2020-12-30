<template>
  <v-container class="">
    <div>
      <v-btn nuxt to="buildDeck">デッキを作成する</v-btn>
    </div>
    <v-row>
      <v-col v-for="n of 6" :key="n" cols="3">
        <v-container>
          <v-hover>
            <template v-slot:default="{ hover }">
              <v-card height="280" class="rounded-xl" nuxt to="buildDeck" hover>
                <v-img
                  :src="require('@/static/img/B13/B13-005N.png')"
                  max-height="70%"
                  position="top"
                ></v-img>
                <v-card-title
                  >紫無リン 〜ニニアンテティスを添えて〜</v-card-title
                >
                <v-fade-transition>
                  <v-overlay v-if="hover" absolute color="#036358">
                    <v-icon x-large>mdi-square-edit-outline</v-icon>
                  </v-overlay>
                </v-fade-transition>
              </v-card>
            </template>
          </v-hover>
        </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      overlay: false,
    }
  },
}
</script>
