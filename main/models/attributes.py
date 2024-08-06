from django.db import models
from authentication.models import UserAccount

class Skill(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class UserSkill(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    def __str__(self):
        return "U-{}|S-{}".format(self.user.id, self.skill.id)

    
class Interest(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class UserInterest(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)

    def __str__(self):
        return "U-{}|I-{}".format(self.user.id, self.interest.id)