from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import WeatherSlide, ProductCategory, Brand, Harmful, HarmfulCategory


class WeatherSlideListView(ListView):
    model = WeatherSlide
    context_object_name = 'weather_slide_list'
    template_name = 'index.html'


class ProductCategoryView(ListView):
    model = ProductCategory
    template_name = 'products.html'


class BrandsListView(ListView):
    model = Brand
    paginate_by = 2
    context_object_name = 'brands_list'
    template_name = 'product_brands.html'

    def get_queryset(self):
        return Brand.objects.filter(product_category__title=self.kwargs['type'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type"] = self.kwargs['type']
        return context


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type"] = self.kwargs['type']
        return context


class HarmfulListView(ListView):
    model = Harmful
    paginate_by = 2
    template_name = 'harmful_list.html'

    def get_queryset(self):
        return Harmful.objects.filter(category__type=self.kwargs['type'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type"] = self.kwargs['type']
        context["categories"] = HarmfulCategory.objects.all().filter(type=self.kwargs['type'])
        return context


class HarmfulDetailView(DetailView):
    model = Harmful
    template_name = 'harmful_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type"] = self.kwargs['type']
        return context

