#!/usr/bin/env python3

import os
from flask import Flask, request, send_from_directory, jsonify
from recipe import Recipe, load_recipe_from_json

app = Flask(__name__, static_url_path=None)

REACT_BUILD_DIR = 'react-js/build'

@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def catch_all(path):
    return send_from_directory(REACT_BUILD_DIR, path)

@app.route('/recipe/<id>')
def render_recipe(id):
    return send_from_directory(REACT_BUILD_DIR, 'index.html')

@app.route('/api/recipe/<id>')
def get_recipe(id):
    recipe = load_recipe_from_json(f'recipes/{id}.json')
    return recipe.as_json()

@app.route('/api/recipe')
def list_recipes() :
    # Possible request query parameters
    requestedLimit = request.args.get('limit')
    query = request.args.get('q')

    limit = 3 if requestedLimit is None else int(requestedLimit)

    if query is None :
        return list_suggested_recipes(limit)
    else :
        return search_recipes(query, limit)

def list_suggested_recipes(limit) :
    guac_recipe = load_recipe_from_json(f'recipes/guacamole.json')
    return jsonify({
        "count": limit,
        "recipes": [guac_recipe.short_form_json()] * limit
    })

def search_recipes(query, limit) :
    return list_suggested_recipes(limit)

def main() :
    # Flask automatically sends static files from ./static, but we override to keep all static files with the React app
    app.static_url_path = f'{REACT_BUILD_DIR}/static/'
    app.static_folder = f'{app.root_path}/{app.static_url_path}'

    print(f"Serving React's build artifacts from path: {app.root_path}/{REACT_BUILD_DIR}")

    # Remove this for only local access when running debug server
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
