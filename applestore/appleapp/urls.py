from django.urls import  path
from . import views

urlpatterns = [
    path("home/", views.my_view),
    path('get_product/<product_id>', views.retire_json_file),
]