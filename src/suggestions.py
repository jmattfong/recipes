from recipe_index import RecipeIndex

class SuggestionEngine :

    def __init__(self, index: RecipeIndex) :
        self.index = index

    def suggest_recipes(self, limit) :
        recipes = self.index.list_recipes()[:limit]
        print(f'suggesting {len(recipes)} recipes, limit was {limit}')
        return [self.index.load_recipe(recipe_name) for recipe_name in recipes]
