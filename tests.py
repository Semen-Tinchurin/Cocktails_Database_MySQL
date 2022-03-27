import json

with open('new_cocktails_dict.json', 'r', encoding='utf-8') as file:
    file = file.read()
    file = json.loads(file)

dictionary = {}

for valuess in file.values():
    ingredients = str(valuess[0]).replace("['", "").replace("']", "").replace("', '", ", ")
    recipe = str(valuess[2]).replace("['", "").replace("']", "").replace("', '", ", ")
    dictionary[ingredients] = [str(recipe)]

with open('recipe_and_ingredients.json', 'w', encoding='utf-8') as save_file:
    json.dump(dictionary, save_file, indent=4, ensure_ascii=False)
