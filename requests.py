from urllib import request, parse
import json

from objects import Category, Meal, Recipe, Area


# get a list of the different categories
def get_categories():
    url = 'https://www.themealdb.com/api/json/v1/1/list.php?c=list'
    f = request.urlopen(url)
    categories = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for category_data in data['meals']:
            category = Category(category_data['strCategory'])

            categories.append(category)
    except (ValueError, KeyError, TypeError):
        print("Json Format Error")

    return categories


# get a list of the meals within each categories
def get_meals_by_category(category):
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php?c=' + category
    f = request.urlopen(url)
    meals = []

    try:
        data = json.loads(f.read().decode('utf-8'))
        for meal_data in data['meals']:
            category = Meal(meal_data['idMeal'],
                            meal_data['strMeal'],
                            meal_data['strMealThumb'])
            meals.append(category)

    except (ValueError, KeyError, TypeError):
        print("Json Format Error")

    return meals


# parse a meal name into the query to search for meals matching that name.
def get_meals_by_name(meal):
    url = 'https://www.themealdb.com/api/json/v1/1/search.php?s=' + parse.quote(meal)
    f = request.urlopen(url)

    recipe = None
    try:
        data = json.loads(f.read().decode('utf-8'))
        for recipe_data in data['meals']:

            recipe = Recipe(recipe_data['idMeal'],
                            recipe_data['strMeal'],
                            recipe_data['strCategory'],
                            recipe_data['strInstructions'],
                            recipe_data['strMealThumb'],
                            recipe_data['strYoutube'],
                            )
            recipe.ingredients.append(recipe_data['strIngredient1'])
            recipe.ingredients.append(recipe_data['strIngredient2'])
            recipe.ingredients.append(recipe_data['strIngredient3'])
            recipe.ingredients.append(recipe_data['strIngredient4'])
            recipe.ingredients.append(recipe_data['strIngredient5'])
            recipe.ingredients.append(recipe_data['strIngredient6'])
            recipe.ingredients.append(recipe_data['strIngredient7'])
            recipe.ingredients.append(recipe_data['strIngredient8'])
            recipe.ingredients.append(recipe_data['strIngredient9'])
            recipe.ingredients.append(recipe_data['strIngredient10'])
            recipe.ingredients.append(recipe_data['strIngredient11'])
            recipe.ingredients.append(recipe_data['strIngredient12'])
            recipe.ingredients.append(recipe_data['strIngredient13'])
            recipe.ingredients.append(recipe_data['strIngredient14'])
            recipe.ingredients.append(recipe_data['strIngredient15'])
            recipe.ingredients.append(recipe_data['strIngredient16'])
            recipe.ingredients.append(recipe_data['strIngredient17'])
            recipe.ingredients.append(recipe_data['strIngredient18'])
            recipe.ingredients.append(recipe_data['strIngredient19'])
            recipe.ingredients.append(recipe_data['strIngredient20'])
            recipe.measures.append(recipe_data['strMeasure1'])
            recipe.measures.append(recipe_data['strMeasure2'])
            recipe.measures.append(recipe_data['strMeasure3'])
            recipe.measures.append(recipe_data['strMeasure4'])
            recipe.measures.append(recipe_data['strMeasure5'])
            recipe.measures.append(recipe_data['strMeasure6'])
            recipe.measures.append(recipe_data['strMeasure7'])
            recipe.measures.append(recipe_data['strMeasure8'])
            recipe.measures.append(recipe_data['strMeasure9'])
            recipe.measures.append(recipe_data['strMeasure10'])
            recipe.measures.append(recipe_data['strMeasure11'])
            recipe.measures.append(recipe_data['strMeasure12'])
            recipe.measures.append(recipe_data['strMeasure13'])
            recipe.measures.append(recipe_data['strMeasure14'])
            recipe.measures.append(recipe_data['strMeasure15'])
            recipe.measures.append(recipe_data['strMeasure16'])
            recipe.measures.append(recipe_data['strMeasure17'])
            recipe.measures.append(recipe_data['strMeasure18'])
            recipe.measures.append(recipe_data['strMeasure19'])
            recipe.measures.append(recipe_data['strMeasure20'])

    except (ValueError, TypeError, KeyError):
        print("Json Format Error")

    return recipe


def get_meals_by_area(search):
    url = 'https://www.themealdb.com/api/json/v1/1/filter.php?a=' + search
    f = request.urlopen(url)
    meals = []
    try:
        data = json.loads(f.read().decode('utf-8'))

        for area_data in data['meals']:
            area = Meal(area_data['idMeal'],
                        area_data['strMeal'],
                        area_data['strMealThumb'])
            meals.append(area)
    except(ValueError, TypeError, KeyError):
        print("Json Format Error")

    return meals
