from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    relation = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True)

    user_account_created = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     verbose_name = 'Registered Users'
    #     verbose_name_plural = verbose_name

    def __str__(self):
        return f'Profile pic updated on {self.user_account_created.strftime("%a %dth-%m-%Y")} at {self.user_account_created.strftime("%H:%M:%S")}'
    