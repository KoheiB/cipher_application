# Overview
TCG『ファイアーエムブレムサイファ』のデッキ管理アプリです。

このアプリの開発目的は、商品展開終了後も続いていくサイファというコンテンツを応援することです。

残念ながらサイファは商品展開を終了し、将来的には完全にサービス終了することが決定しましたが、現在もショップ対戦会やプレイヤー主催のイベント（オンラインを含む）は盛んに行われています。

このアプリが今後のサイファプレイヤー間の交流の一助となることを願っています。

![search](https://user-images.githubusercontent.com/60537225/108232710-6345b080-7186-11eb-941d-f3e703e401bd.mov)
# Demo
## https://my-matching-app-c1796.web.app/

# Installation/Usage

`$ git clone https://github.com/KoheiB/my-matching-app.git`

`$ npm run dev`

# Features

- ユーザー認証機能
  - メールアドレスとパスワードによる認証
  - Twitterアカウントによる認証
- デッキ管理機能
  - 基本的なCRUD機能
- デッキ作成/編集機能
  - デッキ内のカードを種類ごとに表示する機能
  - デッキ内のカードを一枚ずつ表示する機能
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

## buruso3