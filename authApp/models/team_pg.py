from django.db import models
from .user import User

class Team_pg(models.Model):
    team_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, related_name='team_pg', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    isActive = models.BooleanField(default=True)