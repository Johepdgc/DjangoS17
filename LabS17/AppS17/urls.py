from django.urls import path
from .views import all_lists

urlpatterns = [
    path('', all_lists, name='all_lists'),
]