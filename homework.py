def recipe_book(file):
  cook_book = {}
  with open("list.txt", encoding="utf-8") as file:
    for line in file:
      name_of_dishes = line.strip()
      ingredients_count = int(file.readline().strip())
      ingredients_list = []
      for item in range(int(ingredients_count)):
        ingredient = {}
        emp = file.readline().strip().split(" | ")
        ingredient['ingredient_name'] = emp[0]
        ingredient['quantity'] = int(emp[1])
        ingredient['measure'] = emp[2]
        ingredients_list.append(ingredient)
      cook_book[name_of_dishes]= ingredients_list
      file.readline()
  return cook_book     
   


def get_shop_list_by_dishes(dishes, person_count, book):
  recipe_of_the_dish = {}
  for dish in dishes:
    if dish not in book.keys():
      print("В кулинарной книге нет рецепта для такого блюда")
    for ingredient in book[dish]:
      if ingredient['ingredient_name'] not in recipe_of_the_dish.keys():
        new_item = ingredient['ingredient_name']
        new_item_value = {}
        new_item_value["measure"] = ingredient["measure"]
        new_item_value["quantity"] = ingredient["quantity"] * person_count
        recipe_of_the_dish[new_item] = new_item_value
      else:
       recipe_of_the_dish[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
  return recipe_of_the_dish    

     
        
print(recipe_book("list.txt"))
print(get_shop_list_by_dishes(["Омлет","Запеченный картофель"],2 , recipe_book("list.txt")))
