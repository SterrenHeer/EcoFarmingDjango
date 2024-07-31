from django.contrib import admin
from eco_farming.models import WeatherSlide, Brand, ProductCategory, BrandEffectImage, BrandUsageItem

admin.site.register(WeatherSlide)
admin.site.register(ProductCategory)


class BrandEffectImageInline(admin.StackedInline):
    model = BrandEffectImage
    extra = 1


class BrandUsageItemInline(admin.TabularInline):
    model = BrandUsageItem
    extra = 1


class BrandAdmin(admin.ModelAdmin):
    inlines = [
        BrandEffectImageInline,
        BrandUsageItemInline,
    ]


admin.site.register(BrandUsageItem)
admin.site.register(BrandEffectImage)
admin.site.register(Brand, BrandAdmin)
