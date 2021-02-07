const _getImageUrl = function (card) {
  const fileName = card.id.replace('+', 'plus')
  const result = '/img/' + card.recording + '/' + fileName + '.png'
  return result
}

export default {
  methods: {
    getImageUrl: _getImageUrl,
  },
}
