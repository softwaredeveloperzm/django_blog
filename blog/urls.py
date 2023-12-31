from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('signin/', views.signin),
    path('signup/',views.signup),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('logout/', views.logoutUser, name="logout"),
]