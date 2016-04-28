# coding=utf-8
from collections import defaultdict


class Menu(object):

    def __init__(self):
        self.days = defaultdict(list)

    def add_recipe_for_a_day(self, recipe, day):
        self.days[day].append(recipe)

    def remove_recipe_for_a_day(self, recipe, day):
        self.days[date] = [rcp for rcp in self.days[day]
                           if rcp.id != recipe.id]
