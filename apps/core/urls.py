from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('parts/cpus', views.cpus, name='All CPUs'),
    path('parts/rams', views.under_construction, name='All RAMs'),
    path('parts/motherboards', views.under_construction, name='All Motherboards'),
    path('parts/coolings', views.under_construction, name='All Cooling Accessories'),
    path('parts/gpus', views.under_construction, name='All GPUs'),
    path('parts/cases', views.under_construction, name='All Cases'),
    path('parts/storages', views.under_construction, name='All Storages'),
    path('parts/accessories', views.under_construction, name='All other accessories'),
]
