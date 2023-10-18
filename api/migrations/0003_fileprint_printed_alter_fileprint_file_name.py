# Generated by Django 4.2.5 on 2023-09-16 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_fileprint_bolak_balik'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileprint',
            name='printed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fileprint',
            name='file_name',
            field=models.FileField(upload_to='file-upload', verbose_name='file'),
        ),
    ]
