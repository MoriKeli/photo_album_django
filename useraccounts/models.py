from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    user_account_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Registered Users'
        verbose_name_plural = verbose_name

    def __str__(self):
        return 'User {} created account on {}'.format(self.name, self.user_account_created.strftime('%a %dth-%m-%Y %H:%M:%S'))
