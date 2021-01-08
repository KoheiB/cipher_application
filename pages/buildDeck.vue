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
            @change="onMoveCard"
          >
            <PickedCard
              v-for="(card, i) in cards"
              :key="i"
              :img="card"
            ></PickedCard>
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
        require('@/static/img/S10/S10-001ST.png'),
        require('@/static/img/S10/S10-001ST.png'),
        require('@/static/img/S10/S10-001ST.png'),
        require('@/static/img/S10/S10-001ST.png'),
        require('@/static/img/S10/S10-002ST.png'),
        require('@/static/img/S10/S10-002ST.png'),
        require('@/static/img/S10/S10-002ST.png'),
        require('@/static/img/S10/S10-002ST.png'),
        require('@/static/img/S10/S10-003ST.png'),
        require('@/static/img/S10/S10-003ST.png'),
        require('@/static/img/S10/S10-003ST.png'),
        require('@/static/img/S10/S10-003ST.png'),
        require('@/static/img/S10/S10-004ST.png'),
        require('@/static/img/S10/S10-004ST.png'),
        require('@/static/img/S10/S10-004ST.png'),
        require('@/static/img/S10/S10-004ST.png'),
        require('@/static/img/S10/S10-005ST.png'),
        require('@/static/img/S10/S10-005ST.png'),
        require('@/static/img/S10/S10-005ST.png'),
        require('@/static/img/S10/S10-005ST.png'),
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
    // 1枚のカードをドラッグした際、同じ種類のカードの順序をまとめて入れ替えるためのメソッド
    // 一旦、カードの配列を各カードの順序と枚数の情報に変換して並べなおす
    onMoveCard(event) {
      const newIndex = event.moved.newIndex
      const oldIndex = event.moved.oldIndex

      // 各カードがどの順で何枚入っているかを格納する配列
      // obj{ img: String, count: Int}[]
      const cardObjects = []

      // cardObjectsの内容をもとにカード情報をソートして格納する配列
      // string[]
      const sortedCards = []

      if (newIndex > oldIndex) {
        // 後ろにカードを移動した場合

        // 配列の順序をreverseして、末尾から探索できるようにしておく
        // これにより、ドラッグして移動したカードが元より後ろの順で検知される
        this.cards.reverse()

        // カードの配列を末尾から探索
        this.cards.forEach((card) => {
          // 種類順の配列(cardObjects)にあるカードかどうか、オブジェクトのimgキーを参照して確認する
          const isCardInObjects = cardObjects.filter((obj) => {
            return obj.img === card
          })

          if (isCardInObjects.length === 0) {
            // 新しい種類のカードの場合、カードのオブジェクトをcardObjectsに追加する
            cardObjects.push({ img: card, count: 1 })
          } else {
            // 既存カードの場合、該当オブジェクトのcountを1増やす
            const objectIndex = cardObjects.findIndex((obj) => {
              return obj.img === card
            })
            cardObjects[objectIndex].count++
          }
        })

        // 逆順にしたものを元の順に戻す
        cardObjects.reverse()

        // 種類順の配列をカードに変換
        cardObjects.forEach((obj) => {
          for (let i = 0; i < obj.count; ++i) {
            sortedCards.push(obj.img)
          }
        })
        this.cards = sortedCards
      } else if (newIndex < oldIndex) {
        // 前にカードを移動した場合

        // カードの配列を頭から探索
        this.cards.forEach((card) => {
          // 種類順の配列(cardObjects)にあるカードかどうか、オブジェクトのimgキーを参照して確認する
          const isCardInObjects = cardObjects.filter((obj) => {
            return obj.img === card
          })

          if (isCardInObjects.length === 0) {
            // 新しい種類のカードの場合、カードのオブジェクトをcardObjectsに追加する
            cardObjects.push({ img: card, count: 1 })
          } else {
            // 既存カードの場合、該当オブジェクトのcountを1増やす
            const objectIndex = cardObjects.findIndex((obj) => {
              return obj.img === card
            })
            cardObjects[objectIndex].count++
          }
        })

        // 種類順の配列をカードに変換
        cardObjects.forEach((obj) => {
          for (let i = 0; i < obj.count; ++i) {
            sortedCards.push(obj.img)
          }
        })
        this.cards = sortedCards
      }
    },
  },
}
</script>

<style>
.v-radio-wrapper {
  margin-bottom: 10px;
}
</style>
