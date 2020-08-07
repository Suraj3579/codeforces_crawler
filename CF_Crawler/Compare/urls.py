from django.urls import path
from . import views

urlpatterns = [
    path('', views.compare, name='compare'),
    path('compare_analysis/', views.compare_analysis, name='compare_analysis'),
    ]
