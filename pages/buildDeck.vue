<template>
  <v-container>
    <v-navigation-drawer v-model="searchDrawer" app clipped width="400">
      <v-container>
        <v-tabs v-model="tab" grow>
          <v-tab>ALL</v-tab>
          <v-tab><v-icon>mdi-bookmark-multiple</v-icon></v-tab>
        </v-tabs>
        <v-container>
          <v-select
            v-model="selectedSymbol"
            :items="selectItems"
            :item-color="selectItems.color"
            label="シンボルで絞り込む"
            prepend-inner-icon="mdi-filter"
            item-text="symbol"
            item-value="symbol"
            @change="getSymbolFilterCardsSnapshot(selectedSymbol)"
          ></v-select>
        </v-container>
        <v-autocomplete
          v-model="unitNameFilter"
          :items="unitNames"
          label="ユニット名で検索"
          prepend-inner-icon="mdi-database-search"
          clearable
          outlined
          @input="filterUnitName(unitNameFilter)"
        >
        </v-autocomplete>
        <v-tabs-items v-model="tab">
          <v-tab-item>
            <v-list height="400" class="overflow-y-auto" outlined>
              <template v-for="(card, index) in cardList">
                <v-list-item
                  :key="card._id"
                  :class="card.color"
                  three-line
                  @click.prevent="cards.push(card)"
                >
                  <v-list-item-avatar>
                    <v-img :src="card.avatar" />
                  </v-list-item-avatar>
                  <v-list-item-content>
                    <v-list-item-subtitle
                      v-text="card._id"
                    ></v-list-item-subtitle>
                    <v-list-item-subtitle
                      v-text="card.title"
                    ></v-list-item-subtitle>
                    <v-list-item-title
                      v-text="card.unitName"
                    ></v-list-item-title>
                  </v-list-item-content>
                  <v-list-item-action>
                    <v-btn outlined>
                      <v-icon @click.prevent="markCards.push(card)"
                        >mdi-star</v-icon
                      >
                    </v-btn>
                  </v-list-item-action>
                </v-list-item>
                <v-divider
                  v-if="index < cardList.length - 1"
                  :key="index"
                ></v-divider>
              </template>
              <infinite-loading
                ref="infiniteLoading"
                spinner="spiral"
                @infinite="infiniteHandler"
              >
                <span slot="no-more">No More Cards</span>
                <span slot="no-results">No Data</span>
              </infinite-loading>
            </v-list>
          </v-tab-item>
          <v-tab-item>
            <v-list height="400" class="overflow-y-auto">
              <v-list-item
                v-for="card in markCards"
                :key="card._id"
                @click="cards.push(card)"
              >
                <v-list-item-avatar>
                  <v-img :src="card.avatar" />
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-subtitle
                    v-text="card._id"
                  ></v-list-item-subtitle>
                  <v-list-item-subtitle
                    v-text="card.title"
                  ></v-list-item-subtitle>
                  <v-list-item-title v-text="card.unitName"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-tab-item>
        </v-tabs-items>
      </v-container>
    </v-navigation-drawer>

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
          <v-btn class="primary" width="100" @click="shareDeck">ツイート</v-btn>
          <v-btn class="info" width="100" @click="saveDeck">保存</v-btn>
        </div>
      </div>
    </div>
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
        :img="card.image"
      ></PickedCard>
    </draggable>
  </v-container>
</template>

