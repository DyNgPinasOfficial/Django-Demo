from django.urls import path
from . import views

urlpatterns = [
    path('<int:number>/', views.average, name='average'),
]