from django.urls import path
from .views import ListLetters


urlpatterns = [
    path('/letters', ListLetters.as_view(), name='list_letters'),
]

