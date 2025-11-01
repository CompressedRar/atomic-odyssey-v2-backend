import firebase_admin
from firebase_admin import credentials, firestore, auth, db
from flask import Blueprint, jsonify

# ===============================================================
# 🔹 Initialize Firebase Admin
# ===============================================================
cred = credentials.Certificate("FirebaseApi/config.json")

try:
    app1 = firebase_admin.get_app("dbapp")
    print("♻️ Reusing existing Firebase Admin app")
except ValueError:
    app1 = firebase_admin.initialize_app(cred, {
        "databaseURL": "https://tofis-app-default-rtdb.firebaseio.com"
    }, name="dbapp")
    print("✅ Firebase Admin initialized successfully")

# ===============================================================
# 🔹 Initialize Firestore and Auth (same app context)
# ===============================================================
firestore_db = firestore.client(app=app1)
auth_client = auth

# ===============================================================
# 🔹 Firestore Collections
# ===============================================================
UserDB = firestore_db.collection("users")
LogDB = firestore_db.collection("logs")
ScoreDB = firestore_db.collection("scores")
ElementsDB = firestore_db.collection("elements")

# ===============================================================
# 🔧 USER MANAGEMENT FUNCTIONS
# ===============================================================

def disables_user(uid: str):
    """Disable a Firebase Auth user by UID."""
    try:
        auth_client.update_user(uid, disabled=True, app=app1)
        print(f"🚫 User {uid} disabled")
        return True
    except Exception as e:
        print("❌ Error disabling user:", e)
        return False


def enables_user(uid: str):
    """Re-enable a previously disabled user by UID."""
    try:
        auth_client.update_user(uid, disabled=False, app=app1)
        print(f"✅ User {uid} re-enabled")
        return True
    except Exception as e:
        print("❌ Error enabling user:", e)
        return False


def get_user(uid: str):
    """Fetch a Firebase Auth user object by UID."""
    try:
        return auth_client.get_user(uid, app=app1)
    except Exception as e:
        print("❌ Error getting user:", e)
        return None


def list_all_users():
    """List all users in Firebase Auth."""
    try:
        all_users = []
        for user in auth_client.list_users(app=app1).iterate_all():
            all_users.append({
                "uid": user.uid,
                "email": user.email,
                "disabled": user.disabled,
                "display_name": user.display_name,
            })
        print(f"✅ Retrieved {len(all_users)} users.")
        return all_users
    except Exception as e:
        print("❌ Error listing users:", e)
        return []


def get_all_users():
    """Combine Firebase Auth + Realtime DB data."""
    try:
        # ✅ 1. Fetch all users from Firebase Auth
        auth_users = {u.uid: u for u in auth_client.list_users(app=app1).iterate_all()}

        # ✅ 2. Fetch all user records from Realtime Database
        rtdb_ref = db.reference("users", app=app1)
        rtdb_data = rtdb_ref.get() or {}

        users = []
        for uid, info in rtdb_data.items():
            auth_user = auth_users.get(uid)
            users.append({
                "uid": uid,
                "email": info.get("email", auth_user.email if auth_user else "N/A"),
                "username": info.get("username", "Unknown"),
                "profilePic": info.get("profilePic"),
                "mmr": info.get("mmr", 0),
                "stars": info.get("stars", 0),
                "disabled": auth_user.disabled if auth_user else False,
            })

        # ✅ 3. Include Auth users not present in DB
        for uid, auth_user in auth_users.items():
            if uid not in rtdb_data:
                users.append({
                    "uid": uid,
                    "email": auth_user.email or "N/A",
                    "username": "N/A",
                    "profilePic": None,
                    "mmr": 0,
                    "stars": 0,
                    "disabled": auth_user.disabled,
                })

        return jsonify(success=True, users=users), 200

    except Exception as e:
        print("❌ Error fetching users:", e)
        return jsonify(success=False, error=str(e)), 500
