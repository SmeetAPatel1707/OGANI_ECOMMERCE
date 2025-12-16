"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('blog_details', views.blog_details, name='blog_details'),
    path('blog', views.blog, name='blog'),
    
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    
    path('', views.index, name='index'),
    
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    
    path('main', views.main, name='main'),
    
    path('shop_grid', views.shop_grid, name='shop_grid'),
    path('get_color', views.get_color, name='get_color'),
    path('get_size', views.get_size, name='get_size'),
    path('price_range', views.price_range, name='price_range'),
    path('wishlist/<int:id>',views.wishlist,name='wishlist'),
    
    # path('shop_details', views.shop_details, name='shop_details'),
    # path('shop_details/<int:id>/', views.open_details, name='open_details'),
    # path('shop_details/<int:id>/', views.shop_details, name='shop_details'),

    
    path('shoping_cart', views.shoping_cart, name='shoping_cart'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('pluscart/<int:id>/', views.pluscart, name='pluscart'),
    path('minuscart/<int:id>/', views.minuscart, name='minuscart'),
    path('update_cart/<int:id>/', views.update_cart, name='update_cart'),
    path('remove_cart/<int:id>/', views.remove_cart, name='remove_cart'),
]