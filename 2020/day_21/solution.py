from collections import defaultdict
from functools import reduce


def read_data(path="input.data"):
    output = defaultdict(list)
    ingredients_list = []
    with open(path) as fobj:
        for line in map(str.rstrip, fobj):
            ingredients, alergens = line.rstrip(")").split(" (contains ")
            ingredients = ingredients.split()
            ingredients_list += ingredients
            for alergen in alergens.split(", "):
                output[alergen].append(ingredients)
    return output, ingredients_list


def allergens_to_ingredients(data):
    data = {
        allergen: reduce(set.intersection, map(set, ingredients))
        for allergen, ingredients in data.items()
    }
    data = sorted(data.items(), key=lambda t: -len(t[1]))
    result = {}
    while data:
        if len(data[-1][1]) == 1:
            allergen, ingredient = data.pop()
            data = sorted(
                [(a, i - ingredient) for a, i in data], key=lambda t: -len(t[1])
            )
            result[allergen] = ingredient.pop()
    return result


def solution_01(path="input.data"):
    data, ingredients_list = read_data(path)
    ingredients = set(allergens_to_ingredients(data).values())
    return sum(i not in ingredients for i in ingredients_list)


def solution_02(path="input.data"):
    data, _ = read_data(path)
    return ",".join(v for _, v in sorted(allergens_to_ingredients(data).items()))


if __name__ == "__main__":
    print("Solution 01:", solution_01())
    print("Solution 02:", solution_02())
