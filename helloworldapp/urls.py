from django.urls import include, path

from .views import helloworldappview

urlpatterns = [
    path("helloworldapp/", helloworldappview)
]
