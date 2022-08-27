
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    
    path('', include('lsbase.urls')),
    path('', include('agora.urls')),
    path('admin/', admin.site.urls),
]
