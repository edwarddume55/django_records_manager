from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('user_logout', views.user_logout, name='user_logout'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('create_record', views.create_record, name='create_record'),

    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('record/<int:pk>', views.record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
]