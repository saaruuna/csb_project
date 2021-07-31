from django.urls import path
from pages import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('add/', views.addView, name='add'),
    path('delete/', views.deleteView, name='delete'),
]
