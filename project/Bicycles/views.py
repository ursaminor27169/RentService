from django.shortcuts import render
from .models import Bsles


def bicycles(request):
    Bicycles = Bsles.objects.all()
    context = {'Bicycles': Bicycles}
    return render(request, 'Bicycles/Bicycles.html', context)