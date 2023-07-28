from django.urls import path
from main.views import IndexView


urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
]
