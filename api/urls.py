from django.urls import path
from .views import home, item_list

urlpatterns = [
    path('', home, name='home'),
    path('items/', item_list, name='item_list'),
]
