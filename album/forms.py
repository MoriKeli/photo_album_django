from django import forms
from album.models import UploadedImages

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImages
        fields ='__all__'
        