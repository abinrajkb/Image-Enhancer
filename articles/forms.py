from django import forms
from . import models

class UploadImage(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ['name','raw_image']