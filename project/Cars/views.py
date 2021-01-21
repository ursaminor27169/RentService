from django.shortcuts import render
from .models import Cars, Transmissions, Ranks


def cars(request):
    all_car = Cars.objects.all()
    transmission = Transmissions.objects.all()
    classes = Ranks.objects.all()
    context = {'Cars': all_car, 'Transmissions': transmission, 'classes': classes}
    return render(request, 'Cars/Cars.html', context)


def filter_by_transmissions(request, transmission_id):
    car = Cars.objects.filter(transmission=transmission_id)
    transmission = Transmissions.objects.all()
    context = {'Cars': car, 'Transmissions': transmission}
    return render(request, 'Cars/by_transmissions.html', context)


def filter_by_class(request, class_id):
    car = Cars.objects.filter(rank=class_id)
    classes = Ranks.objects.all()
    context = {'Cars': car, 'classes': classes}
    return render(request, 'Cars/by_classes.html', context)