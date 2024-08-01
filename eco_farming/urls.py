from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.WeatherSlideListView.as_view(), name="index"),
    path('products/categories/<str:type>', views.ProductCategoryView.as_view(), name='product_categories'),
    path("harmful/categories/<str:type>", TemplateView.as_view(template_name="harmful.html"), name="harmful_categories"),
    path('harmful/items/<str:type>', views.HarmfulListView.as_view(), name='harmful_items'),
    path('product_brands/<str:type>/', views.BrandsListView.as_view(), name='product_brands'),
    path('brand_page/details/<int:pk>/<str:type>/', views.BrandDetailView.as_view(), name='brands_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
