import json

class Recipe :

    def __init__(self, json_config) :
        self.json_config = json_config
        self.time = parse_time(json_config["time"])
        self.ingredients = parse_ingredients(json_config["ingredients"])

    def short_form_json(self) :
        return {
            "recipe_id": self.json_config["recipe_id"],
            "title": self.json_config["title"],
            "subtitle": self.json_config["subtitle"],
            "description": self.json_config["description"],
            "servings": self.json_config["servings"],
            "time": self.time,
            "image_url": self.json_config["image_url"],
            "publisher": self.json_config["publisher"],
            "publisher_url": self.json_config["publisher_url"],
            "source_url": self.json_config["source_url"],
        }

    def as_json(self) :
        return self.json_config

def parse_time(time) :
    # TODO parse this into a duration, it'll be something like "1 hour" or "25-35 mins"
    return time

def parse_ingredients(ingredients) :
    # TODO parse the amounts, so we can compare them. "1 oz", "2", "1 Tbsp", etc.
    return ingredients

def load_recipe_from_json(path) :
    f = open(path, "r")
    return Recipe(json.loads(f.read()))
