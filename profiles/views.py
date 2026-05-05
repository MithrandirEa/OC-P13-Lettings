"""Vues pour l'application de gestion des profils utilisateurs."""

from django.shortcuts import get_object_or_404, render

from .models import Profile


def index(request):
    """Affiche la liste de tous les profils utilisateurs.

    Args:
        request: L'objet requête HTTP de Django.

    Returns:
        HttpResponse: La page HTML listant tous les profils.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


def profile(request, username):
    """Affiche le détail du profil d'un utilisateur spécifique.

    Args:
        request: L'objet requête HTTP de Django.
        username (str): Le nom d'utilisateur dont on souhaite afficher le profil.

    Returns:
        HttpResponse: La page HTML de détail du profil utilisateur.
    """
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
