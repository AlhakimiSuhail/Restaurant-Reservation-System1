from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user', views.homepage_user, name='homepage_user'),
    path('restaurant', views.homepage_restaurant, name='homepage_restaurant'),
    path('table_management', views.table_management, name='table_management'),
    path('userreservations', views.User_Reservations, name='User_Reservations'),
    path('delete_reservation/<int:pk>/', views.delete_reservation, name="delete_reservation"),
    path('user_delete_reservation/<int:pk>/', views.user_delete_reservation, name="user_delete_reservation"),
    path('create_reservation', views.create_reservation_times, name="create_reservation"),
    path('create_reservation_user', views.create_reservation_user_times, name="create_reservation_user")
]
