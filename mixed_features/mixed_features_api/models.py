from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, image, username, email, first_name, last_name, zip_code, password = None):
        if not username:
            raise ValueError("Username required!")

        user = self.model(
            email = self.normalize_email(email)
        )
        user.image = image
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.zip_code = zip_code
        user.save(using = self._db)
        return user

    def create_staffuser(self, image, username, email, first_name, last_name, password, zip_code):
        user = self.create_user(
            image, 
            username,
            email,
            first_name,
            last_name,
            zip_code,
            password = password,
            
        )
        user.staff = True
        user.save(using = self._db)
        return user

    def create_superuser(self, image, username, email, first_name, last_name, password, zip_code):
        user = self.create_user(
            image,
            username,
            email,
            first_name,
            last_name,
            zip_code,
            password = password,
        )
        user.staff = True
        user.admin = True
        user.save(using = self._db)
        return user

class EventManager(models.Manager):
    def event_validation(self, postData):
        errors = {'test error'}
        return errors


class User(AbstractBaseUser):
    image = models.ImageField(upload_to='images', blank = True, null = True)
    username = models.CharField(max_length = 25, unique = True)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField(max_length = 25)
    zip_code = models.CharField(max_length = 5)
    password = models.CharField(max_length = 10000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    active = models.BooleanField(default = True)
    staff = models.BooleanField(default = False)
    admin = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'zip_code']

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    @property
    def is_active(self):
        return self.active

    objects = UserManager()

class Event(models.Model):
    users_going = models.ManyToManyField(User, related_name = "users_going_related")
    event_by_user = models.ForeignKey(User, related_name = "events_by_user", on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    zip_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = EventManager()




