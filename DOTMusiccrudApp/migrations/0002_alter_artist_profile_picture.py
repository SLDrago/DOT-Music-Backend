# Generated by Django 5.1.4 on 2025-01-10 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOTMusiccrudApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='artist_Pic/'),
        ),
    ]
