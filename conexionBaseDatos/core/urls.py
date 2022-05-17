from django.urls import path
from .views import home, formCategoria

urlpatterns = [
    path('', home),
    path('formCategoria', formCategoria)
]