import { symbolItems } from '../constant/constant'

const getImageUrl = function (id, recording) {
  const fileName = id.replace('+', 'plus')
  const result = '/img/' + recording + '/' + fileName + '.png'
  return result
}
const checkDoubleSymbols = function (symbols) {
  switch (symbols[1]) {
    case '聖痕':
      return { color: 'red-blue', gradation: 'red-blue-gradation' }
    case '暗夜':
      return { color: 'black-white', gradation: 'black-white-gradation' }
    default:
      return null
  }
}
const getSymbolColor = function (symbols) {
  const doubleSymbols = checkDoubleSymbols(symbols)
  if (doubleSymbols) {
    return doubleSymbols.color
  } else {
    const symbolItem = symbolItems.filter((item) => {
      return item.name === symbols[0]
    })
    return symbolItem[0].color
  }
}

const getSymbolGradation = function (symbols) {
  const symbolItem = symbolItems.filter((item) => {
    return item.name === symbols[0]
  })
  const doubleSymbols = checkDoubleSymbols(symbols)
  if (doubleSymbols) {
    return doubleSymbols.gradation
  } else {
    return symbolItem[0].gradation
  }
}

export default ({ app }, inject) => {
  inject('imageUrl', getImageUrl)
  inject('color', getSymbolColor)
  inject('gradation', getSymbolGradation)
}
