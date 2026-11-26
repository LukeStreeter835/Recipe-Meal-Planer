"""Utility functions for the Recipe & Meal Planner."""

import json


def load_config(filename):
    """Load application configuration from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def load_recipes(filename):
    """Load recipe data from a JSON file."""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)

def load_meal_plan(filename):
    """Load the users weekly meal plan from JSON file"""
    with open(filename, encoding="utf-8") as file:
        return json.load(file)

def search_by_name(recipes, search_term):
    """Return recipes whose names contain the search term."""
    search_term = search_term.lower()
    return [
        recipe
        for recipe in recipes
        if search_term in recipe["name"].lower()
    ]


def filter_by_category(recipes, category):
    """Return recipes that match the requested category."""
    category = category.lower()
    return [
        recipe
        for recipe in recipes
        if recipe["category"].lower() == category
    ]

def sort_by_time(recipes):
    """Returns a new list of the recipies with shortest cook/prep time being first"""
    time_sort_recipies = sorted(recipes, key=lambda recipe: recipe["prep_time"] + recipe["cook_time"])
    return time_sort_recipies
