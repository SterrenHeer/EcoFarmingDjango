from django.contrib import admin
from eco_farming.models import (Brand, ProductCategory, BrandEffectImage, BrandUsageItem, BrandAdvantage,
                                Harmful, HarmfulImage, HarmfulCategory, Culture, CultureCategory,
                                Publication, PublicationCategory, PublicationImage, HeaderImage, ContactsPage,
                                ContactsPageItem, CompanyPage)

admin.site.register(PublicationCategory)


@admin.register(HarmfulCategory)
class HarmfulCategoryAdmin(admin.ModelAdmin):
    model = HarmfulCategory
    prepopulated_fields = {'slug': ('type',)}


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    model = ProductCategory
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    model = Culture
    list_display = ('title', 'category')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('brand',)


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


class HarmfulImageInline(admin.StackedInline):
    model = HarmfulImage
    extra = 1


class PublicationImageInline(admin.StackedInline):
    model = PublicationImage
    extra = 1


class ContactsPageItemInline(admin.StackedInline):
    model = ContactsPageItem
    extra = 1


class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'product_category', 'type', 'substance', 'preparative', 'consumption', 'packaging',
                    'expiration')
    inlines = [
        BrandAdvantageInline,
        BrandUsageItemInline,
        BrandEffectImageInline,
    ]
    prepopulated_fields = {'slug': ('title',)}


class HarmfulAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'family', 'subtype', 'bio_group')
    inlines = [
        HarmfulImageInline,
    ]
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('brand',)


class CultureCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('brand',)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'category', 'date')
    inlines = [
        PublicationImageInline,
    ]
    prepopulated_fields = {'slug': ('type',)}


class ContactsPageAdmin(admin.ModelAdmin):
    inlines = [
        ContactsPageItemInline,
    ]


admin.site.register(BrandEffectImage)
admin.site.register(BrandAdvantage)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Harmful, HarmfulAdmin)
admin.site.register(CultureCategory, CultureCategoryAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(ContactsPage, ContactsPageAdmin)
admin.site.register(CompanyPage)
