<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="3">
        <v-tabs v-model="tab" grow>
          <v-tab>ALL</v-tab>
          <v-tab><v-icon>mdi-bookmark-multiple</v-icon></v-tab>
        </v-tabs>
        <div class="white">
          <v-radio-group v-model="selectedRadio" mandatory row>
            <div class="d-flex flex-wrap flex-row">
              <v-flex
                v-for="radioItem in radioItems"
                :key="radioItem.color"
                md3
              >
                <v-radio
                  class="v-radio-wrapper"
                  :name="radioItem.name"
                  :label="radioItem.name"
                  :color="radioItem.color"
                ></v-radio>
              </v-flex>
            </div>
          </v-radio-group>
        </div>
        <v-form>
          <v-text-field
            class="mt-2"
            solo
            append-icon="mdi-magnify"
            placeholder="ユニット名で検索"
          ></v-text-field>
        </v-form>
        <v-tabs-items v-model="tab">
          <v-tab-item>
            <v-card>全てのカード</v-card>
          </v-tab-item>
          <v-tab-item>
            <v-card>お気に入りカード</v-card>
          </v-tab-item>
        </v-tabs-items>
      </v-col>
      <v-col cols="12" sm="9">
        <div class="d-flex justify-space-between">
          <v-form
            v-model="deckName"
            class="w-20 d-flex align-center"
            @submit.prevent
          >
            <v-text-field type="text" label="DeckName"></v-text-field>
          </v-form>
          <div class="d-flex align-center">
            <div>
              <v-btn class="primary" width="100" @click="shareDeck"
                >ツイート</v-btn
              >
              <v-btn class="info" width="100" @click="saveDeck">保存</v-btn>
            </div>
          </div>
        </div>
        <v-card>
          <draggable
            v-model="cards"
            class="d-flex flex-wrap"
            group="cards"
            :animation="200"
            @start="drag = true"
            @end="drag = false"
            @change="onChange"
          >
            <Card
              v-for="(card, i) in cards"
              :key="i"
              :image="card.image"
            ></Card>
          </draggable>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import draggable from 'vuedraggable'
export default {
  components: {
    draggable,
  },
  data() {
    return {
      tab: null,
      deckName: '',
      selectedRadio: 0,
      radioItems: [
        {
          name: '全',
          color: 'grey lighten-1',
        },
        {
          name: '無',
          color: 'grey',
        },
        {
          name: '赤',
          color: 'red',
        },
        {
          name: '青',
          color: 'blue',
        },
        {
          name: '白',
          color: 'grey lighten-2',
        },
        {
          name: '黒',
          color: 'black',
        },
        {
          name: '緑',
          color: 'green',
        },
        {
          name: '紫',
          color: 'purple',
        },
        {
          name: '黄',
          color: 'orange',
        },
        {
          name: '茶',
          color: 'brown',
        },
      ],
      cards: [
        { image: require('@/static/img/S10/S10-001ST.png') },
        { image: require('@/static/img/S10/S10-001ST.png') },
        { image: require('@/static/img/S10/S10-001ST.png') },
        { image: require('@/static/img/S10/S10-001ST.png') },
        { image: require('@/static/img/S10/S10-002ST.png') },
        { image: require('@/static/img/S10/S10-002ST.png') },
        { image: require('@/static/img/S10/S10-002ST.png') },
        { image: require('@/static/img/S10/S10-002ST.png') },
        { image: require('@/static/img/S10/S10-003ST.png') },
        { image: require('@/static/img/S10/S10-003ST.png') },
        { image: require('@/static/img/S10/S10-003ST.png') },
        { image: require('@/static/img/S10/S10-003ST.png') },
        { image: require('@/static/img/S10/S10-004ST.png') },
        { image: require('@/static/img/S10/S10-004ST.png') },
        { image: require('@/static/img/S10/S10-004ST.png') },
        { image: require('@/static/img/S10/S10-004ST.png') },
        { image: require('@/static/img/S10/S10-005ST.png') },
        { image: require('@/static/img/S10/S10-005ST.png') },
        { image: require('@/static/img/S10/S10-005ST.png') },
        { image: require('@/static/img/S10/S10-005ST.png') },
      ],
    }
  },
  methods: {
    saveDeck() {
      console.log('saved')
    },
    shareDeck() {
      console.log('shared')
    },
    onChange(event) {
      const imgUrl = event.moved.element.image
      const newIndex = event.moved.newIndex
      console.log(imgUrl)
      const newArray = this.cards.map((card) => card)
      const moveCardsArray = this.cards.filter((card) => {
        return card.image === imgUrl
      })
      this.cards.forEach((card) => {
        if (card.image === imgUrl) {
        }
      })
      this.cards = newArray
      this.cards = newArray.filter((card) => {
        return card.image !== 'move'
      })
    },
  },
}
</script>

<style>
.v-radio-wrapper {
  margin-bottom: 10px;
}
</style>
