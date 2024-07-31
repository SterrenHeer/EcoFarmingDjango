from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.WeatherSlideListView.as_view(), name="index"),
    path('product_brands/<str:type>/', views.BrandsListView.as_view(), name='product_brands'),
    path('brand_page/details/<int:pk>/<str:type>', views.BrandDetailView.as_view(), name='brands_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)