export default {
  methods: {
    getImageUrl(card) {
      const fileName = card.id.replace('+', 'plus')
      const result = '/img/' + card.recording + '/' + fileName + '.png'
      return result
    },
  },
}
