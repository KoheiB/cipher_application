<template>
  <div class="card-wrapper">
    <v-card class="ma-1">
      <v-img :src="img"></v-img>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    img: {
      type: String,
    },
  },
}
</script>

<style>
.card-wrapper {
  width: 10%;
}
</style>
