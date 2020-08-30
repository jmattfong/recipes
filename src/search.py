from recipe_index import RecipeIndex
from recipe import Recipe

class SearchEngine :

    def __init__(self, index: RecipeIndex) :
        self.index = index
        self.all_recipes = [index.load_recipe(recipe) for recipe in index.list_recipes()]

    def search(self, query, limit) :
        result = []
        for recipe in self.all_recipes :
            if self.recipe_matches_query(query, recipe) :
                result.append(recipe)
            if len(result) == limit :
                return result

        return result

    def recipe_matches_query(self, query, recipe) :
        return query in recipe.get_title()