from django.db import models
from client_user.models import Client 

class Staff(models.Model):
    ROLE_CHOICES = (
        ('worker', 'Worker'),
        ('admin', 'Admin'),
    ) 

    name = models.CharField("Name", max_length=240)
    email = models.EmailField(unique=True)
    dni = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=20)
    registration_date = models.DateField("Registration Date", auto_now_add=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='worker')
    password = models.CharField("Password", max_length=128, default="default123") 

    assigned_clients = models.ManyToManyField(
        Client,
        related_name='assigned_staff',
        blank=True
    )


    photo = models.ImageField(
        upload_to='staff_photos/', 
        null=True,                  
        blank=True,                 
        help_text="Profile picture of the staff member."
    )

    def __str__(self):
        return f"{self.name} ({self.role})"
