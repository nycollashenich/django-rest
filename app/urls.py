from django.urls import path
from .views import tod_list

urlpatterns = [
    path('', tod_list),
]
