from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/', views.difficult, name='difficult'),
    path('<str:name>/increment/', views.increment_envelope_count, name='increment_envelope_count'),
]