<script>
import draggable from 'vuedraggable'
import InfiniteLoading from 'vue-infinite-loading'
export default {
  components: {
    draggable,
    InfiniteLoading,
  },
  data() {
    return {
      tab: null,
      deckName: '',
      searchDrawer: null,
      nextPage: null,
      lastCard: null,
      selectedSymbol: '指定なし',
      unitNameFilter: '',
      unitNames: ['マルス', 'シーダ', 'ジェイガン'],
      selectItems: [
        {
          name: '全',
          symbol: '指定なし',
          color: 'grey lighten-1',
        },
        {
          name: '無',
          symbol: '（なし）',
          color: 'grey',
        },
        {
          name: '赤',
          symbol: '光の剣',
          color: 'red',
        },
        {
          name: '青',
          symbol: '聖痕',
          color: 'blue',
        },
        {
          name: '白',
          symbol: '白夜',
          color: 'grey lighten-2',
        },
        {
          name: '黒',
          symbol: '暗夜',
          color: 'black',
        },
        {
          name: '緑',
          symbol: 'メダリオン',
          color: 'green',
        },
        {
          name: '紫',
          symbol: '神器',
          color: 'purple',
        },
        {
          name: '黄',
          symbol: '聖戦旗',
          color: 'orange',
        },
        {
          name: '茶',
          symbol: '女神紋',
          color: 'brown',
        },
      ],
      cards: [],
      markCards: [],
      cardList: [],
    }
  },
  async created() {
    await this.getAllCardsSnapshot()
    this.displayCards()
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

      if (newIndex > oldIndex) {
        // 後ろにカードを移動した場合

        // 配列の順序をreverseして、末尾から探索できるようにしておく
        // これにより、ドラッグして移動したカードが元より後ろの順で検知される
        this.cards.reverse()

        const cardObjects = this.toCardObjects(this.cards)
        this.cards = this.toArrayCards(cardObjects)
        // 逆順にしたものを元の順に戻す
        this.cards.reverse()
      } else if (newIndex < oldIndex) {
        // 前にカードを移動した場合

        const cardObjects = this.toCardObjects(this.cards)
        this.cards = this.toArrayCards(cardObjects)
      }
    },
    toCardObjects(cards) {
      // 各カードがどの順で何枚入っているかを格納する配列
      // obj{ img: String, count: Int}[]
      const result = []

      // カードの配列を頭から探索
      cards.forEach((card) => {
        // 種類順の配列(result)にあるカードかどうか、オブジェクトのimgキーを参照して確認する
        const isCardInObjects = result.filter((obj) => obj.img === card)

        // 種類順の配列に含まれているかどうか
        if (isCardInObjects.length === 0) {
          // 新規のカードの場合

          // カードのオブジェクトをresultに新規追加する
          result.push({ img: card, count: 1 })
        } else {
          // 既存のカードの場合

          // 該当のオブジェクトのcountを1増やす
          const objectIndex = result.findIndex((obj) => obj.img === card)
          result[objectIndex].count++
        }
      })
      return result
    },
    toArrayCards(objects) {
      // 一覧で表示するカードの配列
      const result = []

      objects.forEach((obj) => {
        for (let i = 0; i < obj.count; ++i) {
          result.push(obj.img)
        }
      })
      return result
    },
    async getAllCardsSnapshot() {
      if (this.lastCard) {
        this.nextPage = await this.$firestore
          .collection('Cards')
          .startAfter(this.lastCard)
          .limit(10)
          .get()
      } else {
        this.nextPage = await this.$firestore
          .collection('Cards')
          .limit(10)
          .get()
      }
      this.lastCard = this.nextPage.docs[this.nextPage.size - 1]
    },
    displayCards() {
      const cardData = this.nextPage.docs.map((doc) => {
        const result = doc.data()
        switch (result.symbol2) {
          case '聖痕':
            result.color = 'skyblue'
            break
          case '暗夜':
            result.color = 'pink'
            break
          default:
            switch (result.symbol1) {
              case '光の剣':
                result.color = 'red lighten-3'
                break
              case '聖痕':
                result.color = 'blue accent-1'
                break
              case '白夜':
                result.color = 'grey lighten-4'
                break
              case '暗夜':
                result.color = 'grey lighten-1'
                break
              case 'メダリオン':
                result.color = 'green lighten-3'
                break
              case '神器':
                result.color = 'deep-purple lighten-3'
                break
              case '聖戦旗':
                result.color = 'amber lighten-4'
                break
              case '女神紋':
                result.color = 'brown lighten-3'
                break
            }
        }
        return result
      })
      cardData.forEach((card) => {
        card.image = require('~/static/img/B01/B01-001SR.png')
        this.cardList.push(card)
      })
      return cardData
    },
    infiniteHandler($state) {
      console.log('inifinite')
      setTimeout(async () => {
        await this.getAllCardsSnapshot()
        this.displayCards()
        this.displayCards.length <= 10 ? $state.loaded() : $state.complete()
      }, 1000)
    },
    filterUnitName(unitName) {
      this.cardList.filter((card) => card.unitName === unitName)
    },
    async getSymbolFilterCardsSnapshot(symbol) {
      this.nextPage = await this.$firestore
        .collection('Cards')
        .where('symbol1', '==', symbol)
        .limit(10)
        .get()
      this.lastCard = this.nextPage.docs[this.nextPage.size - 1]
      this.cardList = []
      this.displayCards()
    },
  },
}
</script>
