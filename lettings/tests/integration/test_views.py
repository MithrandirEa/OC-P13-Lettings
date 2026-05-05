"""Tests d'intégration pour les vues de l'application lettings."""

import pytest
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.fixture
def address(db):
    """Fixture : adresse valide persistée en base."""
    return Address.objects.create(
        number=10,
        street="Baker Street",
        city="London",
        state="LN",
        zip_code=12345,
        country_iso_code="GBR",
    )


@pytest.fixture
def letting(db, address):
    """Fixture : location valide persistée en base."""
    return Letting.objects.create(title="Beautiful Flat", address=address)


# --- Vue index ---


@pytest.mark.django_db
def test_index_returns_200(client):
    # Arrange / Act
    response = client.get(reverse("lettings:index"))
    # Assert
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_uses_correct_template(client):
    response = client.get(reverse("lettings:index"))
    assert "lettings/index.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_index_with_empty_list_returns_200(client):
    response = client.get(reverse("lettings:index"))
    assert response.status_code == 200
    assert list(response.context["lettings_list"]) == []


@pytest.mark.django_db
def test_index_displays_letting_title(client, letting):
    response = client.get(reverse("lettings:index"))
    assert "Beautiful Flat" in response.content.decode()


# --- Vue letting (détail) ---


@pytest.mark.django_db
def test_letting_detail_returns_200(client, letting):
    response = client.get(reverse("lettings:letting", args=[letting.id]))
    assert response.status_code == 200


@pytest.mark.django_db
def test_letting_detail_uses_correct_template(client, letting):
    response = client.get(reverse("lettings:letting", args=[letting.id]))
    assert "lettings/letting.html" in [t.name for t in response.templates]


@pytest.mark.django_db
def test_letting_detail_displays_title_and_address(client, letting):
    response = client.get(reverse("lettings:letting", args=[letting.id]))
    content = response.content.decode()
    assert "Beautiful Flat" in content
    assert "Baker Street" in content


@pytest.mark.django_db
def test_letting_detail_unknown_id_returns_500(client):
    # La vue utilise get() sans get_object_or_404 → DoesNotExist → 500
    client.raise_request_exception = False
    response = client.get(reverse("lettings:letting", args=[9999]))
    assert response.status_code == 500
