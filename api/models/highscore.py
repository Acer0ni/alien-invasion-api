from django.db import models
from api.models.users import User


class Highscore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="highscore")
    score = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
