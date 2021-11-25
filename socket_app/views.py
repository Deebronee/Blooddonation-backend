from django.http.response import HttpResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from backend.models.appointments import appointments

def anzeigen(request):
    all_appointments = appointments.objects.all
    return render(request, 'anzeigen.html', {'all_appointments': all_appointments})
