# Generated by Django 3.0.5 on 2020-05-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mixed_features_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='./placeholder_image/profile-placeholder.jpg', upload_to='images'),
        ),
    ]
