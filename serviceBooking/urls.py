from django.urls import path
from . import views

# Url ,View ,Name
urlpatterns = [
    path('bookServicer', views.booking, name='booking'),
]
