from django.urls import path
from .views.home import home
from .views.about import about
from .views.cpus import cpus
from .views.under_construction import under_construction
from .views.cases import cases

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('parts/cpus', cpus, name='All CPUs'),
    path('parts/rams', under_construction, name='All RAMs'),
    path('parts/motherboards', under_construction, name='All Motherboards'),
    path('parts/coolings', under_construction, name='All Cooling Accessories'),
    path('parts/gpus', under_construction, name='All GPUs'),
    path('parts/cases', cases, name='All Cases'),
    path('parts/storages', under_construction, name='All Storages'),
    path('parts/accessories', under_construction, name='All other accessories'),
]
