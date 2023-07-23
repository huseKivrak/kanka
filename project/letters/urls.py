from django.urls import path

from . import views

app_name = "letters"
urlpatterns = [
    path("<int:pk>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("create/<int:pk>/", views.create, name="create"),
    path("mailbox/", views.mailbox, name="mailbox"),
    path("drafts/", views.drafts, name="drafts")
]