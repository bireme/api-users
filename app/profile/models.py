from django.db import models
from django.contrib.auth.models import User

import secrets

def generate_api_key():
    return secrets.token_hex(32)

# User profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    licence_id = models.CharField(max_length=64, blank=True)
    licence_notes = models.TextField(blank=True)
    api_token = models.CharField(max_length=32, default=generate_api_key, editable=False)

    class Meta:
        verbose_name = "Licence information"