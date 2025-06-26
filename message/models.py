from django.db import models
from conversation.models import Conversation

class Message(models.Model):
    MESSAGE_TYPE_CHOICES = [
        ('user', 'User'), 
        ('machine', 'Machine'),
    ]

    conversation = models.ForeignKey(
        Conversation, 
        on_delete=models.CASCADE,
        related_name='messages',
        help_text="The conversation this message belongs to.",
        default=None
    )

    content = models.TextField(
        help_text="The actual content of the message."
    )
    type = models.CharField(
        max_length=10,
        choices=MESSAGE_TYPE_CHOICES,
        help_text="The origin of the message (user or machine)."
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        help_text="The exact moment the message was created."
    )

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"[{self.type.upper()}] {self.content[:50]}..." if len(self.content) > 50 else f"[{self.type.upper()}] {self.content}"

