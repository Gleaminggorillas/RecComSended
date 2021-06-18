import os
import json
import pandas as pd
from flask import Flask, render_template, json, url_for, abort, current_app as app


app = Flask(__name__)

# ======= Open "recipes.json" =========

with open("recipes.json", 'r') as recipe_json:
    recipes_list = json.load(recipe_json)

# ======= recipes_list keys into interpolated list for index.html links ======

recipe_links = list(recipes_list.keys())

# ====== take ingredients from recipes_list =========

ingredients_list = list(recipes_list.values())


print(ingredients_list)

@app.route("/")
def home():
    return render_template("index.html", recipe_links=recipe_links)

@app.route("/<str:recipe>")
def recipe(recipe):
    if recipe in recipe_links:
        return render_template('recipe.html', recipes_list=recipes_list)
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)

