from Account.models import MyUser



def user_authentication(email , password):
    auth_user = MyUser.objects.get(email=email)
    if auth_user is  None:
        raise ValueError("the user is not exsist")
    else:
        print(auth_user.email)
        if auth_user.password==password:
            print("auth_user",auth_user)
            return auth_user
    