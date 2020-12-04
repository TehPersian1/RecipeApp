#!/usr/bin/env/python3
import requests
import os
from time import sleep
import tkinter as tk
HEIGHT = 800
WIDTH = 1600

# CPSC 254 FINAL PROJECT
# THE MEAL DB RECIPE APP
# CREATED BY SHERVIN, MILES, AND SUNNY
# Professor David Heckathorn


# display our main title to the console on program launch
def show_title():
    print("My Recipe Program")
    print()

# This function is no longer needed as well will be implementing the GUI, but we included it as part of the original
# source code
# Display Command Menu to the user
def show_menu():
    print("COMMAND MENU")
    print("1 - List all Categories")
    print("2 - List all meals for a Category")
    print("3 - Search meal by Name")
    print("4 - Search meal by Area")
    print("0 - Exit the Program")
    print()


# Lists all available categories to the GUI
def list_categories(categories, recipe_label):
    print("CATEGORIES")
    print("-" * 20)
    label_list = []
    for i in range(len(categories)):
        category = categories[i]
        print(category.get_category())
        label_list.append(category.get_category())

    recipe_label['text'] = label_list[0] + ', ' + label_list[1] + ', ' + label_list[2] + ', ' + label_list[3] + '\n ' +\
                           label_list[4] + ', ' + label_list[5] + ', ' + label_list[6] + ', ' + label_list[7] + '\n' +\
                           label_list[8] + ', ' + label_list[9] + ', ' + label_list[10] + ', ' + label_list[11] + '\n'
    recipe_label['font'] = 'times 32'
    print()


# generates a list of meals based on the category selected and displays them to the GUI
def list_meals_by_category(category, meals, recipe_label):
    print(category.upper() + " MEALS")
    print("-" * 30)
    label_meals = []
    for i in range(len(meals)):
        meal = meals[i]
        print(meal.get_meal())
        label_meals.append(meal.get_meal())
    recipe_label['font'] = "times 12"
    recipe_label['text'] = label_meals[0] + '\n' + label_meals[1] + '\n' + label_meals[2] + '\n' + label_meals[3] + '\n' \
    + label_meals[4] + '\n' + label_meals[5] + '\n' + label_meals[6] + '\n' + label_meals[7] + '\n' + label_meals[8] \
    + '\n' + label_meals[9] + '\n' + label_meals[10] + '\n' + label_meals[11] + '\n' + label_meals[12] + '\n' \
    + label_meals[13] + '\n' + label_meals[14] + '\n' + label_meals[15] + '\n' + label_meals[16] + '\n' + label_meals[17] \
    + '\n' + label_meals[18] + '\n' + label_meals[19] + '\n' + label_meals[20]
    print()


# searches the categories to make sure the user's input in the GUI was valid.
def search_meal_by_category(categories, entry, recipe_label):
    lookup_category = entry
    found = False

    for i in range(len(categories)):
        category = categories[i]
        if category.get_category().lower() == lookup_category.lower():
            found = True
            break

    if found:
        meals = requests.get_meals_by_category(lookup_category)
        list_meals_by_category(lookup_category, meals, recipe_label)
    else:
        print("invalid Category, please try again.")


# displays all the information about the recipe, including ingredients, measurements, instructions, and the youtube link
def display_meal(recipe, recipe_label):
    os.system('cls')
    print()
    print("View a Step by Step guide:", recipe.get_youtube())
    print()
    print("Recipe:", recipe.get_meal())
    print("Ingredients: ")
    for i in range(10):
        if recipe.ingredients[i] != " " or recipe.ingredients[i] != '':
            print(recipe.ingredients[i] + " - " + recipe.measures[i])
    print()
    print("-" * 64)
    recipe_label["text"] = recipe.get_instructions()
    recipe_label['font'] = 'times 13'

    print()


# Pulls the information from the GUI search bar and uses that to search for the meal
def search_meal_by_name(entry, recipe_label):
    lookup_meal = entry
    meal = requests.get_meals_by_name(lookup_meal)

    if meal:
        display_meal(meal, recipe_label)
    else:
        print("A recipe for this meal was not found")


