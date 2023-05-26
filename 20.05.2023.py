# Задание 1

class Shoe:
    def __init__(self, shoe_type, gender, shoe_style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.gender = gender
        self.shoe_style = shoe_style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

# Контроллер (Controller) - класс ShoeController
class ShoeController:
    def __init__(self):
        self.shoes = []

    def add_shoe(self, shoe):
        self.shoes.append(shoe)

    def remove_shoe(self, shoe):
        self.shoes.remove(shoe)

    def get_shoes(self):
        return self.shoes

# Представление (View) - функция display_shoes
def display_shoes(shoes):
    for shoe in shoes:
        print(f"{shoe.shoe_type} {shoe.gender} {shoe.shoe_style} ({shoe.color}) - {shoe.price} руб. ({shoe.manufacturer}), размер {shoe.size}")

# Пример использования паттерна MVC для класса Обувь
controller = ShoeController()

shoe1 = Shoe("Кроссовки", "Мужская", "Nike Air Max", "Черный", 7990, "Nike", 42)
shoe2 = Shoe("Туфли", "Женская", "Christian Louboutin", "Красный", 49990, "Christian Louboutin", 38)
shoe3 = Shoe("Сапоги", "Женская", "Dr. Martens", "Черный", 9990, "Dr. Martens", 39)

controller.add_shoe(shoe1)
controller.add_shoe(shoe2)
controller.add_shoe(shoe3)

shoes = controller.get_shoes()
display_shoes(shoes)

controller.remove_shoe(shoe2)

shoes = controller.get_shoes()
display_shoes(shoes)

# Задание 2

class Recipe:
    def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

# Контроллер (Controller) - класс RecipeController
class RecipeController:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def remove_recipe(self, recipe):
        self.recipes.remove(recipe)

    def get_recipes(self):
        return self.recipes

# Представление (View) - функция display_recipes
def display_recipes(recipes):
    for recipe in recipes:
        print(f"Название: {recipe.name}")
        print(f"Автор: {recipe.author}")
        print(f"Тип блюда: {recipe.recipe_type}")
        print(f"Описание: {recipe.description}")
        print(f"Ссылка на видео: {recipe.video_link}")
        print("Ингредиенты:")
        for ingredient in recipe.ingredients:
            print(f"- {ingredient}")
        print(f"Кухня: {recipe.cuisine}")
        print()

# Пример использования паттерна MVC для класса Рецепт
controller = RecipeController()

recipe1 = Recipe("Борщ", "Иванова Анна", "Первое блюдо", "Традиционный украинский суп", "https://www.youtube.com/watch?v=123456", ["свекла", "картошка", "капуста"], "Украинская")
recipe2 = Recipe("Паста карбонара", "Романо Марко", "Второе блюдо", "Итальянская паста с беконом и яйцом", "https://www.youtube.com/watch?v=789012", ["спагетти", "бекон", "сыр пармезан"], "Итальянская")
recipe3 = Recipe("Курица терияки", "Сато Хироши", "Второе блюдо", "Японский рецепт курицы в соусе терияки", "https://www.youtube.com/watch?v=345678", ["курица", "соевый соус", "мед"], "Японская")

controller.add_recipe(recipe1)
controller.add_recipe(recipe2)
controller.add_recipe(recipe3)

recipes = controller.get_recipes()
display_recipes(recipes)

controller.remove_recipe(recipe2)

recipes = controller.get_recipes()
display_recipes(recipes)