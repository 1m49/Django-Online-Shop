from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('product/', include('products.urls')),
    path('cart/', include('cart.urls')),

    # Rosetta (i18n)
    path('rosetta/', include('rosetta.urls')),
]
