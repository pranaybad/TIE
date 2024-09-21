from django.urls import path
from . import views
from django.urls import  include

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('jobopenings', include('jobopenings.urls')),
    path('learningapp', include('learningapp.urls')),
    path('freelanceapp', include('freelanceapp.urls')),
]
