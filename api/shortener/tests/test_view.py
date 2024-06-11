import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_create_short_url_api_view():
    client = APIClient()
    data = {"url": "https://example.com"}
    response = client.post('/create/', data, format='json')
    assert response.status_code == 201
    assert 'short_url' in response.data
