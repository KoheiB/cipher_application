// ※注意
// １．事前にCardsコレクションをFirestoreコンソールで削除しておくこと
// ２．サービスアカウントファイルはgitにはコミットしないので、
//     このプログラムを動かすときは自分で同じ階層に置いてください

var admin = require("firebase-admin");

var serviceAccount = require("./firebase-privateKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

// 配列を指定されたサイズに分割するメソッド
const arrayChunk = ([...array], size = 1) => {
  return array.reduce((acc, value, index) => index % size ? acc : [...acc, array.slice(index, index + size)], []);
}

const db = admin.firestore();
const fs = require('fs');
const csvSync = require('csv-parse/lib/sync');
const file = './2020-12-31_cipher_data.csv'; //同階層にファイルを置く
let data = fs.readFileSync(file); //csvファイルの読み込み
let responses = csvSync(data);//parse csv
let objects = []; //この配列の中にパースしたcsvの中身をkey-value形式で入れていく

// データ準備
responses.forEach(function(response) {
  objects.push({
    _id:            response[0] + response[1],
    card_no :       response[0],
    rare:           response[1],
    recording:      response[2],
    title:          response[3],
    unitName:       response[4],
    sortie_cost:    response[5],
    cc_cost:        response[6],
    symbols:        [ ( response[7]=='' ? 'なし' : response[7] ) ,
                      response[8]
                    ],
    gender:         response[9],
    weapon:         response[10],
    types:          [ response[11],
                      response[12],
                      response[13],
                      response[14]
                    ],
    n_skills:       [ {name: response[15],
                       text: response[19]
                      },
                      {name: response[16],
                       text: response[20]},
                      {name: response[17],
                       text: response[21]},
                      {name: response[18],
                       text: response[22]
                      }
                    ],
    s_skills:       [{name: response[23],
                      text: response[25]},
                     {name: response[24],
                      text: response[26]}
                    ],
    c_power:        response[27],
    s_power:        response[28],
    range:          response[29],
    class:          response[30],
    job:            response[31],
    flavor:         response[32],
    illustrator:    response[33]
  })
}, this);

// 一番初めに入ってるヘッダーの要素を削除
objects.shift();

// 配列を400要素の単位で分割
// firestoreでは1トランザクションで500回の通信制限があるため
// マックスギリギリだとたまに失敗するらしいので400要素にした
let devObjects = arrayChunk(objects, 400);

let dataSetCount = 0;

devObjects.forEach(function(devObject){

  // Cardsコレクションをまるごと削除するコードを書くのが想像以上にだるいので削除処理は書かない
  // FirestoreのコンソールからCardsコレクションを事前に削除しておくこと
  const batch = db.batch();

  devObject.forEach(function(object){
      let id = object["_id"]
      batch.set(db.collection('Cards').doc(id), object)
      dataSetCount++;
  });

  batch.commit();

});

// 何件データを入れたかを出力する
// 3177ならOK
console.log("dataSetCount : " + dataSetCount);