# lists different meals based on an area or geographic region that the user types in
def list_meal_by_area(search, areas, recipe_label):
    print(search.upper(), "MEALS")
    print("-" * 64)
    recipe_area = []
    for i in range(len(areas)):
        area = areas[i]
        print(area.get_meal())
        recipe_area.append(areas[i].get_meal())
    recipe_label['font'] = 'times 16'
    recipe_label['text'] = recipe_area[0] + '\n' + recipe_area[1] + '\n' + recipe_area[2] + '\n' + recipe_area[3] + '\n' \
    + recipe_area[4] + '\n' + recipe_area[5] + '\n' + recipe_area[6] + '\n' + recipe_area[7] + '\n' + recipe_area[8] \
    + '\n' + recipe_area[9] + '\n' + recipe_area[10] + '\n' + recipe_area[11] + '\n' + recipe_area[12] + '\n' + recipe_area[13]
    print()


def search_meals_by_area(entry, recipe_label):
    search = entry
    found = False

    if         search.lower() == "canadian"   or search.lower() == "american"     or search.lower() == "chinese"\
            or search.lower() == "vietnamese" or search.lower() == "british"      or search.lower() == "french"\
            or search.lower() == "jamaican"   or search.lower() == "dutch"        or search.lower() == "egyptian"\
            or search.lower() == "greek"      or search.lower() == "indian"       or search.lower() == "japanese" \
            or search.lower() == "irish"      or search.lower() == "italian"      or search.lower() == "kenyan"\
            or search.lower() == "malaysian"  or search.lower() == "mexican"      or search.lower() == "moroccan"\
            or search.lower() == "croatian"   or search.lower() == "Norwegian"    or search.lower() == "portuguese"\
            or search.lower() == "russian"    or search.lower() == "aregentinian" or search.lower() == "spanish"\
            or search.lower() == "slovakian"  or search.lower() == "thai"         or search.lower() == "arabic":
        found = True

    if found:
        areas = requests.get_meals_by_area(search)
        list_meal_by_area(search, areas, recipe_label)
    else:
        print("Invalid Area, Please try again.")
    print()


def main():
    show_title()
    categories = requests.get_categories()
    # start of gui
    root = tk.Tk()
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    bg_image = tk.PhotoImage(file='background.png')
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(relwidth=1, relheight=1, )
    frame1 = tk.Frame(root, bg='#7B7472', bd=5)
    frame1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
    frame2 = tk.Frame(root, bg='#7B7472', bd=4)
    frame2.place(relx=0.1, rely=0.23, relwidth=0.8, relheight=0.65)
    recipe_label = tk.Label(frame2, bg='#E7F6B3', text='')
    recipe_label.place(relheight=1, relwidth=1)

    button1 = tk.Button(frame1, text="Categories", command=lambda: list_categories(categories, recipe_label))
    button1.place(relx=0.47, relheight=1, relwidth=0.1)
    button2 = tk.Button(frame1, text="Search Meal", command=lambda: search_meal_by_name(entry.get(), recipe_label))
    button2.place(relx=0.58, relheight=1, relwidth=0.12)
    button3 = tk.Button(frame1, text="Expand", command=lambda: search_meal_by_category(categories, entry.get(), recipe_label))
    button3.place(relx=0.71, relheight=1, relwidth=0.1)
    button4 = tk.Button(frame1, text="Area Search", command=lambda: search_meals_by_area(entry.get(), recipe_label))
    button4.place(relx=0.82, relheight=1, relwidth=0.12)
    entry = tk.Entry(frame1, bg='#E7F6B3', font='times 20')
    entry.place(relx=0, relheight=1, relwidth=0.45)

    root.mainloop()
    # end of gui

    #   while True:
     #   command = input("Command: ")
     #   if command == "1":
     #      list_categories(categories)
     #   elif command == "2":
    #        search_meal_by_category(categories)
    #    elif command == "3":
     #       search_meal_by_name(entry)
    #    elif command == "0":
     #       print("Thank you for using my program!")
    #        break
     #   elif command == "4":
     #       search_meals_by_area()
     #   else:
    #        print("Not a valid command. Please try again \n")
    #        sleep(1)
     #       os.system('cls')

# ^ this portion of code is commented out because we implemented a gui, so it is no longer needed.

if __name__ == '__main__':
    main()
