from django.urls import path

from . import views

app_name = "letters"
urlpatterns = [
    path("create/", views.create, name="create"),
    path("<int:pk>/", views.detail, name="detail"),
    path("mailbox/", views.mailbox, name="mailbox"),
    path("drafts/", views.drafts, name="drafts")
]