from django.db import models
from .user import User

class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='conversation', on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    