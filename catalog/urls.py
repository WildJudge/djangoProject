from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('contacts/', views.contact, name='contact'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]
