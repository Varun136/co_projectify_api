from django.db import models
from django.contrib.auth.models import AbstractUser


class UserAccount(AbstractUser):
    GENDER_CHOICES = {
        "M": "Male",
        "W": "Woman"
    }
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def __str__(self):
        return self.username
