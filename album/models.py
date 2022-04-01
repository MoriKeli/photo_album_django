from django.db import models

from django.contrib.auth.models import User
from useraccounts.models import Users

class UploadedImages(models.Model):
    # relationship = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image_file = models.ImageField(upload_to='uploadedImages', name='image_file')
    image_name = models.CharField(max_length=100)
    image_description = models.CharField(max_length=100)
    image_upload_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Uploaded Images'
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return 'Image {} uploaded on {}'.format(self.image_name, self.image_upload_date.strftime('%a %dth-%m-%Y %H:%M:%S'))
    