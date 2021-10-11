from django.db import models
from .user import User

class Foro(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    start_at = models.DateTimeField()
    finish_at = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name='foro', on_delete=models.CASCADE)
    receptor = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE)
    