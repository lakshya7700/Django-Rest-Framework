from django.shortcuts import render
from .models import CarList
from django.http import JsonResponse

# Create your views here.

def car_list_view(request):
    cars=CarList.objects.all()
    # converting into dictionary
    data={
        'cars':list(cars.values()),
    }
    return JsonResponse(data)

def car_detail_view(request,pk): 
    car=CarList.objects.get(pk=pk)
    data={
        'name':car.name,
        'description':car.description,
        'active':car.active,
    }

    return JsonResponse(data)