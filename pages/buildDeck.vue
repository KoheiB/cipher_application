<template>
  <v-container>
    <!--▼ 検索ドロワー ****************************************▼-->
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
      width="90%"
      style="max-width: 400px"
      :mobile-breakpoint="$vuetify.breakpoint.mobileBreakpoint"
    >
      <!--▼ ユニット名フィルター ****************************************▼-->
      <v-container class="pb-0 pt-4" style="height: 60px">
        <v-autocomplete
          v-model="unitNameFilter"
          :items="unitNameItems"
          :filter="checkUnitName"
          item-text="name"
          label="ユニット名"
          autofocus
          dense
          clearable
          outlined
          @change="searchCards()"
        />
      </v-container>
      <!--▲ ユニット名フィルター ****************************************▲-->

      <!--▼ シンボル/出撃コストフィルター ****************************************▼-->
      <v-container class="pb-0 pt-4 d-flex" style="height: 60px">
        <v-select
          v-model="symbolFilter"
          :items="symbolItems"
          item-text="name"
          style="width: 60%; padding-right: 1px"
          label="シンボル"
          dense
          clearable
          outlined
          @change="searchCards()"
        />
        <v-select
          v-model="sortieCostFilter"
          :items="sortieCostItems"
          style="width: 40%; padding-left: 1px"
          label="コスト"
          dense
          clearable
          outlined
          @change="searchCards()"
        />
      </v-container>
      <!--▲ シンボル/出撃コストフィルター ****************************************▲-->

      <!--▼ タブ選択画面 ****************************************▼-->
      <v-tabs v-model="tab" grow height="45px">
        <v-tab style="max-width: 50%"
          ><v-icon class="pr-1">mdi-cards</v-icon>Search</v-tab
        >
        <v-tab style="max-width: 50%"
          ><v-icon class="pr-1">mdi-bookmark-multiple</v-icon>Keep</v-tab
        >
      </v-tabs>
      <!--▲ タブ選択画面 ****************************************▲-->

      <v-tabs-items v-model="tab">
        <!--▼ タブ内容1:Search ****************************************▼-->
        <v-tab-item>
          <v-list
            class="py-0 overflow-y-auto"
            :height="
              // eslint-disable-next-line prettier/prettier
              $vuetify.breakpoint.mobile
                ? 'calc(100vh - 165px)'
                : 'calc(100vh - 165px - 48px)'
            "
            outlined
          >
            <template v-for="(card, index) in searchedCards">
              <v-list-item
                :key="'search-' + card.id"
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
                  <v-img :src="card.imageUrl" />
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-subtitle v-text="card.id" />
                  <v-list-item-subtitle v-text="card.title" />
                  <v-list-item-title v-text="card.unitName" />
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
                    @click.prevent="keepCards.push(card)"
                  >
                    <v-icon>mdi-bookmark</v-icon>キープ
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
              <v-divider v-if="index < searchedCards.length - 1" :key="index" />
            </template>
            <infinite-loading
              ref="searchedCardsInfiniteLoading"
              spinner="spiral"
              @infinite="searchedCardsInfiniteHandler"
            >
              <span slot="no-more" />
              <span slot="no-results" />
            </infinite-loading>
          </v-list>
        </v-tab-item>
        <!--▲ タブ内容1:Search ****************************************▲-->

        <!--TODO▼ タブ内容2:Keep ****************************************▼-->
        <v-tab-item>
          <v-list class="py-0 overflow-y-auto" height="450" outlined>
            <template v-for="(card, index) in keepCards">
              <v-list-item
                :key="'keep-' + card.id"
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
                  <v-img :src="card.imageUrl" />
                </v-list-item-avatar>
                <v-list-item-content>
                  <v-list-item-subtitle v-text="card.id" />
                  <v-list-item-subtitle v-text="card.title" />
                  <v-list-item-title v-text="card.unitName" />
                </v-list-item-content>
                <v-list-item-action class="d-flex flex-column">
                  <v-btn
                    class="mb-1"
                    outlined
                    width="100%"
                    small
                    @click="useCards.push(card)"
                    >１枚追加</v-btn
                  >
                  <v-btn class="mb-1" outlined width="100%" small
                    >４枚追加</v-btn
                  >
                  <v-btn
                    outlined
                    width="100%"
                    small
                    @click.prevent="keepCards.push(card)"
                  >
                    <v-icon>mdi-delete</v-icon>削除
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
              <v-divider v-if="index < searchedCards.length - 1" :key="index" />
            </template>
            <!-- TODO<infinite-loading
              ref="keepCardsInfiniteLoading"
              spinner="spiral"
              @infinite="keepCardsInfiniteHandler"
            >
              <span slot="no-more">No More Cards</span>
              <span slot="no-results">No More Cards</span>
            </infinite-loading> -->
          </v-list>
        </v-tab-item>
        <!--▲ タブ内容2:Keep ****************************************▲-->
      </v-tabs-items>
    </v-navigation-drawer>
    <!--▲ 検索ドロワー ****************************************▲-->

    <!--▼ メイン画面 ****************************************▼-->
    <v-container>
      <v-form @submit.prevent>
        <v-text-field v-model="deckName" type="text" label="deckName" />
      </v-form>
      <v-layout class="d-flex align-center">
        <v-btn class="primary" width="25%" tile @click="shareDeck"
          >ツイート</v-btn
        >
        <v-btn class="info" width="25%" tile @click="saveDeck">保存</v-btn>
        <v-btn class="info" width="25%" tile @click="loadDeck">ロード</v-btn>
        <v-btn width="25%" tile @click=";(drawer = !drawer), (overlayId = null)"
          >ドロワー</v-btn
        >
      </v-layout>
    </v-container>
    <draggable
      v-model="allUseCards"
      class="d-flex flex-wrap"
      group="allUseCards"
      :animation="200"
      @start="drag = true"
      @end="drag = false"
      @change="groupAllUseCards"
    >
      <UseCard
        v-for="(card, index) in allUseCards"
        :key="'allUseCard-' + card.id + '-' + index"
        class="hidden-mobile-and-down"
        :card-id="'allUseCard-' + card.id + '-' + index"
        :image-url="card.imageUrl"
      />
    </draggable>
    <v-list>
      <draggable
        v-model="useCards"
        group="useCards"
        :animation="200"
        @start="drag = true"
        @end="drag = false"
        @change="sortAllUseCards"
      >
        <UseCardObj
          v-for="card in useCards"
          :key="'useCard-' + card.info.id"
          class="d-mobile-none"
          :card-id="card.info.id"
          :title="card.info.title"
          :unit-name="card.info.unitName"
          :symbols="card.info.symbols"
          :color="card.info.color"
          :gradation="card.info.gradation"
          :sortie-cost="card.info.sortie_cost"
          :image-url="card.info.imageUrl"
          :count="card.count"
          :overlay-id="overlayId"
          @use-card-obj-plus-btn-click="incrementUseCardObjCount(card)"
          @use-card-obj-minus-btn-click="decrementUseCardObjCount(card)"
          @use-card-obj-list-click="changeCardCount"
        />
      </draggable>
    </v-list>
  </v-container>
  <!--▲ メイン画面 ****************************************▲-->
