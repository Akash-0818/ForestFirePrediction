from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_fire, name='predict_fire'),
]
