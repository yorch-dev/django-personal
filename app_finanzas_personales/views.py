from django.shortcuts import render

def index(request):
    return render(request, 'app_finanzas_personales/index_finanzas_personales.html')