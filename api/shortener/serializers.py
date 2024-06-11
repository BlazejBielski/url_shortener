from rest_framework import serializers

from .models import URL


class URLSerializer(serializers.ModelSerializer):
    """
    Serializer for the URL model.

    This serializer handles the serialization and deserialization of
    URL instances, focusing on the `id` and `short_url` fields.

    Meta:
        model (URL): The model that is being serialized.
        fields (tuple): Specifies the fields to include in the serialization.
                        In this case, it includes 'id' and 'short_url'.
    """
    class Meta:
        model = URL
        fields = (
            "id",
            "short_url",
        )


class OriginalURLSerializer(serializers.ModelSerializer):
    """
    Serializer for the URL model, focusing on the original URL.

    This serializer handles the serialization and deserialization of
    URL instances, focusing on the `original_url` field.

    Meta:
        model (URL): The model that is being serialized.
        fields (str): Specifies the field to include in the serialization.
                      In this case, it includes only 'original_url'.
    """
    class Meta:
        model = URL
        fields = ("url",)
