<template>
  <div style="width: 10%; padding: 1px">
    <v-hover>
      <template v-slot:default="{ hover }">
        <v-card>
          <v-img :src="imageUrl" />
          <v-fade-transition>
            <v-overlay v-show="hover" absolute>
              <v-layout column>
                <v-btn color="blue-grey lighten-4" x-small
                  ><v-icon color="black">mdi-magnify</v-icon></v-btn
                >
                <v-btn
                  class="align-self-end"
                  color="blue-grey lighten-5"
                  x-small
                  ><v-icon color="light-blue accent-4">mdi-plus</v-icon></v-btn
                >
                <v-btn
                  class="align-self-end"
                  color="blue-grey lighten-5"
                  x-small
                  ><v-icon color="red accent-4">mdi-minus</v-icon></v-btn
                >
              </v-layout>
            </v-overlay>
          </v-fade-transition>
        </v-card>
      </template>
    </v-hover>
  </div>
</template>

<script>
export default {
  props: {
    cardId: {
      type: String,
      required: true,
    },
    imageUrl: {
      type: String,
      required: true,
    },
  },
}
</script>
