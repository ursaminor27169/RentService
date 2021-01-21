from django.urls import path
from .views import bicycles


urlpatterns = [
    path('', bicycles, name='bicycles'),
]