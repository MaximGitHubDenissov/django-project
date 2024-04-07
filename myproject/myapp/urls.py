from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('orders/<int:client_id>/<str:filter_name>', views.get_orders_by_client, name='orders'),
]
