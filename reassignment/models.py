from django.db import models
from staff.models import Staff
from appointment.models import Appoinment

class Reassignment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    appointment = models.ForeignKey(
        Appoinment,
        on_delete=models.CASCADE,
        related_name='reassignment_requests',
        help_text="The appointment being requested for reassignment."
    )
    
    requesting_worker = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE, 
        related_name='reassignment_requests_sent',
        help_text="The worker who is requesting the reassignment."
    )
    
    reason = models.TextField(
        help_text="The reason for the reassignment request."
    )
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        help_text="The current status of the reassignment request (pending, approved, rejected)."
    )
    
    requested_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The timestamp when the reassignment request was created."
    )


    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The timestamp when the reassignment request was last updated."
    )

    class Meta:
        ordering = ['-requested_at']
        verbose_name = "Reassignment Request"
        verbose_name_plural = "Reassignment Requests"

    def __str__(self):
        return f"Reassignment Request for Appointment {self.appointment.titulo} by {self.requesting_worker.name} (Status: {self.status})"


