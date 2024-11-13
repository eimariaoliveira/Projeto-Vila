from django.urls import path
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.views import LoginView, EventosView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login/', LoginView.as_view(), name='login'),
    path('eventos/', EventosView.as_view(), name='eventos'),

]

@login_required
def adquirir_ingresso(request):
    return render(request, 'adquirir_ingresso.html')

