from typing import Any

from django.views.generic import RedirectView
from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import models, serializers
from .serializers import URLSerializer


class CreateShortURLApiView(generics.CreateAPIView):
    """
    API view to create a shortened URL.

    This view handles the creation of a new URL instance, validating the input
    data and generating a shortened URL.

    Attributes:
        queryset (QuerySet): QuerySet of all URL instances.
        serializer_class (Serializer): The serializer class used for validating
                                       and deserializing input data.

    Methods:
        create(request, *args, **kwargs): Creates a new URL instance, validates
                                          the input data, saves the instance,
                                          and returns the serialized data of the
                                          shortened URL.
    """

    queryset = models.URL.objects.all()
    serializer_class = serializers.OriginalURLSerializer

    def create(self, request, *args, **kwargs):
        """
        Handle the creation of a new URL instance.

        Args:
            request (Request): The request object containing the input data.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            Response: A response object containing the serialized data of the
                      created URL instance and a status code of 201 (Created).
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        url = serializer.save()

        short_url = URLSerializer(instance=url, context={"request": request})

        return Response(data=short_url.data, status=status.HTTP_201_CREATED)


class ShortURLRedirectView(RedirectView):
    """
    View to handle redirection from a shortened URL to the original URL.

    This view retrieves the original URL associated with the given shortened URL
    and redirects the user to the original URL.

    Methods:
        get_redirect_url(*args, short_url, **kwargs): Retrieves the original URL
                                                      for the given shortened URL
                                                      and returns it for redirection.
    """

    def get_redirect_url(self, *args: Any, short_url: str, **kwargs: Any) -> str | None:
        """
        Retrieve the original URL for the given shortened URL and return it.

        Args:
            *args: Additional positional arguments.
            short_url (str): The shortened URL.
            **kwargs: Additional keyword arguments.

        Returns:
            str: The original URL if found, otherwise None.
        """
        url = get_object_or_404(models.URL, short_url=short_url)

        return url.url
