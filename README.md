# Overview
TCG『ファイアーエムブレムサイファ』(以下、サイファと呼びます)のデッキ管理アプリです。

このアプリの開発目的は、商品展開終了後も続いていくサイファというコンテンツを応援することです。

残念ながらサイファは商品展開を終了し、将来的には完全にサービス終了することが決定しました。  
ただ、現在もショップ対戦会やプレイヤー主催のイベント（オンラインを含む）は盛んに行われています。

このアプリが、今後のサイファプレイヤー間の交流の一助となることを願っています。

![Search](https://user-images.githubusercontent.com/60537225/108236289-1532ac00-718a-11eb-9522-d0af1ee1baa8.gif)

# Installation/Usage
開発中につき、未デプロイです。

`$ git clone https://github.com/KoheiB/cipher_application.git`

`$ npm run dev`

# Features

- ユーザー認証機能
  - メールアドレスとパスワードによる認証
  - Twitterアカウントによる認証
- デッキ管理機能
  - 基本的なCRUD機能
- デッキ作成/編集機能
  - デッキ内のカードを種類ごとにリスト表示する機能
  - デッキ内のカードを画像一覧で表示する機能
  - デッキ内のカードをドラッグして並べ替える機能
  - 追加カード検索機能
    - ユニット名
    - シンボル
    - 出撃コスト
  - 追加するカードの候補をキープする機能
  - 連携したツイッターアカウントでシェアする機能
  - ドローテスト機能

# 実装予定機能

- デッキレシピ投稿機能
- 投稿されたレシピをいいねする機能
- デッキ価格計算補助機能
- 大会運営用機能（使用カード集計等）

# Technology

- JavaScript Framework: Nuxt.js(v2.14.12)
- Styling: Vuetify,Sass
- BaaS: Firebase
  - IDaaS: Firebase Authentication
  - Database: Cloud Firestore
  - Hosting: Firebase Hosting
  - FaaS: Cloud Functions
  - Storage: Cloud Storage

# Requirements
- Node.js v12.16.0

# Author
## KoheiB
- [Github](https://github.com/KoheiB)
- [Twitter](https://twitter.com/KoheiB1)
- [Qiita](https://qiita.com/kou74)
## henry11239987
- [Github](https://github.com/henry11239987)
- [Qiita](https://qiita.com/henry1123)
