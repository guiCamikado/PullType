def getUserProfilePicture():
    from Flask import JWTAuth as JWTAuth
    import os

    username = JWTAuth.returnUser()
    if not username:
        return dict(userAssets={'profilePicture': 'images/default-profile-picture.png'})
    
    profile_image_path = os.path.join('static', 'users', username, 'image', 'profilePicture.jpg')
    if os.path.isfile(profile_image_path):
        profile_image_relative = f'users/{username}/image/profilePicture.jpg'
    else:
        profile_image_relative = 'images/default-profile-picture.jpg'
    return profile_image_relative