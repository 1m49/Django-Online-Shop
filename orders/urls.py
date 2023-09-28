from django.urls import path
from . import views

app_gname = 'order'
urlpatterns = [
    path('create/', views.order_create_view, name="order_create")
]
