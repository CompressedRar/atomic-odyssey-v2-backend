from FirebaseApi.config import UserDB, profile_storage
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
    def create_account(uuid, username):
        

        UserDB.add({
            "username": username,
            "uuid" : uuid
        })

        #Auth.upload_profile_pic(profile_pic_file)

        return jsonify(message = "User creation successful"), 200
        

    def upload_profile_pic(profile_picture):
        try:
            image_name = f"profile_pictures/{uuid.uuid4()}.jpg"
            profile_image = profile_storage.blob(image_name)
            profile_image.upload_from_file(profile_picture, content_type=profile_picture.content_type)

            profile_image.make_public()
            file_url = profile_image.public_url

            return jsonify({
                "link" : file_url
            }), 200
        
        except:
            return jsonify(message = "Error in uploading picture"), 400

