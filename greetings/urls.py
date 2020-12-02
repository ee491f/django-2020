from django.urls import path
from . import views

app_name = 'greetings'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new/', views.CreateView.as_view(), name='create'),
]