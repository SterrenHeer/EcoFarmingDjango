from eco_farming.models import CultureCategory, ProductCategory, HeaderImage
from django.template.defaultfilters import register
from urllib.parse import unquote


@register.filter
def unquote_new(value):
    return unquote(value)


def header_categories(request):
    categories_titles = CultureCategory.objects.all().values_list('title', 'slug')
    culture_category = None
    for title in categories_titles:
        if title[1] in request.path:
            culture_category = title[0]
    return {"culture_categories": CultureCategory.objects.all(),
            "product_categories": ProductCategory.objects.all(),
            "culture_category": culture_category}


def header_images(request):
    is_exists = False
    path = unquote(request.get_full_path())
    header_all_path = HeaderImage.objects.all().values_list('path', flat=True)
    for all_path in header_all_path:
        if all_path in path:
            is_exists = True

    return {"header_images": HeaderImage.objects.all(),
            "header_exists": is_exists}
