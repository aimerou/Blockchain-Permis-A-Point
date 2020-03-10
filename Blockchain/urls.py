from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('permis_a_point/', include('permis_a_point.urls'))
]
