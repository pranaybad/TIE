from django.urls import path
from . import views

urlpatterns = [
    path('learningapp', views.learningapp, name='learningapp')
]
