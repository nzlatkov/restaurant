from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from menu.forms import FoodForm
from menu.models import Food


def menu(request):
    food_list = Food.objects.all()

    context = {
        'food_types': [
            [food for food in food_list if food.type == 0],
            [food for food in food_list if food.type == 1],
            [food for food in food_list if food.type == 2],
            [food for food in food_list if food.type == 3],
            [food for food in food_list if food.type == 4],
            [food for food in food_list if food.type == 5],
            [food for food in food_list if food.type == 6],
            [food for food in food_list if food.type == 7],
            [food for food in food_list if food.type == 8],
            [food for food in food_list if food.type == 9],
        ],
        'f': [
            'Топли напитки',
            'Безалкохолни напитки',
            'Пиво',
            'Твърд алкохол',
            'Салати',
            'Студени мезета',
            'Топли мезета',
            'Скара',
            'Сачове',
            'Ядки',
        ]
    }

    return render(request, 'menu.html', context)

@login_required
def food_details(request, pk):
    food = Food.objects.get(pk=pk)
    current_user = User.objects.get(pk=request.user.id)

    is_authorized = current_user.is_superuser or current_user is food.submitter

    context = {
        'food': Food.objects.get(pk=pk),
        'is_authorized': is_authorized,
    }

    return render(request, 'food-details.html', context)


def add_food(request):
    if request.method == 'GET':
        context = {
            'form': FoodForm(),
        }

        return render(request, 'add_food.html', context)
    else:
        if request.method == 'POST':
            form = FoodForm(request.POST, request.FILES)

            if form.is_valid():
                food = form.save(commit=True)
                food.submitter = User.objects.get(pk=request.user.id)
                food.save()
                return redirect('menu')

            context = {
                'form': form,
            }

            return render(request, 'add_food.html', context)



def edit_food(request, pk):
    food = Food.objects.get(pk=pk)

    current_user = User.objects.get(pk=request.user.id)

    if not current_user.is_superuser and current_user is not food.submitter:
        return redirect('home')

    if request.method == 'GET':
        context = {
            'form': FoodForm(instance=food),
            'food': food,
        }

        return render(request, 'edit_food.html', context)
    else:
        subm = food.submitter
        form = FoodForm(request.POST, request.FILES, instance=food)

        if form.is_valid():
            food = form.save(commit=True)
            food.submitter = subm
            food.save()
            return redirect('menu')

        context = {
            'form': form,
            'food': food,
        }

        return render(request, 'edit_food.html', context)


def delete_food(request, pk):
    food = Food.objects.get(pk=pk)
    food.delete()

    return redirect('menu')

