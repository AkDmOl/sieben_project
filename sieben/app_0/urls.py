from django.urls import path

from . import views

urlpatterns = [
    path('', views.simp_resp, name='index'),
]