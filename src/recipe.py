import json

class Recipe :

    def __init__(self, config_map: dict) :
        self.config = config_map
        self.time = parse_time(config_map["time"])
        self.ingredients = parse_ingredients(config_map["ingredients"])

    def short_form_json(self) :
        return {
            "recipe_id": self.config["recipe_id"],
            "title": self.config["title"],
            "subtitle": self.config["subtitle"],
            "description": self.config["description"],
            "servings": self.config["servings"],
            "time": self.time,
            "image_url": self.config["image_url"],
            "publisher": self.config["publisher"],
            "publisher_url": self.config["publisher_url"],
            "source_url": self.config["source_url"],
        }

    def as_json(self) :
        return self.config

    def get_id(self) -> str :
        return self.config["recipe_id"]

    def get_title(self) -> str :
        return self.config["title"]

    def get_subtitle(self) -> str :
        return self.config["title"]

    def get_description(self) -> str :
        return self.config["title"]

    def get_ingredients(self) -> dict :
        return self.config["ingredients"]

    def get_notes(self) -> list :
        return self.config["notes"]

    def get_steps(self) -> list :
        return self.config["steps"]

    def get_collapsed_steps(self) -> list :
        steps = []
        for step in self.get_steps() :
            steps.append(step["step"])
            nested_steps = step["steps"]
            if nested_steps is not None :
                for step in nested_steps :
                    steps.append("step")
        return steps

    def get_text_by_importance(self) :
        text = [
            self.get_title(),
            self.get_subtitle(),
            self.get_description(),
        ]
        text += self.get_ingredients().keys()
        text += self.get_collapsed_steps()
        text += self.get_notes()

def parse_time(time) :
    # TODO parse this into a duration, it'll be something like "1 hour" or "25-35 mins"
    return time

def parse_ingredients(ingredients) :
    # TODO parse the amounts, so we can compare them. "1 oz", "2", "1 Tbsp", etc.
    return ingredients

def load_recipe_from_json(path) :
    f = open(path, "r")
    return Recipe(json.loads(f.read()))
