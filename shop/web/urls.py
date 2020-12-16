from django.urls import path
from . import views

# для комита через терминал


urlpatterns = [
    path('', views.index, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop/<int:pk>', views.ProductViews.as_view(), name='product_views'),
   
]