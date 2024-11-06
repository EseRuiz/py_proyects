from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
import uuid

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


class Task(models.Model):
    """ 
    Simple tracking of tasks.
    """
    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4,
        editable=False, 
        unique=True
    )
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    task = models.CharField(max_length=250, verbose_name='tarea')
    description = models.CharField(max_length=250, verbose_name='descripcion')
    name = models.CharField(max_length=125, verbose_name='nombre')

    def __str__(self):
        return f"{self.name}: {self.task}"