from django.urls import path

from . import views

app_name = 'portal.main'

urlpatterns = [
    path('', views.index,name='index'),
]