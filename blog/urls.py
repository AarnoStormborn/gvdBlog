from django.urls import path
from . import views

urlpatterns = [
    # blogs/
    path("home/", views.index, name='index')
]