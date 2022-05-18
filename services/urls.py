from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name="services"),
    path('<slug:slug>/', views.category, name="category")
]
