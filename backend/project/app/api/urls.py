from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import MyTokenObtainPairView, LetterList, LetterDetail, DeliveredLetterDetail

urlpatterns = [
    path('letters/', LetterList.as_view(), name='letters'),
    path('letters/<int:pk>/', LetterDetail.as_view(), name='letter-detail'),
    path('letters/delivered/<int:pk>/', DeliveredLetterDetail.as_view(), name='letter-read'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
