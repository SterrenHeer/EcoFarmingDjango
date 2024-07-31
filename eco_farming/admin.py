from django.contrib import admin
from eco_farming.models import WeatherSlide, Brand, ProductCategory, BrandEffectImage

admin.site.register(WeatherSlide)
admin.site.register(ProductCategory)


class BrandEffectImageInline(admin.StackedInline):
    model = BrandEffectImage


class BrandAdmin(admin.ModelAdmin):
    inlines = [
        BrandEffectImageInline,
    ]


admin.site.register(Brand, BrandAdmin)