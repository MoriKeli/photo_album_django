from django.urls import path
from useraccounts.views import *

urlpatterns = [
    path('', user_login, name='login'),
    path('registration', user_registration, name='user_regist'),
    path('logout', logout, name='logout'),
    path('edit-profile', user_profile, name='edit_profile'),
    
]