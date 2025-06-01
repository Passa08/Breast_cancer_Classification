from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('detection/', views.detection, name='detection'),
    path('about/', views.about, name='about'),
] 