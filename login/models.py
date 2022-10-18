import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.forms import model_to_dict
from simple_history.models import HistoricalRecords


class UserManager(BaseUserManager):
    def _create_user(self, username, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, name,last_name, password=None, **extra_fields):
        return self._create_user(username, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username,  name,last_name, password=None, **extra_fields):
        return self._create_user(username,  name,last_name, password, True, True, **extra_fields)

# usuario model
class User(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(max_length = 255, unique = True)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    token = models.UUIDField(primary_key=False,editable=False,null=True,blank=True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    state = models.PositiveIntegerField(default = 0)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def toJSON(self):
        item = model_to_dict(self)
        return item

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','last_name']

    def _str_(self):
        return f'{self.name} {self.last_name}'
