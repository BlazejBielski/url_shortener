import pytest
from django.utils import timezone
from shortener.models import URL


@pytest.mark.django_db
def test_url_creation():
    url = URL.objects.create(
        url="https://example.com",
        short_url="exmpl"
    )
    assert url.url == "https://example.com"
    assert url.short_url == "exmpl"
    assert url.created_at <= timezone.now()


@pytest.mark.django_db
def test_url_str_representation():
    url = URL.objects.create(
        url="https://example.com/longurl",
        short_url="exmpl"
    )
    assert str(url) == "https://example.com/longurl -> exmpl"
