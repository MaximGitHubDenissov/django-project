from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders/<int:client_id>/<str:filter_name>', views.get_orders_by_client, name='orders'),
    path('add_product', views.add_product, name='add_product')
]
