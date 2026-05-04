"""Vues pour l'application de gestion des locations (lettings)."""

from django.shortcuts import render

from .models import Letting


def index(request):
    """Affiche la liste de toutes les locations disponibles.

    Args:
        request: L'objet requête HTTP de Django.

    Returns:
        HttpResponse: La page HTML listant toutes les locations.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """Affiche le détail d'une location spécifique.

    Args:
        request: L'objet requête HTTP de Django.
        letting_id (int): L'identifiant unique de la location à afficher.

    Returns:
        HttpResponse: La page HTML de détail de la location.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
