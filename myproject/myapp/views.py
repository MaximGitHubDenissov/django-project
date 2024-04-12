import datetime
import logging
from django.shortcuts import render
from .models import Client, Order, Enrollment, Product
from datetime import timedelta, datetime
from .forms import ProductForm

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'base.html')


# Create your views here.

def get_orders_by_client(request, client_id, filter_name):
    today = datetime.utcnow()
    if filter_name == 'week':
        start_date = today - timedelta(days=7)
    elif filter_name == 'month':
        start_date = today - timedelta(days=30)
        print(start_date)
    elif filter_name == 'year':
        start_date = today - timedelta(days=365)
        print(start_date)
    else:
        start_date = None

    client = Client.objects.filter(pk=client_id).first()
    if start_date:
        orders = Order.objects.filter(client=client, date_ordered__range=[start_date, today])
        print(orders)
    else:
        orders = Order.objects.filter(client=client).all()
    enrolls_res = {}
    for order in orders:
        enrolls = Enrollment.objects.filter(order=order).all()
        enrolls_res[order] = enrolls

    context = {'orders': enrolls_res}
    return render(request, 'myapp/orders.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            product = Product(name=name, description=description, price=price, quantity=quantity, image=image)
            product.save()
            img_obj = product
            logger.info(f"Создан новый продукт {product.name} ")
            return render(request, 'myapp/add_product.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProductForm()
    return render(request, 'myapp/add_product.html', {'form': form})
