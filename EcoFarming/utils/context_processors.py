from eco_farming.models import CultureCategory, ProductCategory, HeaderImage


def header_categories(request):
    return {"culture_categories": CultureCategory.objects.all(),
            "product_categories": ProductCategory.objects.all()}


def header_images(request):
    is_exists = False
    path = request.path
    header_all_path = HeaderImage.objects.all().values_list('path', flat=True)
    for all_path in header_all_path:
        if all_path in path:
            is_exists = True

    return {"header_images": HeaderImage.objects.all(),
            "header_exists": is_exists}
