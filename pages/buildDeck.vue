<template>
  <v-container>
    <!--▼ 検索ドロワー ****************************************▼-->
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      width="90%"
      style="max-width: 400px"
      mobile-breakpoint="500"
    >
      <!--▼ ユニット名フィルター ****************************************▼-->
      <v-container class="pb-0 pt-4" style="height: 10vh">
        <v-autocomplete
          v-model="unitNameFilter"
          :items="unitNameFilterItems"
          :filter="filterObject"
          item-text="name"
          label="ユニット名で検索"
          prepend-inner-icon="mdi-human-handsdown"
          autofocus
          dense
          clearable
          outlined
          @change="changeFilter()"
        >
        </v-autocomplete>
      </v-container>
      <!--▲ ユニット名フィルター ****************************************▲-->

      <!--▼ シンボルフィルター ****************************************▼-->
      <v-container class="pb-0 pt-4" style="height: 10vh">
        <v-select
          v-model="symbolFilter"
          :items="symbolItems"
          item-text="name"
          label="シンボルで絞り込み"
          prepend-inner-icon="mdi-filter"
          dense
          clearable
          outlined
          @change="changeFilter()"
        ></v-select>
      </v-container>
      <!--▲ シンボルフィルター ****************************************▲-->

      <!--▼ タブ選択画面 ****************************************▼-->
      <v-tabs v-model="tab" grow>
        <v-tab style="max-width: 50%"
          ><v-icon class="pr-1">mdi-cards</v-icon>Search</v-tab
        >
        <v-tab style="max-width: 50%"
          ><v-icon class="pr-1">mdi-bookmark-multiple</v-icon>Bookmark</v-tab
        >
      </v-tabs>
      <!--▲ タブ選択画面 ****************************************▲-->

      <v-tabs-items v-model="tab">
        <!--▼ タブ内容1:Search ****************************************▼-->
        <v-tab-item>
          <v-list class="py-0 overflow-y-auto" height="65vh" outlined>
            <template v-for="(card, index) in filteredCards">
              <v-list-item
                :key="'search-' + card._id"
                :class="card.color"
                class="pl-0"
                three-line
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
                <v-list-item-action class="d-flex flex-column">
                  <v-btn
                    class="mb-1"
                    outlined
                    width="100%"
                    small
                    @click="addCard(card)"
                    >１枚追加</v-btn
                  >
                  <v-btn
                    class="mb-1"
                    outlined
                    width="100%"
                    small
                    @click="addFourCards(card)"
                    >４枚追加</v-btn
                  >
                  <v-btn
                    outlined
                    width="100%"
                    small
                    @click.prevent="markCards.push(card)"
                  >
                    <v-icon>mdi-bookmark</v-icon>キープ
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
              <v-divider
                v-if="index < filteredCards.length - 1"
                :key="index"
              ></v-divider>
            </template>
            <infinite-loading
              ref="filteredCardsInfiniteLoading"
              spinner="spiral"
              @infinite="filteredCardsInfiniteHandler"
            >
              <span slot="no-more"></span>
              <span slot="no-results"></span>
            </infinite-loading>
          </v-list>
        </v-tab-item>
        <!--▲ タブ内容1:Search ****************************************▲-->

        <!--TODO▼ タブ内容2:Bookmark ****************************************▼-->
        <v-tab-item>
          <v-list class="py-0 overflow-y-auto" height="450" outlined>
            <template v-for="(card, index) in markCards">
              <v-list-item
                :key="'mark-' + card._id"
                :class="card.color"
                class="pl-0"
                three-line
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
                <v-list-item-action class="d-flex flex-column">
                  <v-btn
                    class="mb-1"
                    outlined
                    width="100%"
                    small
                    @click="myDeckCards.push(card)"
                    >１枚追加</v-btn
                  >
                  <v-btn class="mb-1" outlined width="100%" small
                    >４枚追加</v-btn
                  >
                  <v-btn
                    outlined
                    width="100%"
                    small
                    @click.prevent="markCards.push(card)"
                  >
                    <v-icon>mdi-delete</v-icon>削除
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
              <v-divider
                v-if="index < filteredCards.length - 1"
                :key="index"
              ></v-divider>
            </template>
            <!-- TODO<infinite-loading
              ref="markCardsInfiniteLoading"
              spinner="spiral"
              @infinite="markCardsInfiniteHandler"
            >
              <span slot="no-more">No More Cards</span>
              <span slot="no-results">No More Cards</span>
            </infinite-loading> -->
          </v-list>
        </v-tab-item>
        <!--▲ タブ内容2:Bookmark ****************************************▲-->
      </v-tabs-items>
    </v-navigation-drawer>
    <!--▲ 検索ドロワー ****************************************▲-->

    <!--▼ メイン画面 ****************************************▼-->
    <v-container class="">
      <v-form @submit.prevent>
        <v-text-field
          v-model="myDeckName"
          type="text"
          label="myDeckName"
        ></v-text-field>
      </v-form>
      <v-layout class="d-flex align-center">
        <v-btn class="primary" width="25%" tile @click="shareDeck"
          >ツイート</v-btn
        >
        <v-btn class="info" width="25%" tile @click="saveDeck">保存</v-btn>
        <v-btn class="info" width="25%" tile @click="loadDeck">ロード</v-btn>
        <v-btn width="25%" tile @click="drawer = !drawer">ドロワー</v-btn>
      </v-layout>
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
        v-for="(card, index) in myDeckCardView"
        :key="index"
        class="hidden-mobile-and-down"
        :img="card.image"
      ></PickedCard>
    </draggable>
    <v-list>
      <draggable
        v-model="myDeckCards"
        class=""
        group="myDeckCardList"
        :animation="200"
        @start="drag = true"
        @end="drag = false"
        @change="onMoveCard"
      >
        <PickedCardList
          v-for="(card, index) in myDeckCards"
          :key="2 + index"
          class="d-mobile-none"
          :img="card.card.image"
          :unit-name="card.card.unitName"
          :title="card.card.title"
          :count="card.count"
          :symbols="card.card.symbols"
          :color="card.color"
          @on-click="onClick(card)"
        >
        </PickedCardList>
      </draggable>
    </v-list>
    {{ myDeckCards }}
    {{ myDeckCardView }}
    <!-- <v-img :src="require('@/static/img/B01/B01-001SR.png')">
      <div class="fill-height gradient"></div>
    </v-img> -->
  </v-container>
  <!--▲ メイン画面 ****************************************▲-->
