from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eco_farming.urls'))
]

admin.site.site_header = "EcoFarming"
admin.site.site_title = "EcoFarming"
admin.site.index_title = "EcoFarming"
