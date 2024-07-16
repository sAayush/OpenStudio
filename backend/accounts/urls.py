from .views import *
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/profile/', UserProfileView.as_view(), name='profile'),
    path('accounts/profile/details/', ProfileDetailView.as_view(), name='profile-details'),
]
