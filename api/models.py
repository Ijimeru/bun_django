from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class FilePrint(models.Model):
    id = models.BigAutoField(primary_key=True)
    file_name = models.FileField('file', blank=False, upload_to="file-upload")
    pemesan = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False)
    tipe_print = models.CharField(choices=[("1-4","1 lembar 4 halaman"),("1-2","1 lembar 2 halaman"),("1-1","1 lembar 1 halaman"),],max_length=100,blank=True)
    bolak_balik = models.BooleanField(default=False, blank=False)
    printed = models.BooleanField(default=False,blank=False)

    taken_at = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)
