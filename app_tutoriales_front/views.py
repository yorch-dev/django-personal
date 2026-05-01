from django.shortcuts import render

def index(request):
    return render(request, 'app_tutoriales_front/index_tutoriales_front.html')
