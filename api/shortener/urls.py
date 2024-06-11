from django.urls import path
from .views import CreateShortURLApiView, ShortURLRedirectView

app_name = "shortener"

urlpatterns = [
    path("create/", CreateShortURLApiView.as_view(), name="create-short-url"),
    path("<str:short_url>/", ShortURLRedirectView.as_view(), name="short-url-redirect"),
]
