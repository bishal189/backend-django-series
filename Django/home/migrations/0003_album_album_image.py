# Generated by Django 5.1.3 on 2024-12-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_album_created_at_album_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
