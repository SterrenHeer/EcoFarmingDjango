from django.contrib import admin
from eco_farming.models import (WeatherSlide, Brand, ProductCategory, BrandEffectImage, BrandUsageItem, BrandAdvantage,
                                Harmful, HarmfulImage, HarmfulCategory)

admin.site.register(WeatherSlide)
admin.site.register(ProductCategory)
admin.site.register(HarmfulCategory)


class BrandEffectImageInline(admin.StackedInline):
    model = BrandEffectImage
    extra = 1


class BrandUsageItemInline(admin.TabularInline):
    model = BrandUsageItem
    extra = 1


class BrandAdvantageInline(admin.StackedInline):
    model = BrandAdvantage
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


admin.site.register(BrandUsageItem)
admin.site.register(BrandEffectImage)
admin.site.register(BrandAdvantage)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Harmful, HarmfulAdmin)
