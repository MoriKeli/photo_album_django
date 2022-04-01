from django.urls import path
from album.views import *

urlpatterns  = [
    path('homepage', homepage, name='user_homepage'),
    path('upload-photo', upload_image, name='upload_image'),
    path('delete-photo/<str:pk>', delete_image, name='delete'),
    
]