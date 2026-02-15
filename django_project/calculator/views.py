from django.shortcuts import render
from django.http import Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
}

def home(request):
    return render(request, 'calculator/home.html')

def recipe_view(request, dish):
    recipe = DATA.get(dish)

    if recipe is None:
        raise Http404("Рецепт не найден")

    servings = request.GET.get('servings', 1)

    try:
        servings = int(servings)
    except ValueError:
        servings = 1

    calculated_recipe = {
        ingredient: amount * servings
        for ingredient, amount in recipe.items()
    }

    context = {
        'recipe': calculated_recipe
    }

    return render(request, 'calculator/index.html', context)