from django.db import models
from client_user.models import Client


class Conversation(models.Model):
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='conversations',
        help_text="The client who owns this conversation."
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The exact moment the conversation was started."
    )

    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="An optional title for the conversation."
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        if self.title:
            return f"Conversation: {self.title} (Client: {self.client.name})"
        return f"Conversation ID: {self.pk} (Client: {self.client.name})"