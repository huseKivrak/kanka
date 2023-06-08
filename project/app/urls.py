from django.urls import path
from letter import views

urlpatterns = [
    path('letters/', views.ListLetters.as_view(), name='letter_list'),
    path('envelopes/', views.ListEnvelopes.as_view(), name='envelope_list'),

]
