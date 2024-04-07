import datetime
import logging
from django.shortcuts import render
from .models import Client, Order, Enrollment
from django.http import HttpResponse
from datetime import timedelta, datetime

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    html = '''
   <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        
        MaxBot
        
    </title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        main {
            flex: 1;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
        }
    </style>
</head>
<body>
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="#">MaxBot</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Наши продукты</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">О нас</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Контакты</a>
                        </li>
                    </ul>
                </div>
               
            </div>
        </nav>
    </header>

    <main class="container">
        
        <h1>Добро пожаловать на сайт Компании MaxBot!</h1>
        
        
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2024 MaxBot Company. All Rights Reserved.</p>
        </div>
    </footer>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    '''
    return HttpResponse(html)


def about(request):
    html = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        
        MaxBot
        
    </title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }
        main {
            flex: 1;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
        }
    </style>
</head>
<body>
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="#">MaxBot</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Наши продукты</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">О нас</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Контакты</a>
                        </li>
                    </ul>
                </div>
               
            </div>
        </nav>
    </header>

    <main class="container">
        
        <p>Мы занимаемся разработкой "умных" ассистентов с применением технологий ИИ. Создадим модель, которая обучится на Ваших данных</p>
        
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2024 MaxBot Company. All Rights Reserved.</p>
        </div>
    </footer>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
    
    '''
    logger.info('About us page accessed')
    return HttpResponse(html)


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


def new_orders(request):
    return render(request, 'myapp/new_orders.html')
