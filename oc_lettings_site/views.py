"""Vues pour le module principal du site OC Lettings."""

from django.shortcuts import render


def index(request):
    """Affiche la page d'accueil du site OC Lettings.

    Args:
        request: L'objet requête HTTP de Django.

    Returns:
        HttpResponse: La page HTML d'accueil du site.
    """
    return render(request, "index.html")
