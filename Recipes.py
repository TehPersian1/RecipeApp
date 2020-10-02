#!/usr/bin/env/python3
import requests


# display our main title to the console
def show_title():
    print("My Recipe Program")
    print()


# Display Command Menu to the user
def show_menu():
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all meals for a Category")
    print("3 - Search meal by Name")
    print("4 - Search meal by Area")
    print("0 - Exit the Program")
    print()


# Lists all available categories to the main console.
def list_categories(categories):
    print("CATEGORIES")
    print("-" * 20)
    for i in range(len(categories)):
        category = categories[i]
        print(category.get_category())
    print()


# generates a list of meals based on the category selected
def list_meals_by_category(category, meals):
    print(category.upper() + " MEALS")
    print("-" * 30)
    for i in range(len(meals)):
        meal = meals[i]
        print(meal.get_meal())
    print()


# searches the categories to make sure the user's input was valid.
def search_meal_by_category(categories):
    lookup_category = input("Enter a Category: ")
    found = False

    for i in range(len(categories)):
        category = categories[i]
        if category.get_category().lower() == lookup_category.lower():
            found = True
            break

    if found:
        meals = requests.get_meals_by_category(lookup_category)
        list_meals_by_category(lookup_category, meals)
    else:
        print("invalid Category, please try again.")


# displays the meal title as well as the recipe
def display_meal(recipe):
    print()
    print("Recipe:", recipe.get_meal())
    print("-" * 64)
    print("Instructions:", recipe.get_instructions())
    print()


# searches for a meal by prompting the user to enter its name
def search_meal_by_name():
    lookup_meal = input("Enter Meal Name: ")
    meal = requests.get_meals_by_name(lookup_meal)

    if meal:
        display_meal(meal)
    else:
        print("A recipe for this meal was not found")


def list_meal_by_area(search, areas):
    print(search.upper(), "MEALS")
    print("-" * 64)
    for i in range(len(areas)):
        area = areas[i]
        print(area.get_meal())
    print()
# ask how to format this so it holds the values I want.


def search_meals_by_area():
    search = input("Enter Area: ")
    found = False

    # ask how to format this so that it matches the search
    if search.lower() == "canadian" or search.lower() == "american" or search.lower() == "chinese"\
            or search.lower() == "vietnamese" or search.lower() == "british"      or search.lower() == "french"\
            or search.lower() == "jamaican"   or search.lower() == "dutch"        or search.lower() == "egyptian"\
            or search.lower() == "greek"      or search.lower() == "indian"       or search.lower() == "japanese" \
            or search.lower() == "irish"      or search.lower() == "italian"      or search.lower() == "kenyan"\
            or search.lower() == "malaysian"  or search.lower() == "mexican"      or search.lower() == "moroccan"\
            or search.lower() == "croatian"   or search.lower() == "Norwegian"    or search.lower() == "portuguese"\
            or search.lower() == "russian"    or search.lower() == "aregentinian" or search.lower() == "spanish"\
            or search.lower() == "slovakian"  or search.lower() == "thai"         or search.lower() == "arabic":
        found = True

    # make sure this is the right format for testing the search
    if found:
        areas = requests.get_meals_by_area(search)
        list_meal_by_area(search, areas)
    else:
        print("Invalid Area, Please try again.")
    print()


def main():
    show_title()
    show_menu()

    categories = requests.get_categories()

    while True:
        command = input("Command: ")
        if command == "1":
            list_categories(categories)
        elif command == "2":
            search_meal_by_category(categories)
        elif command == "3":
            search_meal_by_name()
        elif command == "0":
            print("Thank you for using my program!")
            break
        elif command == "4":
            search_meals_by_area()
        else:
            print("Not a valid command. Please try again \n")


if __name__ == '__main__':
    main()
