<template>
  <div class="card-wrapper">
    <v-card class="ma-1">
      <v-img :src="image"></v-img>
      <!-- <v-img :src="require('@/static/img/S10/S10-001ST.png')"></v-img> -->
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    image: {
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
