from django.shortcuts import render
from django.views.generic import ListView
from .models import WeatherSlide, Brand


class WeatherSlideListView(ListView):
    model = WeatherSlide
    context_object_name = 'weather_slide_list'
    template_name = 'index.html'


class BrandsListView(ListView):
    model = Brand
    context_object_name = 'brands_list'
    template_name = 'product_brands.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type"] = self.kwargs['type']
        return context