</template>

<script>
import draggable from 'vuedraggable'
import InfiniteLoading from 'vue-infinite-loading'
import unitNameFilterItems from '../mixins/UnitNameFilterItems'
import symbolItems from '../mixins/SymbolItems'
export default {
  components: {
    draggable,
    InfiniteLoading,
  },
  mixins: [unitNameFilterItems, symbolItems],
  data() {
    return {
      myDeckName: '',
      myDeckCards: [],
      markCards: [],
      filteredCards: [],
      useCardsRef: '',

      // UIコンポーネント関連
      drawer: null,
      tab: null,

      // ページネーション関連
      nextFilteredCards: null,
      lastFilteredCard: null,

      // ユニット名フィルター関連
      unitNameFilter: undefined,

      // シンボルフィルター関連
      symbolFilter: undefined,
      // symbolItems: [
      //   'なし',
      //   '光の剣',
      //   '聖痕',
      //   '白夜',
      //   '暗夜',
      //   'メダリオン',
      //   '神器',
      //   '聖戦旗',
      //   '女神紋',
      // ],
    }
  },
  computed: {
    myDeckCardView() {
      const result = []
      this.myDeckCards.forEach((cardObject) => {
        const card = {
          id: cardObject.card.id,
          image: cardObject.card.image,
        }
        for (let i = 0; i < cardObject.count; i++) {
          result.push(card)
        }
      })
      return result
    },
  },
  methods: {
    saveDeck() {
      if (this.useCardsRef === '') {
        console.log('ref')
        this.useCardsRef = this.$firestore
          .collection('Users')
          .doc()
          .collection('Decks')
          .doc()
          .collection('UseCards')
      }
      this.myDeckCards.forEach((cardObject, index) => {
        this.useCardsRef.doc().set(
          {
            card: {
              id: cardObject.card.id,
              title: cardObject.card.title,
              unitName: cardObject.card.unitName,
              symbols: cardObject.card.symbols,
              image: cardObject.card.image,
            },
            count: cardObject.count,
            displayOrder: index,
          },
          { merge: true }
        )
      })
      alert('saved')
    },
    async loadDeck() {
      const snapshot = await this.useCardsRef
        .orderBy('displayOrder', 'asc')
        .get()
      const data = snapshot.docs.map((snapshot) => {
        const result = {
          card: {
            _id: snapshot.data().card.id,
            image: snapshot.data().card.image,
            symbols: snapshot.data().card.symbols,
            title: snapshot.data().card.title,
            unitName: snapshot.data().card.unitName,
          },
          count: snapshot.data().count,
        }
        console.log(result)
        this.addSymbolColorData(snapshot.data().card.symbols, result)
        return result
      })
      this.myDeckCards = data
      alert('loaded')
    },
    shareDeck() {
      console.log('shared')
    },
    // ▼ マイデッキビューに関するメソッド ****************************************▼
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
    // ▲ マイデッキビューに関するメソッド ****************************************▲

    // ▼ 検索ドロワーに関するメソッド ****************************************▼
    // フィルターを変更した時の処理
    async changeFilter() {
      await this.resetFilter()
      await this.getFilteredCardsSnapshot()
      await this.setLastFilteredCard()
      await this.displayCards()
      await this.$refs.filteredCardsInfiniteLoading.stateChanger.reset()
    },
    resetFilter() {
      this.filteredCards = []
      this.nextFilteredCards = null
      this.lastFilteredCard = null
    },
    // フィルターのパターンによって異なるスナップショットを取得
    async getFilteredCardsSnapshot() {
      switch (this.unitNameFilter) {
        case undefined:
          switch (this.symbolFilter) {
            // ユニット名:false、シンボル:false
            case undefined:
              await this.getNoFilteredCardsSnapshot()
              break
            // ユニット名:false、シンボル:true
            default:
              await this.getSymbolFilteredCardsSnapshot()
          }
          break
        default:
          switch (this.symbolFilter) {
            // ユニット名:true、シンボル:false
            case undefined:
              await this.getUnitNameFilteredCardsSnapshot()
              break
            // ユニット名:true、シンボル:true
            default:
              await this.getUnitNameAndSymbolFilteredCardsSnapshot()
          }
      }
    },
    // スナップショットを取得するメソッド4パターン
    async getNoFilteredCardsSnapshot() {
      if (this.lastFilteredCard) {
        this.nextFilteredCards = await this.$firestore
          .collection('Cards')
          .startAfter(this.lastFilteredCard)
          .limit(10)
          .get()
      } else {
        this.nextFilteredCards = await this.$firestore
          .collection('Cards')
          .limit(10)
          .get()
      }
    },
    async getUnitNameFilteredCardsSnapshot() {
      if (this.lastFilteredCard) {
        this.nextFilteredCards = await this.$firestore
          .collection('Cards')
          .where('unitName', '==', this.unitNameFilter)
          .startAfter(this.lastFilteredCard)
          .limit(10)
          .get()
      } else {
        this.nextFilteredCards = await this.$firestore
          .collection('Cards')
          .where('unitName', '==', this.unitNameFilter)
          .limit(10)
          .get()
      }
    },
    async getSymbolFilteredCardsSnapshot() {
      if (this.lastFilteredCard) {
        this.nextFilteredCards = await this.$firestore
          .collection('Cards')
          .where('symbols', 'array-contains', this.symbolFilter)
          .startAfter(this.lastFilteredCard)
          .limit(10)
          .get()
      } else {
        this.nextFilteredCards = await this.$firestore
          .collection('Cards')
          .where('symbols', 'array-contains', this.symbolFilter)
          .limit(10)
          .get()
      }
    },
    async getUnitNameAndSymbolFilteredCardsSnapshot() {
      if (this.lastFilteredCard) {
        this.nextFilteredCards = await this.$firestore
          .collection('Cards')
          .where('unitName', '==', this.unitNameFilter)
          .where('symbols', 'array-contains', this.symbolFilter)
          .startAfter(this.lastFilteredCard)
          .limit(10)
          .get()
      } else {
        this.nextFilteredCards = await this.$firestore
          .collection('Cards')
          .where('unitName', '==', this.unitNameFilter)
          .where('symbols', 'array-contains', this.symbolFilter)
          .limit(10)
          .get()
      }
    },
    // 無限スクロールのために、最後に表示されているカードのスナップショットを取得しておく
    setLastFilteredCard() {
      this.lastFilteredCard = this.nextFilteredCards.docs[
        this.nextFilteredCards.size - 1
      ]
    },
    // 取得した次に表示するカードのスナップショットのデータをクライアントサイドジョインののちに表示
    displayCards() {
      const result = this.nextFilteredCards.docs.map((doc) => {
        const docData = doc.data()
        this.addSymbolColorData(docData.symbols, docData)
        return docData
      })
      result.forEach((card) => {
        const newId = card._id.replace('+', 'plus')
        const imageUrl = '/img/' + card.recording + '/' + newId + '.png'
        card.image = imageUrl
        this.filteredCards.push(card)
      })
      return result
    },
    // シンボルにより背景色をカードのデータに追加するメソッド
    addSymbolColorData(symbols, data) {
      switch (symbols[1]) {
        case '聖痕':
          data.color = 'red-blue'
          break
        case '暗夜':
          data.color = 'black-white'
          break
        default:
          switch (symbols[0]) {
            case 'なし':
              data.color = 'cyan lighten-5'
              break
            case '光の剣':
              data.color = 'red lighten-3'
              break
            case '聖痕':
              data.color = 'blue lighten-4'
              break
            case '白夜':
              data.color = 'grey lighten-4'
              break
            case '暗夜':
              data.color = 'grey lighten-1'
              break
            case 'メダリオン':
              data.color = 'green lighten-3'
              break
            case '神器':
              data.color = 'deep-purple lighten-3'
              break
            case '聖戦旗':
              data.color = 'yellow lighten-4'
              break
            case '女神紋':
              data.color = 'brown lighten-3'
              break
          }
      }
    },
    // サーチ無限スクロール
    filteredCardsInfiniteHandler($state) {
      setTimeout(async () => {
        await this.getFilteredCardsSnapshot()
        await this.setLastFilteredCard()
        await this.displayCards()
        // 取得したカードが10未満ならスクロール終了
        if (this.nextFilteredCards.size <= 9) {
          $state.complete()
        } else {
          $state.loaded()
        }
      }, 100)
    },
    // TODOマーク無限スクロール
    markCardsInfiniteHandler($state) {
      setTimeout(async () => {
        await this.getFilteredCardsSnapshot()
        await this.setLastFilteredCard()
        await this.displayCards()
        // 取得したカードが10未満ならスクロール終了
        if (this.nextFilteredCards.size < 10) {
          $state.complete()
        } else {
          $state.loaded()
        }
      }, 100)
    },
    // ▲ 検索ドロワーに関するメソッド ****************************************▲
    filterObject(item, queryText, itemText) {
      return (
        item.name
          .toLocaleLowerCase()
          .startsWith(queryText.toLocaleLowerCase()) ||
        item.hiragana
          .toLocaleLowerCase()
          .startsWith(queryText.toLocaleLowerCase())
      )
    },
    // TODOisMarked(card) {
    //   const result = this.myDeckCards.filter((myDeckCard) => {
    //     return card
    //   })
    //   if (result.length !== 0) {
    //     return true
    //   } else {
    //     return false
    //   }
    // },
    addCard(card) {
      const newId = card._id.replace('+', 'plus')
      const imageUrl = '/img/' + card.recording + '/' + newId + '.png'
      const result = {
        card: {
          id: card._id,
          title: card.title,
          unitName: card.unitName,
          symbols: card.symbols,
          image: imageUrl,
        },
        count: 1,
      }
      this.addSymbolColorData(card.symbols, result)

      const cardExists = this.myDeckCards.filter((useCard) => {
        return useCard.card.id === result.card.id
      })
      if (cardExists.length === 0) {
        this.myDeckCards.push(result)
      } else {
        const i = this.myDeckCards.indexOf(cardExists[0])
        this.myDeckCards[i].count++
      }
    },
    addFourCards(card) {
      for (let i = 0; i < 4; i++) {
        this.addCard(card)
      }
    },
    onClick(card) {
      card.count--
      const i = this.myDeckCards.indexOf(card)
      if (card.count === 0) {
        this.myDeckCards.splice(i, 1)
      }
    },
  },
}
</script>

<style>
.red-blue {
  background: rgb(239, 154, 154);
  background: linear-gradient(
    90deg,
    rgba(239, 154, 154, 1) 40%,
    rgba(187, 222, 251, 1) 60%
  );
}
.black-white {
  background: rgb(245, 245, 245);
  background: linear-gradient(
    90deg,
    rgba(189, 189, 189, 1) 40%,
    rgba(245, 245, 245, 1) 60%
  );
}
/* .gradient {
  background-image: linear-gradient(
    90deg,
    rgb(109, 213, 208) 30%,
    rgba(109, 213, 208, 0) 70%
  );
} */
</style>
