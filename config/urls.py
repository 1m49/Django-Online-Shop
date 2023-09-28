from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('allauth.urls')),
                  path('', include('pages.urls')),
                  path('product/', include('products.urls')),
                  path('cart/', include('cart.urls')),
                  path('order/', include('orders.urls')),
                  path('ckeditor/', include('ckeditor_uploader.urls')),

                  # Rosetta (i18n)
                  path('rosetta/', include('rosetta.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
