from django.db import models
from .user import User

class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    receptor = models.ForeignKey(User, related_name='notification', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE)
    is_readed = models.BooleanField(default=False)
    created_at = models.DateTimeField()