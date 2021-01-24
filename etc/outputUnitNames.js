const fs = require('fs');
const csvSync = require('csv-parse/lib/sync');
const { set } = require('core-js/fn/dict');
const file = './2021-01-24_cipher_data.csv'; //同階層にファイルを置く
let data = fs.readFileSync(file); //csvファイルの読み込み
let responses = csvSync(data);//parse csv
let unitNames = [];
let titles = [];

responses.forEach(function(response) {
  unitNames.push(response[4]);
});

const distinctUnitNames = [...new Set(unitNames)].sort();

fs.writeFile('./unitNames.txt', '', function(err) {});
distinctUnitNames.forEach(function(distinctUnitName) {
  if(distinctUnitName == "name"){
    return;
  }
  fs.appendFile("./unitNames.txt",'"' + distinctUnitName + '"' + ',\n', function(err) {});
})
