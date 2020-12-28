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
            <v-layout row wrap>
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
            </v-layout>
          </v-radio-group>
        </div>
        <v-form>
          <v-text-field
            class="mt-2 red"
            solo
            append-icon="mdi-magnify"
            placeholder="ユニット名で検索"
          ></v-text-field>
        </v-form>
        <v-tabs-items v-model="tab">
          <v-tab-item>
            <v-card>aaa</v-card>
          </v-tab-item>
          <v-tab-item>
            <v-card>bbb</v-card>
          </v-tab-item>
        </v-tabs-items>
      </v-col>
      <v-col cols="12" sm="9">
        <div class="text-h4">デッキ名</div>
        <v-card class="overflow-auto" height="80vh">
          <v-row no-gutters>
            <v-col v-for="n of 50" :key="n" cols="2">
              <Card></Card>
            </v-col>
          </v-row>
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
}
</script>
