const _symbolItems = [
  { name: 'なし', bgcolor: 'cyan lighten-5', gradation: 'cyan-gradation' },
  { name: '光の剣', bgcolor: 'red lighten-3', gradation: 'red-gradation' },
  { name: '聖痕', bgcolor: 'blue lighten-4', gradation: 'blue-gradation' },
  { name: '白夜', bgcolor: 'grey lighten-4', gradation: 'white-gradation' },
  { name: '暗夜', bgcolor: 'grey lighten-1', gradation: 'black-gradation' },
  {
    name: 'メダリオン',
    bgcolor: 'green lighten-3',
    gradation: 'green-gradation',
  },
  {
    name: '神器',
    bgcolor: 'deep-purple lighten-3',
    gradation: 'purple-gradation',
  },
  {
    name: '聖戦器',
    bgcolor: 'yellow lighten-4',
    gradation: 'yellow-gradation',
  },
  { name: '女神紋', bgcolor: 'brown lighten-3', gradation: 'brown-gradation' },
]

export default {
  data() {
    return {
      symbolItems: _symbolItems,
    }
  },
}
