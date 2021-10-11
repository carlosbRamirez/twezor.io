from django.db import models
from .user import User

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField()
    