<template>
  <v-bottom-navigation class="d-mobile-none">
    <v-btn-toggle borderless>
      <v-btn text nuxt to="buildDeck" class="text-capitalize">
        <v-icon> mdi-file-edit-outline </v-icon>
        <span>Build Deck</span>
      </v-btn>
      <v-btn text nuxt to="myDeckLists" class="text-capitalize">
        <v-icon> mdi-file-cog-outline </v-icon>
        <span>Deck Manager</span>
      </v-btn>
      <v-btn text nuxt to="" class="text-capitalize">
        <v-icon> mdi-file-find-outline </v-icon>
        <span>Recipe Board</span>
      </v-btn>
    </v-btn-toggle>
  </v-bottom-navigation>
</template>

<script>
export default {}
</script>

<style></style>
