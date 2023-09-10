from django.urls import path
from . import views

urlpatterns = [
    path('list', views.ProductListView.as_view(), name='product_list'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('comment/<int:product_id>/', views.CommentCreateView.as_view(), name='comment_create')
]
