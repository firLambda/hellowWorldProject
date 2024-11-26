from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.


def helloworldappview(request: HttpRequest):
    return HttpResponse("app is called")


def testApp(request: HttpRequest):
    return HttpResponse("testApp")
