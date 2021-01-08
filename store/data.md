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
    - DocumentId : random
        - userName : String
        - Decks : SubCollection
            - DocumentID : random
                - deckName : String
                <!-- 諸説
                - inDeckCardIds : Array[string]
                -->
                - UseCards : SubCollection <!-- 動詞 + 名詞 のほうがよくないか？と思いUseに変えました -->
                  - DocumentId : Cards.DocumentId
                    - cardId : String
                    - title : String
                    - unitName : String
                    - symbol1 : String
                    - symbol2 : String
                    - count : Number
                    - displayOrder : Number

                - heroCard : Map
                  - cardId : String
                  - title : String
                  - unitName : String
                  - symbol1 : String
                  - symbol2 : String
                - mainClassChangeCard : Map
                  - cardId : String
                  - title : String
                  - unitName : String
                  - symbol1 : String
                  - symbol2 : String 

                <!-- 諸説
                - markCardIds : Array[string]
                -->
                - MarkCards : SubCollection
                  - DocumentId : Cards.DocumentId
                    - cardId : String
                    - title : String
                    - unitName : String
                    - symbol1 : String
                    - symbol2 : String
                    - count : Number
                    - displayOrder : Number

                - isPublic : Boolean
                - isPosted : Boolean
                - comment : String
                - favoritedCount : Number
                - FavoritedUsers : SubCollection
                  - DocumentId : random
                    - favUserRef : String <!-- Userの情報は書き換え頻度が多いと判断し、DocumentReferenceを持つ方針にする -->
                    - createdAt : Timestamp
                - createdAt : Timestamp
                - updatedAt : Timestamp
        - FavoriteDecks : SubCollection
          - DocumentId : random
            - favDeckRef : String <!-- Deckの情報は書き換え頻度が多いと判断し、DocumentReferenceを持つ方針にする -->
            - createdAt : Timestamp
        - createdAt : Timestamp
        - updatedAt : Timestamp

- Cards : Collectioon <!-- 一旦は検索条件に必要な最低限のカラムだけにする -->
    - DocumentId : cardId + rare (ex.B01-001SR+)
        - title : String
        - unitName : String
        - symbol1 : String
        - symbol2 : String
