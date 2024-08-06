from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class UserAccount(AbstractUser):
    GENDER_CHOICES = {
        "M": "Male",
        "W": "Woman"
    }
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    is_active = models.BooleanField(default=False)
    profile_key = models.CharField(max_length=255, default="default_profile_image_key")

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def __str__(self):
        return self.username

class ConfirmationCode(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    code = models.CharField(max_length=5)
    last_updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "CODE-{}".format(self.user.id)
