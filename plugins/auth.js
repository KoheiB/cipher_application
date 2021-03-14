export default (context) => {
  const { app } = context
  const { store } = context

  return new Promise((resolve, reject) => {
    app.$fireAuth.onAuthStateChanged((user) => {
      // 本来は、ここで必要なユーザー情報のオブジェクトを作成して
      // ユーザー情報としてセットする方が好ましいですが、
      // サンプルなので、全てセットしています。
      store.commit('setUser', user)
      resolve()
    })
  })
}
