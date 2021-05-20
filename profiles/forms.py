from django import forms
from .models import UploadFile

class FileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields =('title','file_upload')