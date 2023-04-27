from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from uuid import uuid4
from django.core.cache import cache


def index(request) -> HttpResponse:
    if request.method == 'POST':
        message = request.POST.get('message')
        ttl = request.POST.get('ttl')
        uid = uuid4()
        cache.set(str(uid), message, int(ttl))
        # try:
        #     cache.set(str(uid), message, int(ttl))
        # except:
        #     response_html = 'smessages/500.html'
        #     return render(request, response_html)

        host = request.META.get('HTTP_HOST')
        target_path = 'http://' + \
                      str(host) + '/smessenger/smessages/' + str(uid) + '/'
        response_html = 'smessages/key.html'

        return render(request, response_html,
                      {'key': target_path})

    response_html = 'smessages/index.html'
    return render(request, response_html)


def get_secret_message(request, key: str) -> HttpResponse:
    message = cache.get(key)
    if message is None:
        response_html = 'smessages/400.html'
        return render(request, response_html)

    try:
        cache.delete(key)
    except:
        response_html = 'smessages/500.html'
        return render(request, response_html)

    response_html = 'smessages/message.html'
    return render(request, response_html, {'message': message})


def page_not_found(request, exception) -> HttpResponseNotFound:
    return render(request, 'smessages/404.html')
