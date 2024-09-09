from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('<int:id>', views.car, name='car'),
    path('', views.home, name='home'),
]
