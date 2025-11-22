from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/<int:pk>/', views.checkout, name='checkout'),
    path('success/<int:pk>/', views.success, name='success'),
    path('discussion/', views.discussion, name='discussion'),
    path('lynk/', views.lynk, name='lynk'),
    path('diskusi/like/<int:pk>/', views.like_comment, name='like_comment'),
    path('payment/<int:pk>/', views.payment, name='payment'),
]