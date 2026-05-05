"""Tests unitaires pour les modèles de l'application profiles."""

import pytest
from django.contrib.auth import get_user_model

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


# --- Profile ---


@pytest.mark.django_db
def test_profile_str_returns_username(profile):
    assert str(profile) == "alice"


@pytest.mark.django_db
def test_profile_favorite_city_can_be_blank(db, user):
    # Arrange / Act
    profile = Profile.objects.create(user=user, favorite_city="")
    # Assert
    assert profile.favorite_city == ""


@pytest.mark.django_db
def test_profile_cascade_delete_on_user(user):
    # Arrange
    profile = Profile.objects.create(user=user, favorite_city="Paris")
    profile_id = profile.id
    # Act
    user.delete()
    # Assert
    assert not Profile.objects.filter(id=profile_id).exists()
