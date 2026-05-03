from django.urls import path
from . import views

urlpatterns = [
    path('tutoriales-front', views.index, name='index_tutoriales_front'),
]