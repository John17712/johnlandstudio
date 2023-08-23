from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('contact.html', views.contact, name='contact'),
    path('service.html', views.service, name='service'),
    path('shop.html', views.shop, name='shop'),
    path('appointment.html', views.appointment, name='appointment'),
    
]