</template>

<script>
import draggable from 'vuedraggable'
import InfiniteLoading from 'vue-infinite-loading'
import {
  unitNameItems,
  symbolItems,
  sortieCostItems,
} from '../constant/constant'
export default {
  components: {
    draggable,
    InfiniteLoading,
  },
  data() {
    return {
      deckName: '',
      useCards: [],
      allUseCards: [],
      keepCards: [],
      useCardsRef: '',
      overlayId: null,

      // UIコンポーネント関連
      drawer: null,
      tab: null,

      // ▼ カード検索関連 ****************************************▼
      searchedCards: [],

      // ページネーション
      nextLoadCards: null,
      lastLoadCard: null,

      // ユニット名フィルター
      unitNameFilter: undefined,
      unitNameItems,

      // シンボルフィルター
      symbolFilter: undefined,
      symbolItems,

      // 出撃コストフィルター
      sortieCostFilter: undefined,
      sortieCostItems,
      // ▲ カード検索関連 ****************************************▲
    }
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
      this.useCards.forEach((cardObj, index) => {
        const card = cardObj.info
        this.useCardsRef.doc().set(
          {
            info: {
              id: card.id,
              title: card.title,
              unitName: card.unitName,
              symbols: card.symbols,
              recording: card.recording,
            },
            count: cardObj.count,
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
        const card = snapshot.data().info
        const result = {
          info: {
            id: card.id,
            title: card.title,
            unitName: card.unitName,
            symbols: card.symbols,
            recording: card.recording,
          },
          count: snapshot.data().count,
        }
        return result
      })
      this.useCards = data
      alert('loaded')
    },
    shareDeck() {
      console.log('shared')
    },
    // ▼ マイデッキビューに関するメソッド ****************************************▼
    // 1枚のカードをドラッグした際、同じ種類のカードの順序をまとめて入れ替えるためのメソッド
    // 一旦、カードの配列を各カードの順序と枚数の情報に変換して並べなおす
    groupAllUseCards(event) {
      const newIndex = event.moved.newIndex
      const oldIndex = event.moved.oldIndex

      if (newIndex > oldIndex) {
        // 後ろにカードを移動した場合
        // 配列の順序をreverseして、末尾から探索できるようにしておく
        // これにより、ドラッグして移動したカードが元より後ろの順で検知される
        this.allUseCards.reverse()
        this.sortUseCards()
        this.sortAllUseCards()
        // 逆順にしたものを元の順に戻す
        this.allUseCards.reverse()
      } else if (newIndex < oldIndex) {
        // 前にカードを移動した場合
        this.sortUseCards()
        this.sortAllUseCards()
      }
    },
    sortAllUseCards() {
      // 一覧で表示するカードの配列
      const result = []
      // 種類ごとにリスト表示するカードの配列を頭から探索
      this.useCards.forEach((cardObj) => {
        for (let i = 0; i < cardObj.count; ++i) {
          result.push(cardObj.info)
        }
      })
      this.allUseCards = result
    },
    sortUseCards() {
      const result = []
      // 画像一覧で表示するカードの配列を頭から探索
      this.allUseCards.forEach((card) => {
        // 種類順の配列(result)にあるカードかどうか、オブジェクトのimgキーを参照して確認する
        const cardExists =
          result.filter((cardObj) => {
            return cardObj.info.id === card.id
          })[0] !== undefined

        // 種類順の配列に含まれているかどうか
        if (!cardExists) {
          // 含まれない：新規のカードの場合
          // カードのオブジェクトをresultに新規追加する
          const cardObj = { info: card, count: 1 }
          result.push(cardObj)
        } else {
          // 含まれる：既存のカードの場合
          // 該当のオブジェクトのcountを1増やす
          const cardObjIndex = result.findIndex(
            (cardObj) => cardObj.info.id === card.id
          )
          result[cardObjIndex].count++
        }
      })
      this.useCards = result
    },
    // ▲ マイデッキビューに関するメソッド ****************************************▲

    // ▼ 検索ドロワーに関するメソッド ****************************************▼
    // フィルターを変更した時の処理
    async searchCards() {
      await this.resetFilter()
      await this.getNextLoadCardsSnapshot()
      await this.setLastLoadCard()
      await this.displayNextLoadCards()
      await this.$refs.searchedCardsInfiniteLoading.stateChanger.reset()
    },
    resetFilter() {
      this.searchedCards = []
      this.nextLoadCards = null
      this.lastLoadCard = null
    },
    checkUnitName(item, queryText, itemText) {
      return (
        item.name
          .toLocaleLowerCase()
          .startsWith(queryText.toLocaleLowerCase()) ||
        item.hiragana
          .toLocaleLowerCase()
          .startsWith(queryText.toLocaleLowerCase()) ||
        item.etc.toLocaleLowerCase().startsWith(queryText.toLocaleLowerCase())
      )
    },
    // フィルターのパターンによって異なるスナップショットを取得
    async getNextLoadCardsSnapshot() {
      let result = this.$firestore.collection('Cards')
      if (this.unitNameFilter) {
        result = result.where('unitName', '==', this.unitNameFilter)
      }
      if (this.symbolFilter) {
        result = result.where('symbols', 'array-contains', this.symbolFilter)
      }
      if (this.sortieCostFilter) {
        result = result.where('sortie_cost', '==', this.sortieCostFilter)
      }
      if (this.lastLoadCard) {
        result = result.startAfter(this.lastLoadCard)
      }
      result = await result.limit(10).get()
      this.nextLoadCards = result
    },
    // 無限スクロールのために、最後に表示されているカードのスナップショットを取得しておく
    setLastLoadCard() {
      this.lastLoadCard = this.nextLoadCards.docs[this.nextLoadCards.size - 1]
    },
    // 取得した次に表示するカードのスナップショットのデータをクライアントサイドジョインののちに表示
    displayNextLoadCards() {
      const result = this.nextLoadCards.docs.map((doc) => {
        const card = doc.data()
        card.color = this.$color(card.symbols)
        card.gradaton = this.$gradation(card.symbols)
        card.imageUrl = this.$imageUrl(card.id, card.recording)
        return card
      })
      result.forEach((card) => {
        this.searchedCards.push(card)
      })
      return result
    },
    // サーチ無限スクロール
    searchedCardsInfiniteHandler($state) {
      setTimeout(async () => {
        await this.getNextLoadCardsSnapshot()
        await this.setLastLoadCard()
        await this.displayNextLoadCards()
        // 取得したカードが10未満ならスクロール終了
        if (this.nextLoadCards.size < 10) {
          $state.complete()
        } else {
          $state.loaded()
        }
      }, 100)
    },
    // TODOマーク無限スクロール
    keepCardsInfiniteHandler($state) {
      setTimeout(async () => {
        await this.getNextLoadCardsSnapshot()
        await this.setLastLoadCard()
        await this.displayNextLoadCards()
        // 取得したカードが10未満ならスクロール終了
        if (this.nextLoadCards.size < 10) {
          $state.complete()
        } else {
          $state.loaded()
        }
      }, 100)
    },
    // ▲ 検索ドロワーに関するメソッド ****************************************▲

    // TODOisMarked(card) {
    //   const result = this.useCards.filter((myDeckCard) => {
    //     return card
    //   })
    //   if (result.length !== 0) {
    //     return true
    //   } else {
    //     return false
    //   }
    // },
    addCard(card) {
      const result = {
        info: {
          id: card.id,
          title: card.title,
          unitName: card.unitName,
          recording: card.recording,
          symbols: card.symbols,
          color: this.$color(card.symbols),
          gradation: this.$gradation(card.symbols),
          sortie_cost: card.sortie_cost,
          imageUrl: this.$imageUrl(card.id, card.recording),
        },
        count: 1,
      }

      const cardExists =
        this.useCards.filter((cardObj) => {
          return cardObj.info.id === result.info.id
        })[0] !== undefined
      if (!cardExists) {
        this.useCards.push(result)
      } else {
        const cardObjIndex = this.useCards.findIndex(
          (cardObj) => cardObj.info.id === card.id
        )
        this.useCards[cardObjIndex].count++
      }
      this.sortAllUseCards()
    },
    addFourCards(card) {
      for (let i = 0; i < 4; i++) {
        this.addCard(card)
      }
    },
    incrementUseCardObjCount(card) {
      card.count++
      this.sortAllUseCards()
    },
    decrementUseCardObjCount(card) {
      card.count--
      const i = this.useCards.indexOf(card)
      if (card.count === 0) {
        this.useCards.splice(i, 1)
        this.overlayId = null
      }
      this.sortAllUseCards()
    },
    changeCardCount(cardId) {
      // オーバーレイのON/OFFを状態により分岐
      if (this.overlayId === cardId) {
        this.overlayId = null
      } else {
        this.overlayId = cardId
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
.gradient {
  background-image: linear-gradient(
    90deg,
    rgb(109, 213, 208) 30%,
    rgba(109, 213, 208, 0) 70%
  );
}
</style>
