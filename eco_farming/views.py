from django.views.generic import ListView, DetailView
from .models import (WeatherSlide, ProductCategory, Brand, Harmful, HarmfulCategory, Culture, CultureCategory,
                     Publication)
from django.core.paginator import Paginator
from django.db.models import Q
import requests
from datetime import datetime


def get_forecast():
    city = 'Гомель'
    appid = "bf67f45c5820583170fa862576056717"
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    result = []
    print('city:', data['city']['name'], data['city']['country'])
    for i in data['list']:
        result.append({'city': city,
                       'date': datetime.strptime(i['dt_txt'], "%Y-%m-%d %H:%M:%S"),
                       'temp': round(i['main']['temp']),
                       'wind': i['wind']['speed'],
                       'weather': i['weather'][0]['description']})
    return result


class WeatherSlideListView(ListView):
    model = WeatherSlide
    context_object_name = 'weather_slide_list'
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["videos"] = Publication.objects.all().filter(type='Видеоматериалы')[:2]
        context["weather"] = get_forecast()
        return context


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
        brands = self.get_brands()
        context['brands'] = brands
        context['page_obj'] = brands
        context["type"] = self.kwargs['type']
        return context

    def get_brands(self):
        queryset = self.object.product_category.brand_set.all()
        paginator = Paginator(queryset, 2)
        page = self.request.GET.get('page')
        brands = paginator.get_page(page)
        return brands


class HarmfulSearch(ListView):
    template_name = 'harmful_list.html'

    def get_queryset(self):
        search = self.request.GET.get("search")
        print(search)
        return Harmful.objects.filter(category__type=self.kwargs['type']).filter(Q(title__iregex=search) |
                                      Q(title_latin__iregex=search) |
                                      Q(description__iregex=search) |
                                      Q(family__iregex=search) |
                                      Q(subtype__iregex=search) |
                                      Q(bio_group__iregex=search) |
                                      Q(biology__iregex=search)).order_by('title')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["search"] = f"search={self.request.GET.get('search')}&"
        context["type"] = self.kwargs['type']
        context["categories"] = HarmfulCategory.objects.all().filter(type=self.kwargs['type'])
        return context


class CultureCategoryView(ListView):
    model = CultureCategory
    template_name = 'cultures.html'


class CultureCategoryDetailView(DetailView):
    model = CultureCategory
    template_name = 'cultures_category_page.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['brands'] = self.object.culturebrands_set.all()
        context['categories'] = self.object.culturebrands_set.all().values_list('brand__product_category__title',
                                                                                flat=True).distinct()
        context["type"] = self.kwargs['type']
        return context


class CultureDetailView(DetailView):
    model = Culture
    template_name = 'culture_page.html'


class PublicationView(ListView):
    model = Publication
    paginate_by = 2
    template_name = 'publications.html'

    def get_queryset(self):
        return Publication.objects.all().filter(type=self.kwargs['type'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type"] = self.kwargs['type']
        context["categories"] = Publication.objects.all().filter(type=self.kwargs['type']).values_list(
            'category__title', flat=True).distinct()
        return context


class PublicationSubView(ListView):
    model = Publication
    paginate_by = 2
    template_name = 'publications.html'

    def get_queryset(self):
        return Publication.objects.all().filter(type=self.kwargs['type'], category__title=self.kwargs['category'])

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["type"] = self.kwargs['type']
        context["categories"] = Publication.objects.all().filter(type=self.kwargs['type']).values_list(
            'category__title', flat=True).distinct()
        return context


class PublicationDetailView(DetailView):
    model = Publication
    template_name = 'publication_page.html'
