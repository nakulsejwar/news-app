from django.urls import path
from .views import HackerNewsAPI

urlpatterns = [
    path('hackernews/', HackerNewsAPI.as_view(), name='hackernews'),
]
