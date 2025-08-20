import firebase_admin
from firebase_admin import credentials, firestore, storage

cred = credentials.Certificate("FirebaseApi/atomic-odyssey-firebase-adminsdk-fbsvc-6ac5414c03.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
profile_storage = storage.bucket()


UserDB = db.collection("users")
LogDB = db.collection("logs")
ScoreDB = db.collection("scores")
ElementsDB = db.collection("elements")