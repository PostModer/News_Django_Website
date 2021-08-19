from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='Homepage'),
    path('category/<int:category_id>/', get_category, name='category'),
]