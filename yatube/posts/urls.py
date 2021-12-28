from django.urls import path

from . import views
from .views import *

app_name = 'post'

urlpatterns = [
    path('', index, name='main'),
    path('group/<slug:slug>/', group_posts, name='group'),
]
