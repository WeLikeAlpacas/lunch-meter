# coding=utf-8

class Unit(object):

    def __init__(self, name, location, workers, recipes, menu):
        self.name = name
        self.location = location
        self.workers = workers
        self.recipes = recipes
        self.menu = menu

    def add_new_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes = [rcp for rcp in self.recipes if rcp.id != recipe.id]

    def change_menu(self, menu):
        self.menu = menu

