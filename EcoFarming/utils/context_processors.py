from eco_farming.models import CultureCategory, ProductCategory


def header_categories(request):
    return {"culture_categories": CultureCategory.objects.all(),
            "product_categories": ProductCategory.objects.all()}
