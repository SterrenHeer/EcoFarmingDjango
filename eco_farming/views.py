from django.views.generic import ListView, DetailView, TemplateView
from .models import (WeatherSlide, ProductCategory, Brand, Harmful, HarmfulCategory, Culture, CultureCategory,
                     Publication)
from django.core.paginator import Paginator
from django.db.models import Q
import requests
from datetime import datetime
from itertools import chain


def get_forecast(req):
    city = 'Минск'
    if "city" in req.GET:
        city = req.GET.get('city')
    appid = "bf67f45c5820583170fa862576056717"
    try:
        result = get_list(city, appid)
    except:
        result = get_list('Минск', appid)
    return result


def get_list(city, appid):
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                       params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    if data['list'] is None:
        city = 'Минск'
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
        data = res.json()
    result = []
    day = -1
    for i in data['list']:
        date = datetime.strptime(i['dt_txt'], "%Y-%m-%d %H:%M:%S")
        if date.weekday() != day:
            day = date.weekday()
            day_result = [[], [], [], []]
            for item in data['list']:
                item_date = datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S").weekday()
                if item_date == day:
                    day_result[0].append(item['main']['temp'])
                    day_result[1].append(item['wind']['speed'])
                    day_result[2].append(item['main']['humidity'])
                    day_result[3].append(item['clouds']['all'])
            average_temp = round(sum(day_result[0]) / len(day_result[0]))
            average_wind = round(sum(day_result[1]) / len(day_result[1]) * 3.6, 1)
            average_humidity = round(sum(day_result[2]) / len(day_result[2]))
            average_clouds = round(sum(day_result[3]) / len(day_result[3]))
            result.append({'city': city,
                           'date': date,
                           'day': date.weekday(),
                           'temp': average_temp,
                           'wind': average_wind,
                           'humidity': average_humidity,
                           'clouds': average_clouds,
                           'weather': i['weather'][0]['description'],
                           'icon': i['weather'][0]['icon']})
    return result


class WeatherSlideListView(ListView):
    model = WeatherSlide
    context_object_name = 'weather_slide_list'
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["videos"] = Publication.objects.all().filter(type='Видеоматериалы')[:2]
        context["weather"] = get_forecast(self.request)
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
        return Harmful.objects.filter(category__type=self.kwargs['type']).filter(Q(title__iregex=search) |
                                                                                 Q(title_latin__iregex=search) |
                                                                                 Q(description__iregex=search) |
                                                                                 Q(family__iregex=search) |
                                                                                 Q(subtype__iregex=search) |
                                                                                 Q(bio_group__iregex=search) |
                                                                                 Q(biology__iregex=search)).order_by(
            'title')

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


class SearchResultsView(TemplateView):
    template_name = "search_results.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        q = self.request.GET.get("search")
        product_category_set = ProductCategory.objects.filter(title__iregex=q).order_by('title')
        brand_set = Brand.objects.filter(Q(title__iregex=q) |
                                         Q(description__iregex=q) |
                                         Q(type__iregex=q) |
                                         Q(substance__iregex=q) |
                                         Q(preparative__iregex=q) |
                                         Q(consumption__iregex=q) |
                                         Q(packaging__iregex=q) |
                                         Q(brandadvantage__description__iregex=q) |
                                         Q(expiration__iregex=q)).order_by('title')
        harmful_set = Harmful.objects.filter(Q(title__iregex=q) |
                                             Q(title_latin__iregex=q) |
                                             Q(description__iregex=q) |
                                             Q(family__iregex=q) |
                                             Q(subtype__iregex=q) |
                                             Q(bio_group__iregex=q) |
                                             Q(category__title__iregex=q) |
                                             Q(category__type__iregex=q) |
                                             Q(biology__iregex=q)).order_by('title')
        culture_category_set = CultureCategory.objects.filter(Q(title__iregex=q) |
                                                              Q(description__iregex=q)).order_by('title')
        culture_set = Culture.objects.filter(Q(title__iregex=q) |
                                             Q(description__iregex=q)).order_by('title')
        publication_set = Publication.objects.filter(Q(title__iregex=q) |
                                                     Q(type__iregex=q) |
                                                     Q(description__iregex=q) |
                                                     Q(description_2__iregex=q) |
                                                     Q(category__title__iregex=q)).order_by('title')
        result_set = list(chain(product_category_set, brand_set, harmful_set,
                                culture_category_set, culture_set, publication_set))
        print(result_set)
        paginator = Paginator(result_set, 6)
        page = self.request.GET.get('page')
        result = paginator.get_page(page)
        context['search_results'] = result
        context['page_obj'] = result
        context['search'] = q
        return context
