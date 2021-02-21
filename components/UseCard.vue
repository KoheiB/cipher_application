<template>
  <div style="width: 10%">
    <v-hover>
      <template v-slot:default="{ hover }">
        <v-card style="margin: 1px" hover>
          <v-img :src="imageUrl" />
          <v-fade-transition>
            <v-overlay v-show="hover" absolute>
              <div class="d-flex flex-column">
                <v-btn
                  class="align-self-end"
                  color="blue-grey lighten-5"
                  fab
                  x-small
                  ><v-icon color="light-blue accent-4">mdi-plus</v-icon></v-btn
                >
                <v-btn class="ma-1" color="blue-grey lighten-4" width="50%"
                  ><v-icon color="black">mdi-magnify</v-icon></v-btn
                >
                <v-btn color="blue-grey lighten-5" fab x-small
                  ><v-icon color="red accent-4">mdi-minus</v-icon></v-btn
                >
              </div>
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
