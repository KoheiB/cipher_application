<template>
  <v-container>
    <v-row>
      <v-col cols="12" sm="3">
        <v-tabs v-model="tab" grow>
          <v-tab>ALL</v-tab>
          <v-tab><v-icon>mdi-bookmark-multiple</v-icon></v-tab>
        </v-tabs>
        <div class="white">
          <v-radio-group mandatory row>
            <div class="d-flex flex-wrap flex-row">
              <v-flex
                v-for="checkboxItem in checkboxItems"
                :key="checkboxItem.color"
                md3
              >
                <v-radio
                  v-model="checkboxItem.checked"
                  :name="checkboxItem.name"
                  :label="checkboxItem.name"
                  :color="checkboxItem.color"
                  hide-details=""
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
        <v-card class="d-flex flex-wrap overflow-auto" height="80vh">
          <!-- <v-card class="overflow-auto" height="80vh"> -->
          <Card v-for="n of 50" :key="n"></Card>
          <!-- <v-row no-gutters>
            <v-col v-for="n of 50" :key="n" cols="1">
              <Card></Card>
            </v-col>
          </v-row> -->
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      tab: null,
      deckName: '',
      checkboxItems: [
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
    }
  },
  methods: {
    saveDeck() {
      console.log('saved')
    },
    shareDeck() {
      console.log('shared')
    },
  },
}
</script>
