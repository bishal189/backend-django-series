# Generated by Django 5.1.3 on 2024-12-12 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_album_album_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='new',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
