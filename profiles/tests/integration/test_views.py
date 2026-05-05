"""Tests d'intégration pour les vues de l'application profiles."""

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

from profiles.models import Profile

User = get_user_model()


@pytest.fixture
def user(db):
    """Fixture : utilisateur valide persisté en base."""
    return User.objects.create_user(username="alice", password="secret")


@pytest.fixture
def profile(db, user):
    """Fixture : profil valide persisté en base."""
    return Profile.objects.create(user=user, favorite_city="Paris")


# --- Vue index ---


@pytest.mark.django_db
def test_index_returns_200(client):
    response = client.get(reverse("profiles:index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_uses_correct_template(client):
    response = client.get(reverse("profiles:index"))
    assert "profiles/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_index_with_empty_list_returns_200(client):
    response = client.get(reverse("profiles:index"))
    assert response.status_code == 200
    assert list(response.context["profiles_list"]) == []


@pytest.mark.django_db
def test_index_displays_profile_username(client, profile):
    response = client.get(reverse("profiles:index"))
    assert "alice" in response.content.decode()


# --- Vue profile (détail) ---


@pytest.mark.django_db
def test_profile_detail_returns_200(client, profile):
    response = client.get(reverse("profiles:profile", args=["alice"]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_detail_uses_correct_template(client, profile):
    response = client.get(reverse("profiles:profile", args=["alice"]))
    assert "profiles/profile.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_profile_detail_displays_username(client, profile):
    response = client.get(reverse("profiles:profile", args=["alice"]))
    assert "alice" in response.content.decode()


@pytest.mark.django_db
def test_profile_detail_unknown_username_returns_404(client):
    response = client.get(reverse("profiles:profile", args=["unknown_user"]))
    assert response.status_code == 404
