from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.CarListCreate.as_view(), name="car-list-create"),
    path('cars/<int:id>', views.CarDetail.as_view(), name="car-detail"),
    path('cars/<int:id>/comments', views.CommentListCreate.as_view(), name="comment-list-create"),
]
