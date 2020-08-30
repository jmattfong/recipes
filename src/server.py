#!/usr/bin/env python3

import os
from flask import Flask, request, send_from_directory, jsonify
from recipe import Recipe, load_recipe_from_json
from pathlib import Path
from recipe_index import RecipeIndex
from search import SearchEngine
from suggestions import SuggestionEngine
import traceback

app = Flask(__name__, static_url_path=None)

# TODO How can we make constants configurable?
REACT_BUILD_DIR = 'react-js/build'
DEFAULT_IMAGE_DIR = f'{str(Path.home())}/data/recipe-data/images'
DEFAULT_CONFIG_DIR = f'{str(Path.home())}/data/recipe-data/config'

INDEX = RecipeIndex(DEFAULT_CONFIG_DIR)
SEARCHER = SearchEngine(INDEX)
SUGGESTER = SuggestionEngine(INDEX)

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(REACT_BUILD_DIR, path)

@app.route('/recipe/<id>')
def render_recipe(id):
    return send_from_directory(REACT_BUILD_DIR, 'index.html')

@app.route('/images/<image_name>')
def get_image(image_name):
    return send_from_directory(DEFAULT_IMAGE_DIR, image_name)

@app.route('/api/recipe/<id>')
def get_recipe(id):
    recipe = load_recipe_from_json(f'{DEFAULT_CONFIG_DIR}/{id}.json')

    return recipe.as_json()

@app.route('/api/recipe')
def list_recipes() :
    # Possible request query parameters
    requestedLimit = request.args.get('limit')
    query = request.args.get('q')

    limit = 3 if requestedLimit is None else int(requestedLimit)

    if query is None :
        recipes = list_suggested_recipes(limit)
    else :
        recipes = search_recipes(query, limit)

    return recipes

def list_suggested_recipes(limit) :
    print(f'Suggesting recipes...')
    return list_recipes_with_guacamole(lambda: SUGGESTER.suggest_recipes(limit), limit)

def search_recipes(query, limit) :
    print(f'Searching recipes...')
    return list_recipes_with_guacamole(lambda: SEARCHER.search(query, limit), limit)

def list_recipes_with_guacamole(function, limit) :
    recipes = []
    try :
        recipes = function()
    except :
        print('An error occurred searching recipes')
        traceback.print_exc()
        recipes = serve_guacamole(limit)

    short_form_recipes = [recipe.short_form_json() for recipe in recipes]

    print(f'Returning {len(recipes)} recipes: {short_form_recipes}')

    return jsonify({
        "count": len(recipes),
        "recipes": short_form_recipes
    })

# Debugging is better with guacamole
def serve_guacamole(count) :
    """
    When in doubt, serve guacamole to the max!
    """
    guac_recipe = load_recipe_from_json(f'recipes/guacamole.json')
    return [guac_recipe] * count

def main() :
    # Flask automatically sends static files from ./static, but we override to keep all static files with the React app
    app.static_url_path = f'{REACT_BUILD_DIR}/static/'
    app.static_folder = f'{app.root_path}/{app.static_url_path}'

    print(f"Serving React's build artifacts from path: {app.root_path}/{REACT_BUILD_DIR}")

    # Remove this for only local access when running debug server
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
