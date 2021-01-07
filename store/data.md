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
        - favoriteOtherPlayersDecks : Array[string] <!-- 自分がいいねした他人のdeckIdを格納する配列。deckIdではなくフィールドパスを持つことになる？ -->
        - Decks : SubCollection
            - deckId : DocumentID
                - deckName : String
                - inDeckCards : Array[string]
                - heroCard : String
                - mainClassChangeCard : String
                - markCards : Array[string]
                - isPublic : Boolean
                - isPosting : Boolean
                - comment : String
                - favoritedCount : Number
                - favoritedUsers : Array[string] <!-- このデッキをいいねしたユーザのuserIdを格納する配列 -->
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
