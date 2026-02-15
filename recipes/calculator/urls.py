from django.urls import path
from .views import recipe_view, home

urlpatterns = [
    path('', home),
    path('<str:dish>/', recipe_view),
]