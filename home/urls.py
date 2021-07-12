from django.urls import path
from . import views

# Url ,View ,Name
urlpatterns = [
    path('', views.index, name='index'),
    path('userdetails/<int:id>/', views.userdetails, name='details'),
]
