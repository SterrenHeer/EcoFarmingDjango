from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('eco_farming.urls'))
]

admin.site.site_header = "ЭкоФарминг"
admin.site.site_title = "ЭкоФарминг"
admin.site.index_title = "ЭкоФарминг"
