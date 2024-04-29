from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('Accounts.urls')),
    path('api/products/', include('Products.urls')),
]
