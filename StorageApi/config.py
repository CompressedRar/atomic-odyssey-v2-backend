import firebase_admin
from firebase_admin import credentials, firestore, storage
from dotenv import load_dotenv
import os
load_dotenv()


firebase_key_path = os.getenv("FIREBASE_KEY")

cred = credentials.Certificate("StorageApi/qrsence-firebase-adminsdk-7k5ew-22531a577d.json")

try:
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'your-bucket-name.appspot.com'
    })
    print("Firebase Storage initialized ✅")
except Exception as e:
    print("Error:", e)

profile_storage = storage.bucket()