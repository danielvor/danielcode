from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('portfolio.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
