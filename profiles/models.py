from django.db import models

# Create your models here.
class UploadFile(models.Model):
    title = models.CharField(max_length=100, blank=False, null= False)
    file_upload= models.FileField(upload_to='files/uplaoded/')

    def __str__(self):
        return self.title

