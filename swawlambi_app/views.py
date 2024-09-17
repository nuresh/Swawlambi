from django.shortcuts import render
from .models import Slider, Product

def index(request):
    sliders = Slider.objects.filter(enabled=True).order_by('image_order')
    products = Product.objects.filter().order_by('-date_of_upload')
    context = {
        'sliders': sliders,
        'products':products,
    }
    return render(request, 'index.html',context)
