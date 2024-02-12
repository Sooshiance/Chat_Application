from django.urls import path, include

from .views import *


urlpatterns = [
	path("", chatPage, name='CHAT'),
]
