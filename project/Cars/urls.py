from django.urls import path
from .views import cars, filter_by_transmissions, filter_by_class

urlpatterns = [
    path('', cars, name='cars'),
    path('transmission/<int:transmission_id>/', filter_by_transmissions, name='filter_by_transmissions'),
    path('class/<int:class_id>/', filter_by_class, name='filter_by_class'),
]