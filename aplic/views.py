from django.shortcuts import render
from django.views import View
from .models import eventos
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
class EventosView(View):
    def get(self, request):
        eventos = eventos.objects.all()
        return render(request, 'eventos.html', {'eventos': eventos})
