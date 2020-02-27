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
    path('',orde,name='order'),
    path('lay',laye,name='lay'),
    path('lays',lay_detail,name='list1'),
    path('lay_detail/<int:pk>/red',lay_detail_view_red, name='red'),
    path('lay_detail/<int:pk>/blue',lay_detail_view_blue, name='blue'),
    path('lay_detail/<int:pk>/yellow',lay_detail_view_yellow, name='yellow'),
    path('lay_detail/<int:pk>/red1',lay_detail_view_red1, name='red1'),
    path('lay_detail/<int:pk>/blue1',lay_detail_view_blue1, name='blue1'),
    path('lay_detail/<int:pk>/yellow1',lay_detail_view_yellow1, name='yellow1'),
    path('lay_detail/<int:pk>/red2',lay_detail_view_red2, name='red2'),
    path('lay_detail/<int:pk>/blue2',lay_detail_view_blue2, name='blue2'),
    path('lay_detail/<int:pk>/yellow2',lay_detail_view_yellow2, name='yellow2'),
    path('roll',roll,name='roll'),
    path('rolls',roll_detail,name='list2'),
    path('roll_detail/<int:pk>/',roll_detail_view, name='roll_detail'),
]
