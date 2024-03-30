from django.urls import path

from . import views

app_name = 'clockboard'


urlpatterns = [
    path('', views.index, name='index'),
    path('board/', views.dashboard, name='dashboard'),
    path('reset/<int:clock_id>/', views.reset_clock, name='reset_clock'),
]
