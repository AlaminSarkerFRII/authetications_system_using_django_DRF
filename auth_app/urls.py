from django.urls import path
from .views import RegistrationAPI, LoginAPI

urlpatterns = [
    path('user-registration/', RegistrationAPI),
    path('user-login/', LoginAPI),
]
