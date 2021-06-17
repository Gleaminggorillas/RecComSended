import os
import json
import pandas as pd
from flask import Flask, render_template, json, current_app as app


app = Flask(__name__)

# ======= Open "recipes.json" =========

with open("recipes.json", 'r') as recipe_json:
    recipes_list = json.load(recipe_json)

# ======= recipes_list keys into interpolated list for index.html links ======

recipe_links = list(recipes_list.keys())

print(recipe_links)

@app.route("/")
def home():
    return render_template("index.html", recipe_links=recipe_links)

@app.route("/<recipe>")
def recipe():
    return render_template('index.html', recipe=recipe)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)

