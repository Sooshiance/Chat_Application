from django.urls import path
from django.contrib.auth.views import LoginView

from .views import *


urlpatterns = [
    # path('', LoginView.as_view(template_name="login.html"), name='LOGIN'),
    path('', loginUser, name='LOGIN'),
    path('logout/', logoutUser, name='LOGOUT'),
    path('register/', registerUser, name='REGISTER'),
]
