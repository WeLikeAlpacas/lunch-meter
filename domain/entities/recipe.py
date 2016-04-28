# coding=utf-8
from domain.value_objets import RecipeIngredient


class Recipe(object):

    def __init__(self):
        self.ingredients = []

    def add_new_ingredient(self, ingredient_name, quantity):
        self.ingredients.append(RecipeIngredient(ingredient_name, quantity))

    def remove_ingredient(self, ingredient_name):
        self.ingredients = [ingredient for ingredient in self.ingredients
                            if ingredient.name != ingredient_name]
