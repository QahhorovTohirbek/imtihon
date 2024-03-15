from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about_us, name='about'),
    path ('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog')
]
