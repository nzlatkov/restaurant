from django.urls import path

from common.views import login, logout, register

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register')
]