"""Modèles de données pour l'application de gestion des profils utilisateurs."""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    """Représente le profil étendu d'un utilisateur."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Retourne le nom d'utilisateur associé au profil."""
        return self.user.username
