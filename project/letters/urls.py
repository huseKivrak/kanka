from django.urls import path

from . import views

app_name = "letters"
urlpatterns = [
    path("create/", views.create, name="create"),
    path("detail/<int:pk>/", views.detail, name="detail")
]