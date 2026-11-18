from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('community/<slug:slug>/', views.category_detail_view, name='category_detail'),
    path('community/<slug:slug>/new/', views.create_post_view, name='create_post'),
    path('post/<int:pk>/', views.post_detail_view, name='post_detail'),
]