import json
import os
import nltk
from nltk.stem import WordNetLemmatizer
import pprint

# initialize lemmatizer for smarter searching later

lemmatizer = WordNetLemmatizer()

# load in all the recipes from the recipe folder

recipes_dir = os.path.join(os.getcwd(), 'recipes')
recipes_json = []

for recipe_file in os.listdir(recipes_dir):
    path = os.path.join(recipes_dir, recipe_file)
    with open(path, encoding='utf-8') as file:
        recipes_json.append(json.load(file))

# user prompt
def main_prompt():
    print('What kind of search would you like to perform?')
    print('1. Title search') # use a keyword to search all the titles (names) of recipes and return them
    print('2. Ingredient search') # use a keyword to search all ingredients in recipes and return them
    print('3. Category search') # use a keyword to search all categories and return recipes in those categories
    print('Type "main" at any time to return to this menu.')
    print('Type "quit" at any time to quit.')
    user_response = input()

    return user_response

def validate_command(user_input):
    if (user_input != 'main' or user_input != 'quit') and user_input.isdigit() == False:
        print('Invalid command.  Please enter something else.')
        user_response = input()
    else:
        user_response = user_input

    return user_response

# to-do: integrate this function for validating user input

def output_recipe(recipejson):
    print('Type "main" or "quit" to continue (or quit).')
    user_response = input()

    return user_response

# add a function for outputting the recipe nicely

# begin executing user's commands

user_command = main_prompt()
while user_command != 'quit':
    if user_command == 'main':
        user_command = main_prompt()
    if user_command == '1':
        user_command = input('Enter the keyword you would like to search:\n')
        if user_command == 'main':
            continue
        else:
            search_term = lemmatizer.lemmatize(user_command) # to counteract any weird user variations
            results = []
            for recipe in recipes_json:
                if search_term.lower() in recipe['recipe']['name'].lower() \
                        or user_command.lower() in recipe['recipe']['name'].lower():
                    results.append(recipe)
            print('Here are all the recipes with', user_command, 'in the title:')
            counter = 1
            for result in results:
                print(counter, result['recipe']['name'])
                counter += 1
            user_command = input('Choose a recipe to print:\n')
            if user_command == 'main':
                continue
            else:
                pprint.pprint(results[int(user_command)-1])
                user_command = output_recipe(results[int(user_command)-1])
    if user_command == '2':
        user_command = input('Enter the keyword you would like to search:\n')
        if user_command == 'main':
            continue
        else:
            search_term = lemmatizer.lemmatize(user_command)  # to counteract any weird user variations
            results = []
            for recipe in recipes_json:
                for ingredient in recipe['recipe']['ingredients']:
                    if search_term in ingredient['ingredientName'] or user_command in ingredient['ingredientName']:
                        results.append(recipe)
            print('Here are all the recipes with', user_command, 'in the ingredients:')
            counter = 1
            for result in results:
                print(counter, result['recipe']['name'])
                counter += 1
            user_command = input('Choose a recipe to print:')
            if user_command == 'main':
                continue
            else:
                pprint.pprint(results[int(user_command) - 1])
                user_command = output_recipe(results[int(user_command) - 1])
    if user_command == '3':
        categories = []
        for recipe in recipes_json:
            for category in recipe['recipe']['categories']:
                if category not in categories:
                    categories.append(category)
        print('Here are all the existing categories:')
        counter = 1
        for item in categories:
            print(counter, item)
            counter += 1
        user_command = input('Choose a category to see all the recipes:\n')
        chosen_category = categories[int(user_command)-1]
        results = []
        for recipe in recipes_json:
            if chosen_category in recipe['recipe']['categories']:
                results.append(recipe)
        print('Here are all the recipes in', chosen_category)
        counter = 1
        for result in results:
            print(counter, result['recipe']['name'])
            counter += 1
        user_command = input('Choose a recipe to print:')
        if user_command == 'main':
            continue
        else:
            pprint.pprint(results[int(user_command) - 1])
            user_command = output_recipe(results[int(user_command) - 1])
else:
    print('Goodbye.')