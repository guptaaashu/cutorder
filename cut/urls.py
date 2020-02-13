"""cut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from order.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders',detail,name='list'),
    path('order_detail/<int:pk>/',detail_view, name='detail'),
    path('',orde),
    path('lay',laye,name='lay'),
    path('lays',lay_detail,name='list1'),
    path('lay_detail/<int:pk>/red',lay_detail_view_red, name='red'),
    path('lay_detail/<int:pk>/blue',lay_detail_view_blue, name='blue'),
    path('lay_detail/<int:pk>/yellow',lay_detail_view_yellow, name='yellow'),
]
