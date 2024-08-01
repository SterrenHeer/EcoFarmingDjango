from django.contrib import admin
from eco_farming.models import WeatherSlide, Brand, ProductCategory, BrandEffectImage, BrandUsageItem, BrandAdvantage

admin.site.register(WeatherSlide)
admin.site.register(ProductCategory)


class BrandEffectImageInline(admin.StackedInline):
    model = BrandEffectImage
    extra = 1


class BrandUsageItemInline(admin.TabularInline):
    model = BrandUsageItem
    extra = 1


class BrandAdvantageInline(admin.StackedInline):
    model = BrandAdvantage
    extra = 1


class BrandAdmin(admin.ModelAdmin):
    inlines = [
        BrandAdvantageInline,
        BrandUsageItemInline,
        BrandEffectImageInline,
    ]


admin.site.register(BrandUsageItem)
admin.site.register(BrandEffectImage)
admin.site.register(BrandAdvantage)
admin.site.register(Brand, BrandAdmin)
