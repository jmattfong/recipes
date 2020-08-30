import os
from recipe import Recipe, load_recipe_from_json

class RecipeIndex :

    def __init__(self, recipe_dir) :
        self.recipe_dir = recipe_dir
        self.recipe_cache = {}

    def list_recipes(self) :
        recipes = os.listdir(self.recipe_dir)
        print(f'There are {len(recipes)} recipes in the database')
        return recipes

    def load_recipe(self, recipe_name) -> Recipe :
        if recipe_name in self.recipe_cache :
            return self.recipe_cache[recipe_name]
        recipe = load_recipe_from_json(f'{self.recipe_dir}/{recipe_name}')
        self.recipe_cache[recipe_name] = recipe
        return recipe
