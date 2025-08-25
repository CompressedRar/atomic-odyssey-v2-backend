from FirebaseApi.config import UserDB
from StorageApi.config import profile_storage
import uuid
from flask import jsonify

class Auth:
    def getUserCount():
        allusers = UserDB.get()
        return len(allusers)
    
    def does_this_email_taken(email):
        allusers = UserDB.get()

        for key, value in dict(allusers).items():
            if value["email"] == email:
                return True
        
        return False
    
    #username
    #email
    #password
    #profile pic
    #uid from firebase
    def create_account(uuid, username, profile_file):
        
        print("creating account")

        try:
            if profile_file:
                upload_res = Auth.upload_profile_pic(profile_file)
                print("picture uploaded")
        except:
            return jsonify(message = "Uploading Profile Picture Failed"), 400

        try:
            UserDB.add({
                "username": username,
                "uuid" : uuid,
                "link": upload_res
            })
            print("account created")
        except:
            return jsonify(message = "Account Creation Failed"), 400

        return jsonify(message = "User creation successful"), 200
        

    def upload_profile_pic(profile_picture):
         
        image_name = f"profile_pictures/{uuid.uuid4()}.jpg"
        profile_image = profile_storage.blob(image_name)
        profile_image.upload_from_file(profile_picture, content_type=profile_picture.content_type)
        profile_image.make_public()
        
        file_url = profile_image.public_url
        print(file_url)
        return file_url 
            
        

