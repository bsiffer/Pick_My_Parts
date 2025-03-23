from django.urls import path
from .views.cooling_accessory_view import cooling_accessory_view
from .views.home import home
from .views.about import about
from .views.cpus import cpus
from .views.storage_view import storage_view
from .views.under_construction import under_construction
from .views.computer_case_view import computer_case_view

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('parts/cpus', cpus, name='All CPUs'),
    path('parts/rams', under_construction, name='All RAMs'),
    path('parts/motherboards', under_construction, name='All Motherboards'),
    path('parts/cooling-accessories', cooling_accessory_view, name='All Cooling Accessories'),
    path('parts/gpus', under_construction, name='All GPUs'),
    path('parts/computer-cases', computer_case_view, name='All Computer Cases'),
    path('parts/storages', storage_view, name='All Storages'),
    path('parts/accessories', under_construction, name='All other accessories'),
]
