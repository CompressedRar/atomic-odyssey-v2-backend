import firebase_admin
from firebase_admin import credentials, firestore, storage
from dotenv import load_dotenv
import os
load_dotenv()


firebase_key_path = os.getenv("FIREBASE_KEY")
cred = credentials.Certificate(firebase_key_path)
firebase_admin.initialize_app(cred, {
    'apiKey': "AIzaSyCCSvYFzj3bEDaSer6hp1NZwa9vCaeUDAY",
  'authDomain': "atomic-odyssey.firebaseapp.com",
  'projectId': "atomic-odyssey",
  'storageBucket': "atomic-odyssey.firebasestorage.app",
  'messagingSenderId': "969855183693",
  'appId': "1:969855183693:web:90fa6ad424d094fa25a504"
})

db = firestore.client()
profile_storage = storage.bucket()


UserDB = db.collection("users")
LogDB = db.collection("logs")
ScoreDB = db.collection("scores")
ElementsDB = db.collection("elements")