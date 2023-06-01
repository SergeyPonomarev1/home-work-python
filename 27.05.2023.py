class Pizza:
    def __init__(self, name, toppings=None):
        self.name = name
        self.toppings = toppings or []

    def __str__(self):
        return f"{self.name} with {', '.join(self.toppings)}"

class Order:
    def __init__(self, pizzas=None):
        self.pizzas = pizzas or []
        self.total = 0

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.total += self.calculate_price(pizza)

    def calculate_price(self, pizza):
        # Calculate price based on pizza and toppings
        return 10 + len(pizza.toppings)

class Payment:
    def __init__(self, amount=0, method="cash"):
        self.amount = amount
        self.method = method

class Sales:
    def __init__(self, orders=None):
        self.orders = orders or []

    def add_order(self, order):
        self.orders.append(order)

    def get_total_sales(self):
        return sum([order.total for order in self.orders])

    def get_profit(self):
        return sum([order.total - 10 for order in self.orders]) # Assuming cost of ingredients is $10

class PizzaMenu:
    def __init__(self):
        self.pizzas = [
            Pizza("Margherita"),
            Pizza("Pepperoni", ["olives", "mushrooms"]),
            Pizza("Hawaiian", ["pineapple", "ham"]),
            Pizza("Meat Lover's", ["sausage", "bacon", "ham"]),
            Pizza("Veggie", ["mushrooms", "onions", "peppers"])
        ]

    def add_pizza(self, pizza):
        self.pizzas.append(pizza)

    def create_pizza(self):
        name = input("Enter pizza name: ")
        toppings = input("Enter toppings (comma separated): ").split(",")
        return Pizza(name, toppings)

    def display_menu(self):
        print("Pizza Menu:")
        for i, pizza in enumerate(self.pizzas):
            print(f"{i+1}. {pizza}")

class PizzaToppings:
    def __init__(self):
        self.toppings = ["sweet onion", "jalapeno", "chili", "pickle", "olives", "prosciutto"]

    def add_topping(self, topping):
        self.toppings.append(topping)

    def display_toppings(self):
        print("Toppings:")
        for i, topping in enumerate(self.toppings):
            print(f"{i+1}. {topping}")

class PizzaOrder:
    def __init__(self, menu, toppings):
        self.menu = menu
        self.toppings = toppings
        self.order = Order()
        self.sales = Sales()

    def place_order(self):
        while True:
            self.menu.display_menu()
            choice = input("Enter pizza number or 'c' to create a custom pizza: ")
            if choice == 'c':
                pizza = self.menu.create_pizza()
            else:
                try:
                    pizza = self.menu.pizzas[int(choice)-1]
                except:
                    print("Invalid choice. Please try again.")
                    continue

            while True:
                self.toppings.display_toppings()
                topping_choice = input("Enter topping number or 'd' to finish pizza: ")
                if topping_choice == 'd':
                    break
                try:
                    topping = self.toppings.toppings[int(topping_choice)-1]
                    pizza.toppings.append(topping)
                except:
                    print("Invalid choice. Please try again.")

            self.order.add_pizza(pizza)
            print(f"Added {pizza} to order.")
            if input("Add another pizza? (y/n): ").lower() != 'y':
                break

        print(f"Total price: ${self.order.total}")
        payment_method = input("Enter payment method ('cash' or 'card'): ")
        payment_amount = float(input("Enter payment amount: "))
        payment = Payment(payment_amount, payment_method)
        self.sales.add_order(self.order)
        print("Order placed.")

    def view_sales(self):
        print(f"Total sales: ${self.sales.get_total_sales()}")
        print(f"Total profit: ${self.sales.get_profit()}")

menu = PizzaMenu()
toppings = PizzaToppings()
order = PizzaOrder(menu, toppings)
order.place_order()
order.view_sales()