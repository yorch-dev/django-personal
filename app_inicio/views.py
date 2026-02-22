from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'app_inicio/index.html')

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, f'Sesión iniciada como: {form.cleaned_data.get("username")}')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error en usuario o contraseña')
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
        return super().dispatch(request, *args, **kwargs)


class CustomPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña cambiada exitosamente')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al cambiar la contraseña')
        return super().form_invalid(form)