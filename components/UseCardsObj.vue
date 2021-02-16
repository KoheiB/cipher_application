<template>
  <v-list-item
    class="px-0 mr-8 ml-2"
    :class="color"
    style="margin-bottom: 1px; min-height: 38px"
    :ripple="false"
    @click="$emit('card-list-click', cardId)"
  >
    <!-- @click="$emit('card-list-click')" -->
    <v-list-item-avatar class="ma-0 mr-2" tile height="38" width="72">
      <v-img :src="imageUrl" position="top" />
    </v-list-item-avatar>
    <v-list-item-content
      class="card-info py-0 d-flex flex-nowrap"
      style="height: 38px"
    >
      <v-row class="mx-0">
        <v-col cols="10" class="py-0" align-self="center">
          <v-list-item-title>
            <span class="list-title">{{ title }}</span>
            <br />
            <span class="list-unit-name">{{ unitName }}</span>
          </v-list-item-title>
        </v-col>
        <v-col
          cols="2"
          class="px-0 blue-grey darken-4 white--text font-weight-bold text-center"
          style="height: 38px; padding-top: 11px"
        >
          <span style="font-size: 16px; margin-right: 2px">x</span>{{ count }}
        </v-col>
      </v-row>
    </v-list-item-content>
    <v-overlay absolute :value="isOverlay">
      <v-btn
        color="blue-grey lighten-5"
        rounded
        small
        @click.stop="$emit('minus-btn-click')"
      >
        <v-icon color="red accent-4">mdi-minus</v-icon>
      </v-btn>
      <v-btn
        color="blue-grey darken-4"
        style="text-transform: none"
        height="30"
        :ripple="false"
        ><span style="font-size: 16px">x{{ count }}</span></v-btn
      >
      <v-btn
        color="blue-grey lighten-5"
        rounded
        small
        @click.stop="$emit('plus-btn-click')"
        ><v-icon color="light-blue accent-4">mdi-plus</v-icon></v-btn
      >
    </v-overlay>
  </v-list-item>
</template>

<script>
export default {
  props: {
    cardId: {
      type: String,
      required: true,
    },
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
    imageUrl: {
      type: String,
      required: true,
    },
    count: {
      type: Number,
      required: true,
    },
    overlayId: {
      type: String,
      required: false,
      default: null,
    },
  },
  computed: {
    isOverlay() {
      return this.cardId === this.overlayId
    },
  },
}
</script>

<style>
.list-title {
  color: rgba(0, 0, 0, 0.6);
  font-size: 0.75rem;
}
.list-unit-name {
  font-size: 0.875rem;
}
</style>
