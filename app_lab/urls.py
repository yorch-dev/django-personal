from django.urls import path
from . import views

urlpatterns = [
    path('erlangc', views.erlangc, name='erlangc'),
]
