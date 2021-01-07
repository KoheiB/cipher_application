<!-- 
変更点
・Userのpasswordを消しました。
・CardのcreatedAtとupdatedAtを消しました。
・デッキをいいねする機能に関わるフィールドを修正しました。
・いくつかフィールド名を微修正しました。
　特に、下記の考え方で「お気に入り」や「いいね」といった似通ったものを区別しています。
　　デッキ作成時にお気に入りカードを登録　→　mark
　　ユーザ同士でいいねを登録　→　favorite
 -->
- Users : Collection
    - userId : DocumentID
        - userName : String
        - Decks : SubCollection
            - deckId : DocumentID
                - deckName : String
                - inDeckCardIds : Array[string]
                <!--
                リストとサブコレのどっちにするか諸説あり、サブコレのほうが良い気がしてきた
                サブコレの場合、Cardの基本情報が更新されることはないので、実体を書き写す方針（二重持ち）にする
                - InDeckCards : SubCollection
                  - inDeckCardId : DocumentId
                    - title : String
                    - unitName : String
                    - symbol1 : String
                    - symbol2 : String
                    - createdAt : Timestamp
                -->

                - heroCardId : String
                - mainClassChangeCardId : String
                <!--
                この2つもMapにしてCardの情報そのものをここに持たせたほうがよくね？                
                - heroCard : Map
                  - title : String
                  - unitName : String
                  - symbol1 : String
                  - symbol2 : String
                - mainClassChangeCard : Map
                  - title : String
                  - unitName : String
                  - symbol1 : String
                  - symbol2 : String 
                -->

                - markCardIds : Array[string]
                <!--
                inDeckCardIdsのコメントと同様

                - MarkCards : SubCollection
                  - MarkCardId : DocumentId
                    - title : String
                    - unitName : String
                    - symbol1 : String
                    - symbol2 : String
                    - createdAt : Timestamp
                -->
                - isPublic : Boolean
                - isPosting : Boolean
                - comment : String
                - favoritedCount : Number
                - FavoritedUsers : SubCollection
                  - favUserId : DocumentId
                    - favUserRef : String <!-- Userの情報は書き換え頻度が多いと判断し、DocumentReferenceを持つ方針にする -->
                    - createdAt : Timestamp
                    - updatedAt : Timestamp
                - createdAt : Timestamp
                - updatedAt : Timestamp
        - FavoriteDecks : SubCollection
          - favDeckId : DocumentId
            - favDeckRef : String <!-- Deckの情報は書き換え頻度が多いと判断し、DocumentReferenceを持つ方針にする -->
            - createdAt : Timestamp
            - updatedAt : Timestamp
        - createdAt : Timestamp
        - updatedAt : Timestamp

- Cards : Collectioon <!-- 一旦は検索条件に必要な最低限のカラムだけにする -->
    - cardId : DocumentID
        - title : String
        - unitName : String
        - symbol1 : String
        - symbol2 : String
