from django.db.models import Q
from authentication.models import UserAccount

def get_user_obj(email_or_username):
    if not email_or_username:
        return None
        
    return UserAccount.objects.filter(
        Q(email=email_or_username) | Q(username=email_or_username)
    ).first()