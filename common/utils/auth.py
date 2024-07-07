import os
import jwt
from datetime import datetime, timedelta
from common.constants import RESET_TOKEN_EXP_TIME
from common.urls import PASSWORD_RESET_URL
from common.response import Errors, Responses
from config.settings import SECRET_KEY
from .queries import get_user_obj


def get_password_reset_url(username):
    token_exp = datetime.now() + timedelta(minutes=RESET_TOKEN_EXP_TIME)
    reset_token = jwt.encode(
        {
            "username": username,
            "exp": token_exp
        },
        SECRET_KEY,
        algorithm="HS256"
    )
    url = os.environ.get("BASE_URL") + PASSWORD_RESET_URL.format(token=reset_token)
    return url

def reset_password(serailizer_data):
    token = serailizer_data.get("token")
    password = serailizer_data.get("password")

    try:    
        decoded_data = jwt.decode(
            token, SECRET_KEY, algorithms="HS256"
        )
        user = get_user_obj(decoded_data.get("username"))
        if not user:
            raise
    except Exception:
        return False, Errors.INVALID_TOKEN.value

    user.set_password(password)
    user.save()
    return True, Responses.PASSWORD_RESET.value