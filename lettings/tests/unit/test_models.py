"""Tests unitaires pour les modèles de l'application lettings."""

import pytest
from django.core.exceptions import ValidationError

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


# --- Address ---


@pytest.mark.django_db
def test_address_str_returns_number_and_street(address):
    # Arrange / Act / Assert
    assert str(address) == "10 Baker Street"


def test_address_verbose_name_plural():
    assert Address._meta.verbose_name_plural == "Addresses"


def test_address_number_max_validator():
    # Arrange
    address = Address(
        number=10000,  # > 9999
        street="Baker Street",
        city="London",
        state="LN",
        zip_code=12345,
        country_iso_code="GBR",
    )
    # Act / Assert
    with pytest.raises(ValidationError):
        address.full_clean()


def test_address_zip_code_max_validator():
    address = Address(
        number=10,
        street="Baker Street",
        city="London",
        state="LN",
        zip_code=100000,  # > 99999
        country_iso_code="GBR",
    )
    with pytest.raises(ValidationError):
        address.full_clean()


def test_address_state_min_length_validator():
    address = Address(
        number=10,
        street="Baker Street",
        city="London",
        state="L",  # < 2 caractères
        zip_code=12345,
        country_iso_code="GBR",
    )
    with pytest.raises(ValidationError):
        address.full_clean()


def test_address_country_iso_min_length_validator():
    address = Address(
        number=10,
        street="Baker Street",
        city="London",
        state="LN",
        zip_code=12345,
        country_iso_code="GB",  # < 3 caractères
    )
    with pytest.raises(ValidationError):
        address.full_clean()


# --- Letting ---


@pytest.mark.django_db
def test_letting_str_returns_title(letting):
    assert str(letting) == "Beautiful Flat"


@pytest.mark.django_db
def test_letting_cascade_delete_on_address(address):
    # Arrange
    letting = Letting.objects.create(title="Flat to delete", address=address)
    letting_id = letting.id
    # Act
    address.delete()
    # Assert
    assert not Letting.objects.filter(id=letting_id).exists()
