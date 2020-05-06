# Generated by Django 3.0.5 on 2020-05-06 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mixed_features_api', '0006_auto_20200505_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('zip_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('event_by_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_by_user', to=settings.AUTH_USER_MODEL)),
                ('users_going', models.ManyToManyField(related_name='users_going_related', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
