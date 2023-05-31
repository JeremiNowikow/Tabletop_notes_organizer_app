import pytest
from django.test import Client
from django.urls import reverse
from django.test import TestCase

# Create your tests here.

@pytest.mark.django_db
def test_index():
    client = Client()
    url = reverse('/')
    response = client.get(url)
    assert response.status_code == 200