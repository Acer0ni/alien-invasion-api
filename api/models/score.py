from django.db import models
from api.models.users import User


class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="score")
    score = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
