from django.urls import path
from ProfileAdd import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.helloworld, name='hello', ),
    path('firstpage', views.firstPage, name='firstpage'),
    path('secondpage', views.secondpage, name='secondpage'),
    path('thirdpage', views.thirdpage, name='thirdpage'),
    path('hnypage', views.hnypage, name='hnppage'),
]