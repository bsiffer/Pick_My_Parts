from django.urls import path
from .views.detail_view import detail_view
from .views.suggestions import suggestions
from .views.build_view import build
from .views.cooling_accessory_view import cooling_accessory_view
from .views.gpu_view import gpu_view
from .views.home import home
from .views.about import about
from .views.cpu_view import cpu_view
from .views.motherboard_view import motherboard_view
from .views.power_supply_view import power_supply_view
from .views.ram_view import ram_view
from .views.storage_view import storage_view
from .views.under_construction import under_construction
from .views.computer_case_view import computer_case_view

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('build', build, name='build'),
    path('parts/cpus', cpu_view, name='All CPUs'),
    path('parts/rams', ram_view, name='All RAMs'),
    path('parts/motherboards', motherboard_view, name='All Motherboards'),
    path('parts/cooling-accessories', cooling_accessory_view, name='All Cooling Accessories'),
    path('parts/gpus', gpu_view, name='All GPUs'),
    path('parts/computer-cases', computer_case_view, name='All Computer Cases'),
    path('parts/storages', storage_view, name='All Storages'),
    path('parts/power-supplies', power_supply_view, name='All Power Supplies'),
    path('parts/accessories', under_construction, name='All other accessories'),
    path('api/suggestions', suggestions, name='Suggestions based on current selection'),
    path('parts/<str:model_name>/<int:sku>/', detail_view, name='power_supply_detail'),
]
