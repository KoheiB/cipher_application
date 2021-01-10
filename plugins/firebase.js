import firebase from 'firebase'

if (!firebase.apps.length) {
  firebase.initializeApp(
    {
      apiKey: "AIzaSyCJ8QjDNyiwsdMLOCyZsZOUR7rPfdAatFs",
      authDomain: "cipher-app-4a381.firebaseapp.com",
      projectId: "cipher-app-4a381",
      storageBucket: "cipher-app-4a381.appspot.com",
      messagingSenderId: "304342188149",
      appId: "1:304342188149:web:58330ba75b30ae8559783c",
      measurementId: "G-KRNKBB1Y4K"
    }
  )
}

export default firebase
