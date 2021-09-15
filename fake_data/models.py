from django.db import models

from users.models import CustomUser


class FakeData(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    data = models.JSONField()
    created_at = models.DateTimeField(auto_now=True)
