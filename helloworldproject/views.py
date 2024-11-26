from pathlib import Path

from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView


def helloworldfunction(request: HttpRequest):
    returnedObject = HttpResponse(Path(__file__).resolve())
    return returnedObject


class HelloWorldClass(TemplateView):
    template_name = "hello.html"
