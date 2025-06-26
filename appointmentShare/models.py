from django.db import models
from appointment.models import Appoinment
from staff.models import Staff

class AppointmentShare(models.Model):
    class Permissions(models.TextChoices):
        READONLY = 'readonly', 'Read-Only'
        EDITING = 'editing', 'Editing'

    appointment = models.ForeignKey(
        Appoinment,
        on_delete=models.CASCADE,
        related_name='shares'
    )
    shared_with = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name='shared_appointments'
    )
    permission = models.CharField(
        max_length=20,
        choices=Permissions.choices,
        default=Permissions.READONLY
    )

    shared_by = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        related_name='+', 
        null=True
    )
    shared_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('appointment', 'shared_with')

    def __str__(self):
        return f"{self.appointment.titulo} shared with {self.shared_with.name} as {self.get_permission_display()}"