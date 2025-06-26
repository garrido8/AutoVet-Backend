from django.db import models
from appointment.models import Appoinment 

class AppointmentMessage(models.Model):
    appointment = models.ForeignKey(
        Appoinment, 
        on_delete=models.CASCADE, 
        related_name='messages'
    )
    user = models.CharField(max_length=150)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"Message from {self.user} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"