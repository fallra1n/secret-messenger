from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from uuid import uuid4

storage = {}


def index(request) -> HttpResponse:
    if request.method == 'POST':
        message = request.POST.get('message')
        ttl = request.POST.get('ttl')

        uid = uuid4()
        global storage
        storage[str(uid)] = message
        host = request.META.get('HTTP_HOST')

        return render(request, 'smessages/key.html', {'key': 'http://' + str(host) + '/smessenger/smessages/' + str(uid) + '/'})

    return render(request, 'smessages/index.html')


def get_secret_message(request, key: str) -> HttpResponse:
    message = storage[key]
    return render(request, 'smessages/message.html', {'message': message})


def page_not_found(request, exception) -> HttpResponseNotFound:
    return render(request, 'smessages/404.html')
