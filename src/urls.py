from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("dum/", include("dum.urls")),
    path('admin/', admin.site.urls),
]
