from django.urls import path
from . import views

#same as base/url.py
urlpatterns = [
    path('', views.getRoutes),
    path('rooms/', views.getRooms),
    path('rooms/<str:pk>/', views.getRoom)

]