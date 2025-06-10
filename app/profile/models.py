from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.conf import settings

import secrets
import requests

def generate_api_key():
    return secrets.token_hex(16)

def update_api_gateway(profile):
    url = f"{settings.APISIX_ADMIN_URL}/apisix/admin/consumers"

    payload = {
        "username": profile.user.username,
        "desc": f"LICENCE:{profile.licence_id}. {profile.licence_notes}",
        "plugins": { "key-auth": {
                "disable": True,
                "key": profile.api_token
            } }
    }
    headers = {
        "x-api-key": settings.APISIX_ADMIN_KEY,
        "content-type": "application/json"
    }

    response = requests.put(url, json=payload, headers=headers)
    if not response.ok:
        raise Exception(f"API Gateway update failed with status {response.status_code}")
    else:
        messages.success(profile.user, "O token de API do usuário foi atualizado com sucesso.")

# User profile model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    licence_id = models.CharField(max_length=64, blank=True)
    licence_notes = models.TextField(blank=True)
    api_token = models.CharField(max_length=32, default=generate_api_key, editable=True)

    class Meta:
        verbose_name = "Licence information"

    def save(self, *args, **kwargs):
        # Extract the 'request' if provided.
        request = kwargs.pop("request", None)

        # Save the model normally.
        super().save(*args, **kwargs)

        # Call the function to update API Gateway
        if self.licence_id and self.api_token:
            try:
                update_api_gateway(self)
            except Exception as e:
                messages.error(request, f"Ocorreu um erro ao tentar atualizar os dados da API. Detalhes do erro: {e}")
