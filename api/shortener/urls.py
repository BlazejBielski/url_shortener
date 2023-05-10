from django.urls import path
from . import views
from .views import CreateShortURLApiView, ShortURLRedirectView

app_name = "shortener"

urlpatterns = [
    path("api/v1/urls/", CreateShortURLApiView.as_view(), name="shorten_url"),
    path("<str:short_url>/", ShortURLRedirectView.as_view(), name="redirect"),
]
