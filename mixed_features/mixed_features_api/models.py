
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    username = models.CharField(max_length = 25)
    email = models.EmailField(max_length = 50)
    password = models.CharField(max_length = 18)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)