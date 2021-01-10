from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная Страница',
        'values': ['Some', 'Hello', '132'],
        'obj': {
            'car': 'BMW M5',
            'age': '18',
            'hobby': 'Football',
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')
