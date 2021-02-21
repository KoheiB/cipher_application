<template>
  <div class="card-wrapper">
    <v-card style="margin: 1px">
      <v-img :src="imageUrl" />
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    imageUrl: {
      type: String,
      required: true,
    },
  },
}
</script>

<style>
.card-wrapper {
  width: 10%;
}
</style>
