from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
# Register your models here.


class FilePrintAdmin(ModelAdmin):
    list_display = ('id','file_name', 'bolak_balik','printed','created_at','updated_at')
    search_fields = ("pemesan",)
    ordering = ("pemesan",)
    list_display_links=('id','file_name', 'bolak_balik','printed',)
    

admin.site.register(models.FilePrint, FilePrintAdmin)
admin.site.register(models.User, UserAdmin)
