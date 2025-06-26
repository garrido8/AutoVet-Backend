from django.db import models

class Client(models.Model):
    name = models.CharField("Name", max_length=240)
    email = models.EmailField(unique=True)
    dni = models.CharField("Document", max_length=20)
    phone = models.CharField(max_length=20)
    registration_date = models.DateField("Registration Date", auto_now_add=True)
    password = models.CharField("Password", max_length=128, default="default123") 

    photo = models.ImageField(
        upload_to='client_photos/', 
        null=True,                  
        blank=True,                 
        help_text="Profile picture of the client."
    )

    def __str__(self):
        return self.name
