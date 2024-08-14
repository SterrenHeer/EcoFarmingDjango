from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("", views.WeatherSlideListView.as_view(), name="index"),
    path("harmful/categories/", TemplateView.as_view(template_name="harmful.html"), name="harmful_categories"),
    path("contacts/", TemplateView.as_view(template_name="contacts.html"), name="contacts"),
    path('harmful/items/', views.HarmfulListView.as_view(), name='harmful_items'),
    path('harmful_page/details/<slug:type>/<int:pk>/', views.HarmfulDetailView.as_view(), name='harmful_details'),
    path('harmful/items/<str:type>/search/', views.HarmfulSearch.as_view(), name='harmful_search'),
    path('products/categories/', views.ProductCategoryView.as_view(), name='product_categories'),
    path('product_brands/<slug:type>/', views.BrandsListView.as_view(), name='product_brands'),
    path('brand_page/details/<slug:type>/<int:pk>/', views.BrandDetailView.as_view(), name='brands_details'),
    path('cultures/categories/', views.CultureCategoryView.as_view(), name='culture_categories'),
    path('cultures_category/details/<slug:type>/<int:pk>/', views.CultureCategoryDetailView.as_view(), name='cultures_category_details'),
    path('culture/details/<slug:category>/<slug:title>/<int:pk>/', views.CultureDetailView.as_view(), name='culture_details'),
    path('publications/', views.PublicationView.as_view(), name='publications'),
    path('publications/<str:type>/<str:category>/', views.PublicationSubView.as_view(), name='publications_sub'),
    path('publication/details/<slug:type>/<int:pk>/', views.PublicationDetailView.as_view(), name='publication_details'),
    path('search/results/', views.SearchResultsView.as_view(), name='search_results'),
    path('contacts/send/telegram/', views.SendTelegramMessageView.as_view(), name='send_contacts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
