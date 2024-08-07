from django.contrib import admin
from eco_farming.models import (WeatherSlide, Brand, ProductCategory, BrandEffectImage, BrandUsageItem, BrandAdvantage,
                                Harmful, HarmfulImage, HarmfulCategory, Culture, CultureCategory, CultureBrands,
                                Publication, PublicationCategory, PublicationImage, HeaderImage)

admin.site.register(ProductCategory)
admin.site.register(HarmfulCategory)
admin.site.register(PublicationCategory)


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    model = Culture
    list_display = ('title', 'category')


@admin.register(HeaderImage)
class HeaderImageAdmin(admin.ModelAdmin):
    model = HeaderImage
    list_display = ('title', 'path', 'image')


@admin.register(BrandUsageItem)
class BrandUsageItemAdmin(admin.ModelAdmin):
    model = BrandUsageItem
    list_display = ('brand', 'culture', 'saboteur', 'drug_consumption', 'solution_consumption')


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


class PublicationImageInline(admin.StackedInline):
    model = PublicationImage
    extra = 1


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_category', 'type', 'substance', 'preparative', 'consumption', 'packaging',
                    'expiration')
    inlines = [
        BrandAdvantageInline,
        BrandUsageItemInline,
        BrandEffectImageInline,
    ]


class HarmfulAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'family', 'subtype', 'bio_group')
    inlines = [
        HarmfulImageInline,
    ]


class CultureCategoryAdmin(admin.ModelAdmin):
    inlines = [
        CultureBrandsInline,
    ]


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'category', 'date')
    inlines = [
        PublicationImageInline,
    ]


admin.site.register(BrandEffectImage)
admin.site.register(BrandAdvantage)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Harmful, HarmfulAdmin)
admin.site.register(CultureCategory, CultureCategoryAdmin)
admin.site.register(Publication, PublicationAdmin)
