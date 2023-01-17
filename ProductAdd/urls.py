from django.contrib import admin
from django.urls import  path,include
from ProductAdd import  views
urlpatterns = [
    # path('',views.productadd_home,name='productadd_home'),
    path('testbt',views.testbt,name='testbt'),
]