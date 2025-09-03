import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv
import os
load_dotenv()


firebase_key_path = os.getenv("FIREBASE_KEY")

cred = credentials.Certificate("FirebaseApi/atomic-odyssey-3d061-firebase-adminsdk-fbsvc-64b12f17f8.json")
app1 = None

try:
    app1 = firebase_admin.initialize_app(cred, name = "dbapp")
    print("Firebase Admin initialized ✅")
except Exception as e:
    print("Error:", e)


db = firestore.client(app = app1)


UserDB = db.collection("users")
LogDB = db.collection("logs")
ScoreDB = db.collection("scores")
ElementsDB = db.collection("elements")

"""print("adding user")

UserDB.add({
    "user": "test3",
    "uuid": "nope"
})"""