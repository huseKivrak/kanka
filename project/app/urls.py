from django.urls import path
from .api.views import ListLetters


urlpatterns = [
    path('api/letters', ListLetters.as_view(), name='list_letters'),
]
