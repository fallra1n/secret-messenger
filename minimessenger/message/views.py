from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return HttpResponse("hello world")


def get_secret_message(request, key: str):
    return HttpResponse(f"{key}")


def page_not_found(request, exception):
    return HttpResponseNotFound("str not found")
