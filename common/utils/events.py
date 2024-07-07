from .auth import get_password_reset_url

def add_event_to_reset_password(user_obj) -> bool:
    username = user_obj.username
    url = get_password_reset_url(username)
    print(url)
    print("ADDED EVENT TO SEND PASSWORD RESET")
    # lambda function implimentation pending
    return True