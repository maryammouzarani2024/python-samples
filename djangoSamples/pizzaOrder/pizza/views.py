from django.shortcuts import render, redirect
from .models import Pizza




def pricing(request):
    pizzas=Pizza.objects.all()
    return render(request, 'pizza/pricing.html', {'pizzas':pizzas})
