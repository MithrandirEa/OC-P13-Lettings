"""Modèles de données pour l'application de gestion des locations (lettings)."""

from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """Représente une adresse postale associée à une location."""

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """Retourne une représentation lisible de l'adresse (numéro + rue)."""
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """Représente une location (bien immobilier) avec son titre et son adresse."""

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Retourne le titre de la location."""
        return self.title
