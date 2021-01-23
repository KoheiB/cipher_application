<template>
  <v-container>
    <!--▼ 検索ドロワー ****************************************▼-->
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      width="400"
      mobile-breakpoint="500"
    >
      <!--▼ シンボルフィルター ****************************************▼-->
      <v-container class="pb-0">
        <v-select
          v-model="symbolFilter"
          :items="symbolFilterItems"
          label="シンボルで絞り込み"
          prepend-inner-icon="mdi-filter"
          clearable
          outlined
          @change="getSymbolFilterCardsSnapshot(symbolFilter)"
        ></v-select>
      </v-container>
      <!--▲ シンボルフィルター ****************************************▲-->

      <!--▼ ユニット名フィルター ****************************************▼-->
      <v-container class="py-0">
        <v-autocomplete
          v-model="unitNameFilter"
          :items="unitNameFilterItems"
          label="ユニット名で絞り込み"
          prepend-inner-icon="mdi-database-search"
          clearable
          outlined
          @input="filterUnitName(unitNameFilter)"
        >
        </v-autocomplete>
      </v-container>
      <!--▲ ユニット名フィルター ****************************************▲-->

      <!--▼ タブ選択画面 ****************************************▼-->
      <v-tabs v-model="tab" grow>
        <v-tab><v-icon>mdi-cards</v-icon>All Cards</v-tab>
        <v-tab><v-icon>mdi-bookmark-multiple</v-icon>Bookmark</v-tab>
      </v-tabs>
      <!--▲ タブ選択画面 ****************************************▲-->

      <v-tabs-items v-model="tab">
        <!--▼ タブ内容1:All Cards ****************************************▼-->
        <v-tab-item>
          <v-list class="py-0 overflow-y-auto" height="450" outlined>
            <template v-for="(card, index) in filteredCards">
              <v-list-item
                :key="'all' + card._id"
                :class="card.color"
                class="pl-0"
                three-line
                @click.prevent="myDeckCards.push(card)"
              >
                <v-list-item-avatar
                  class="ma-0 mr-2"
                  tile
                  size="88"
                  height="100%"
                >
                  <v-img :src="card.image" />
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
                <v-list-item-action>
                  <v-btn outlined>
                    <v-icon @click.prevent="markCards.push(card)"
                      >mdi-bookmark</v-icon
                    >
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
              <v-divider
                v-if="index < filteredCards.length - 1"
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
        <!--▲ タブ内容1:All Cards ****************************************▲-->

        <!--▼ タブ内容2:Bookmark ****************************************▼-->
        <v-tab-item>
          <v-list height="400" class="overflow-y-auto">
            <v-list-item
              v-for="card in markCards"
              :key="'mark' + card._id"
              @click="myDeckCards.push(card)"
            >
              <v-list-item-avatar>
                <v-img :src="card.image" />
              </v-list-item-avatar>
              <v-list-item-content>
                <v-list-item-subtitle v-text="card._id"></v-list-item-subtitle>
                <v-list-item-subtitle
                  v-text="card.title"
                ></v-list-item-subtitle>
                <v-list-item-title v-text="card.unitName"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-tab-item>
        <!--▲ タブ内容2:Bookmark ****************************************▲-->
      </v-tabs-items>
    </v-navigation-drawer>
    <!--▲ 検索ドロワー ****************************************▲-->

    <!--▼ メイン画面 ****************************************▼-->
    <v-container class="d-flex justify-space-between">
      <v-form
        v-model="myDeckName"
        class="w-20 d-flex align-center"
        @submit.prevent
      >
        <v-text-field type="text" label="myDeckName"></v-text-field>
      </v-form>
      <div class="d-flex align-center">
        <div>
          <v-btn class="primary" width="100" @click="shareDeck">ツイート</v-btn>
          <v-btn class="info" width="100" @click="saveDeck">保存</v-btn>
        </div>
      </div>
    </v-container>
    <draggable
      v-model="myDeckCards"
      class="d-flex flex-wrap"
      group="myDeckCards"
      :animation="200"
      @start="drag = true"
      @end="drag = false"
      @change="onMoveCard"
    >
      <PickedCard
        v-for="(card, index) in myDeckCards"
        :key="index"
        :img="card.image"
      ></PickedCard>
    </draggable>
    {{ myDeckCards }}
  </v-container>
  <!--▲ メイン画面 ****************************************▲-->
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
      myDeckCards: [],
      markCards: [],
      filteredCards: [],
      myDeckName: '',
      // UIコンポーネント
      drawer: null,
      tab: null,
      // ページネーション
      nextDisplayCards: null,
      lastDisplayCard: null,
      // シンボルフィルター
      symbolFilter: '',
      symbolFilterItems: [
        'なし',
        '光の剣',
        '聖痕',
        '白夜',
        '暗夜',
        'メダリオン',
        '神器',
        '聖戦旗',
        '女神紋',
      ],
      // ユニット名フィルター
      unitNameFilter: '',
      unitNameFilterItems: [
        'マルス',
        'シーダ',
        'クロム',
        'アルフォンス',
        'リョウマ',
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

      if (newIndex > oldIndex) {
        // 後ろにカードを移動した場合
        // 配列の順序をreverseして、末尾から探索できるようにしておく
        // これにより、ドラッグして移動したカードが元より後ろの順で検知される
        this.myDeckCards.reverse()

        const cardObjects = this.toCardObjects(this.myDeckCards)
        this.myDeckCards = this.toArrayCards(cardObjects)
        // 逆順にしたものを元の順に戻す
        this.myDeckCards.reverse()
      } else if (newIndex < oldIndex) {
        // 前にカードを移動した場合
        const cardObjects = this.toCardObjects(this.myDeckCards)
        this.myDeckCards = this.toArrayCards(cardObjects)
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
      if (this.lastDisplayCard) {
        this.nextDisplayCards = await this.$firestore
          .collection('Cards')
          .startAfter(this.lastDisplayCard)
          .limit(10)
          .get()
      } else {
        this.nextDisplayCards = await this.$firestore
          .collection('Cards')
          .limit(10)
          .get()
      }
      this.lastDisplayCard = this.nextDisplayCards.docs[
        this.nextDisplayCards.size - 1
      ]
    },
    displayCards() {
      const cardData = this.nextDisplayCards.docs.map((doc) => {
        const result = doc.data()
        switch (result.symbols[1]) {
          case '聖痕':
            result.color = 'skyblue'
            break
          case '暗夜':
            result.color = 'pink'
            break
          default:
            switch (result.symbols[0]) {
              case 'なし':
                result.color = 'cyan lighten-5'
                break
              case '光の剣':
                result.color = 'red lighten-3'
                break
              case '聖痕':
                result.color = 'blue lighten-4'
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
                result.color = 'yellow lighten-4'
                break
              case '女神紋':
                result.color = 'brown lighten-3'
                break
            }
        }
        return result
      })
      cardData.forEach((card) => {
        const newId = card._id.replace('+', 'plus')
        const imageUrl = '/img/' + card.recording + '/' + newId + '.png'
        card.image = imageUrl
        this.filteredCards.push(card)
      })
      return cardData
    },
    infiniteHandler($state) {
      setTimeout(async () => {
        await this.getAllCardsSnapshot()
        this.displayCards()
        this.displayCards.length <= 10 ? $state.loaded() : $state.complete()
      }, 500)
    },
    async filterUnitName(unitName) {
      if (!unitName) {
        this.getAllCardsSnapshot()
        this.displayCards()
        return
      }
      this.nextDisplayCards = await this.$firestore
        .collection('Cards')
        .where('unitName', '==', unitName)
        .limit(10)
        .get()
      this.lastDisplayCard = this.nextDisplayCards.docs[
        this.nextDisplayCards.size - 1
      ]
      this.filteredCards = []
      this.displayCards()
    },
    async getSymbolFilterCardsSnapshot(symbol) {
      if (!symbol) {
        console.log('clear filter')
        this.filteredCards = []
        this.lastDisplayCard = null
        this.nextDisplayCards = null
        await this.getAllCardsSnapshot()
        this.displayCards()
        return
      }
      this.nextDisplayCards = await this.$firestore
        .collection('Cards')
        .where('symbols', 'array-contains', symbol)
        .limit(10)
        .get()
      this.lastDisplayCard = this.nextDisplayCards.docs[
        this.nextDisplayCards.size - 1
      ]
      this.filteredCards = []
      this.displayCards()
    },
  },
}
</script>
