from django.urls import path
from .views import ChatBotAPI, homePage

urlpatterns = [
    path("homepage/", homePage, name="homepage"),  # Correct usage: reference the view function directly
    path("api/", ChatBotAPI.as_view(), name="chatbot"),
]
