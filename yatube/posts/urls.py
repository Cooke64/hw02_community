from django.urls import path
from .views import index, group_posts

app_name = 'post'

urlpatterns = [
    path('', index, name='main'),
    path('group/<slug:slug>/', group_posts, name='group'),
]
