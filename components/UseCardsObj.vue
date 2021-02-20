<template>
  <v-list-item
    class="px-0 mr-8 ml-2"
    :class="color"
    style="margin-bottom: 1px; min-height: 38px"
    :ripple="false"
    @click="$emit('card-list-click', cardId)"
  >
    <div
      class="px-0 mx-1 blue-grey darken-3 white--text font-weight-bold rounded-xl d-flex justify-center align-center"
      style="width: 30px; height: 30px"
    >
      <span style="font-size: 16px">{{ sortieCost }}</span>
    </div>
    <v-list-item-content class="py-0 d-flex flex-nowrap" style="height: 38px">
      <v-list-item-title>
        <span class="list-title font-weight-bold">{{ title }}</span>
        <br />
        <span class="list-unit-name font-weight-bold">{{ unitName }}</span>
      </v-list-item-title>
    </v-list-item-content>
    <v-list-item-avatar class="ma-0" tile height="38" width="72">
      <v-img :src="imageUrl" position="top">
        <div class="fill-height red-gradation" />
      </v-img>
    </v-list-item-avatar>
    <div
      class="px-0 blue-grey darken-4 white--text font-weight-bold d-flex justify-center align-center"
      style="height: 38px; width: 38px"
    >
      <span style="font-size: 16px">x{{ count }}</span>
    </div>
    <v-overlay absolute :value="isOverlay">
      <v-btn
        color="blue-grey lighten-4"
        style="text-transform: none"
        height="30"
        @click.stop="$emit('plus-btn-click')"
        ><v-icon color="black">mdi-magnify</v-icon></v-btn
      >
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
    sortieCost: {
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
.red-gradation {
  background-image: linear-gradient(
    90deg,
    rgb(109, 213, 208) 30%,
    rgba(109, 213, 208, 0) 70%
  );
}
</style>
