from django.db import models


class Answer(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    keywords = models.TextField()  
    votes = models.IntegerField(default=0)
    votedEmails = models.TextField( null=True, blank=True ) 
    userEmail = models.EmailField( null=True, blank=True )
    topAnswer = models.BooleanField( null=True, blank=True, default=False )

    def __str__(self):
        return f"Answer of {self.userEmail} at {self.time}"