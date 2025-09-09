"Referente a ferramentas de uso do menu superior"

def getUserProfilePicture():
    from Flask.PageTools import JWTAuth as JWTAuth
    import os
    
    username = JWTAuth.returnUser()
    imgTypes = ["png","jpg","jpeg","gif","bmp"]
    for i in imgTypes:
        try:
            with open(f'static/users/{username}/image/profilePicture.{i}', 'rb') as img:
                imagePath = f'users/{username}/image/profilePicture.{i}'
                take = imagePath.split('/')
                image = take[3]
            break
        except:
            return None
        
    if not username:
        return dict(userAssets={'profilePicture': 'images/default-profile-picture.png'})
    

    
    profile_image_path = os.path.join('static', 'users', username, 'image', image)
    if os.path.isfile(profile_image_path):
        profile_image_relative = imagePath
    else:
        print("Entrou aqui e isso é um BO")
        profile_image_relative = 'images/default-profile-picture.jpg'
    return profile_image_relative