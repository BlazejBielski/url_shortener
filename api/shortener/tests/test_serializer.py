import pytest
from shortener.models import URL
from shortener.serializers import URLSerializer, OriginalURLSerializer


@pytest.mark.django_db
def test_url_serializer():
    url = URL.objects.create(
        url="https://example.com",
        short_url="exmpl"
    )
    serializer = URLSerializer(url)
    assert serializer.data == {
        "id": url.id,
        "short_url": "exmpl"
    }


@pytest.mark.django_db
def test_original_url_serializer():
    data = {"url": "https://example.com"}
    serializer = OriginalURLSerializer(data=data)
    assert serializer.is_valid()
    url = serializer.save()
    assert url.url == "https://example.com"
