from django.shortcuts import render, redirect
from .models import Auto
from .forms import AutoForm

# Create your views here.

def agregar(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrados')
    else:
        form = AutoForm()
    return render(request, 'autos/agregar.html', {'form': form})

def registrados(request):
    autos = Auto.objects.all()
    return render(request, 'autos/registrados.html', {'autos': autos})