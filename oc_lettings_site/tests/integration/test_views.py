"""Tests d'intégration des vues du site OC Lettings et des pages d'erreur."""

import pytest
from django.test import RequestFactory, override_settings
from django.urls import reverse
from django.views.defaults import page_not_found, server_error

# --- Vue index ---


@pytest.mark.django_db
def test_index_returns_200(client):
    response = client.get(reverse("index"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_index_uses_correct_template(client):
    response = client.get(reverse("index"))
    assert "index.html" in [t.name for t in response.templates]


# --- Pages d'erreur personnalisées ---


@override_settings(DEBUG=False)
def test_404_uses_custom_template():
    # Arrange
    factory = RequestFactory()
    request = factory.get("/page-inexistante/")
    # Act
    response = page_not_found(request, exception=Exception("Not found"))
    # Assert
    assert response.status_code == 404
    assert b"404" in response.content
    assert "Page introuvable" in response.content.decode()


@override_settings(DEBUG=False)
def test_500_uses_custom_template():
    # Arrange
    factory = RequestFactory()
    request = factory.get("/")
    # Act
    response = server_error(request)
    # Assert
    assert response.status_code == 500
    assert b"500" in response.content
    assert "Erreur interne du serveur" in response.content.decode()
