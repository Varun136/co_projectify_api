import random
from datetime import datetime
from .auth import get_password_reset_url
from authentication.models import ConfirmationCode

def add_event_to_reset_password(user_obj) -> bool:
    username = user_obj.username
    url = get_password_reset_url(username)
    print("ADDED EVENT TO SEND PASSWORD RESET")
    # lambda function implimentation pending
    return True


def add_event_to_send_confirmation_code(user_id, user_email) -> bool:
    confirmation_code = random.randint(10000, 99999)

    code_obj = ConfirmationCode.objects.filter(user_id=user_id).first()
    if not code_obj:
        code_obj = ConfirmationCode()
        code_obj.user_id = user_id

    code_obj.code = confirmation_code
    code_obj.last_updated_at = datetime.now()
    code_obj.save()
    print("ADDED EVENT TO SEND CONFIRMATION CODE")
    # lambda function implimentation pending
    return True