from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.WeatherSlideListView.as_view(), name="index"),
    path("harmful/categories/<str:type>", TemplateView.as_view(template_name="harmful.html"), name="harmful_categories"),
    path("contacts/", TemplateView.as_view(template_name="contacts.html"), name="contacts"),
    path('harmful/items/<str:type>', views.HarmfulListView.as_view(), name='harmful_items'),
    path('harmful_page/details/<int:pk>/<str:type>/', views.HarmfulDetailView.as_view(), name='harmful_details'),
    path('products/categories/<str:type>', views.ProductCategoryView.as_view(), name='product_categories'),
    path('product_brands/<str:type>/', views.BrandsListView.as_view(), name='product_brands'),
    path('brand_page/details/<int:pk>/<str:type>/', views.BrandDetailView.as_view(), name='brands_details'),
    path('cultures/categories/<str:type>', views.CultureCategoryView.as_view(), name='culture_categories'),
    path('cultures_category/details/<int:pk>/<str:type>/', views.CultureCategoryDetailView.as_view(), name='cultures_category_details'),
    path('culture/details/<int:pk>/', views.CultureDetailView.as_view(), name='culture_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
