from django import forms
from useraccounts.models import *

class EditProfile(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['profile_pic']
        
