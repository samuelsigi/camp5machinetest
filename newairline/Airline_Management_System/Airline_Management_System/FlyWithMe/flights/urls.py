from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('flights/', views.flight_list, name='flight_list'),
    path('flights/edit/<int:flight_id>/', views.edit_flight, name='edit_flight'),
    path('flights/delete/<int:flight_id>/', views.delete_flight, name='delete_flight'),
    path('flights/add/', views.add_flight, name='add_flight'),
    path('flights/search/', views.search_flight, name='search_flight'),
    path('flights/login/', views.user_login, name='user_login'),

]
