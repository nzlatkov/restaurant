from django.urls import path

from menu.views import menu, food_details, add_food, edit_food, delete_food

urlpatterns = [
    path('', menu, name='menu'),
    path('details/<int:pk>/', food_details, name='food details'),
    path('add_food/', add_food, name='add food'),
    path('edit_food/<int:pk>/', edit_food, name='edit food'),
    path('delete_food/<int:pk>/', delete_food, name='delete food'),
]