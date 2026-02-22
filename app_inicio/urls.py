from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='index', permanent=False)),
    path('index', views.index, name='index'),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("password_change/", views.CustomPasswordChangeView.as_view(), name="password_change"),
]