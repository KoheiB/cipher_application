<template>
  <v-list-item
    class="px-0 mr-8 ml-2"
    :class="color"
    style="margin-bottom: 1px"
    @click="$emit('card-list-click')"
  >
    <v-list-item-avatar class="ma-0 mr-2" tile height="48" width="72">
      <v-img :src="imageUrl" position="top" />
    </v-list-item-avatar>
    <v-list-item-content class="card-info py-0 d-flex flex-nowrap">
      <v-row class="mx-0">
        <v-col cols="10" class="py-0" align-self="center">
          <v-list-item-title>
            <span class="card-title">{{ title }}</span>
            <br />
            <span>{{ unitName }}</span>
          </v-list-item-title>
        </v-col>
        <v-col
          cols="2"
          class="px-0 py-4 blue-grey darken-4 white--text font-weight-bold text-center"
          style="height: 48px"
        >
          <span style="font-size: 16px; margin-right: 2px">x</span>{{ count }}
        </v-col>
      </v-row>
    </v-list-item-content>
  </v-list-item>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    unitName: {
      type: String,
      required: true,
    },
    symbols: {
      type: Array,
      required: true,
    },
    color: {
      type: String,
      required: true,
    },
    gradation: {
      type: String,
      required: true,
    },
    count: {
      type: Number,
      required: true,
    },
  },
}
</script>

<style>
.card-title {
  color: rgba(0, 0, 0, 0.6);
  font-size: 0.875rem;
}
</style>
