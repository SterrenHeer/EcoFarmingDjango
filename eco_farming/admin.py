from django.contrib import admin
from eco_farming.models import (WeatherSlide, Brand, ProductCategory, BrandEffectImage, BrandUsageItem, BrandAdvantage,
                                Harmful, HarmfulImage, HarmfulCategory, Culture, CultureCategory, CultureBrands)

admin.site.register(WeatherSlide)
admin.site.register(ProductCategory)
admin.site.register(HarmfulCategory)
admin.site.register(Culture)


class BrandEffectImageInline(admin.StackedInline):
    model = BrandEffectImage
    extra = 1


class BrandUsageItemInline(admin.TabularInline):
    model = BrandUsageItem
    extra = 1


class BrandAdvantageInline(admin.StackedInline):
    model = BrandAdvantage
    extra = 1


class CultureBrandsInline(admin.StackedInline):
    model = CultureBrands
    extra = 1


class HarmfulImageInline(admin.StackedInline):
    model = HarmfulImage
    extra = 1


class BrandAdmin(admin.ModelAdmin):
    inlines = [
        BrandAdvantageInline,
        BrandUsageItemInline,
        BrandEffectImageInline,
    ]


class HarmfulAdmin(admin.ModelAdmin):
    inlines = [
        HarmfulImageInline,
    ]


class CultureCategoryAdmin(admin.ModelAdmin):
    inlines = [
        CultureBrandsInline,
    ]


admin.site.register(BrandUsageItem)
admin.site.register(BrandEffectImage)
admin.site.register(BrandAdvantage)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Harmful, HarmfulAdmin)
admin.site.register(CultureCategory, CultureCategoryAdmin)
