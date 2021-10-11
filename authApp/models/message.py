from django.db import models
from .user import User
from .conversation import Conversation

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=500)
    user = models.ForeignKey(User,related_name='message', on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation,related_name='message', on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    is_readed = models.BooleanField(default=False)