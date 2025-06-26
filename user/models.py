from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('worker', 'Worker'),
        ('admin', 'Admin'),
    )

    name = models.CharField("Name", max_length=240)
    email = models.EmailField(unique=True)
    dni = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=20)
    registration_date = models.DateField("Registration Date", auto_now_add=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  

    assigned_clients = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='assigned_worker',
        blank=True,
        limit_choices_to={'role': 'client'},
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['name']  

    def clean(self):
        if self.pk and self.role == 'client' and self.assigned_clients.exists():
            raise ValidationError("Clients cannot have assigned clients.")

    def __str__(self):
        return f"{self.name} ({self.role})"
