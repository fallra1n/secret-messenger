from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request) -> HttpResponse:
    if request.method == 'POST':
        message = request.POST.get('message')
        ttl = request.POST.get('ttl')

        return render(request, 'smessages/key.html', {'key': message + ttl})

    return render(request, 'smessages/index.html')


def get_secret_message(request, key: str) -> HttpResponse:
    return HttpResponse(f"{key}")


def page_not_found(request, exception) -> HttpResponseNotFound:
    return render(request, 'smessages/404.html')
