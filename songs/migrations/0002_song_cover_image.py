# Generated by Django 5.1.4 on 2025-01-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='songs/covers/%Y/%m/%d/'),
        ),
    ]
