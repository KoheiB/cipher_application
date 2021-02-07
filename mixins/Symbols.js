const _symbolItems = [
  { name: 'なし', color: 'cyan lighten-5', gradation: 'cyan-gradation' },
  { name: '光の剣', color: 'red lighten-3', gradation: 'red-gradation' },
  { name: '聖痕', color: 'blue lighten-4', gradation: 'blue-gradation' },
  { name: '白夜', color: 'grey lighten-4', gradation: 'white-gradation' },
  { name: '暗夜', color: 'grey lighten-1', gradation: 'black-gradation' },
  {
    name: 'メダリオン',
    color: 'green lighten-3',
    gradation: 'green-gradation',
  },
  {
    name: '神器',
    color: 'deep-purple lighten-3',
    gradation: 'purple-gradation',
  },
  {
    name: '聖戦器',
    color: 'yellow lighten-4',
    gradation: 'yellow-gradation',
  },
  { name: '女神紋', color: 'brown lighten-3', gradation: 'brown-gradation' },
]

const _getSymbolColor = function (card) {
  const symbolItem = this.symbolItems.filter((item) => {
    return item.name === card.symbols[0]
  })
  return symbolItem[0].color
}

const _getSymbolGradation = function (card) {
  const symbolItem = this.symbolItems.filter((item) => {
    return item.name === card.symbols[0]
  })
  return symbolItem[0].gradation
}

export default {
  data() {
    return {
      symbolItems: _symbolItems,
    }
  },
  methods: {
    getSymbolColor: _getSymbolColor,
    getSymbolGradation: _getSymbolGradation,
  },
}
