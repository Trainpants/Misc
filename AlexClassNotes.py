import pprint

class Pizza:
    size = "Large"
    toppings = ["cheese", "sauce"]

    def __init__(self, size=None, toppings=None):
        if size:
            self.size = size

        if toppings:
            self.toppings += toppings

    def __repr__(self):
        return f"Pizza: size {self.size} toppings {self.toppings}"

    def baking_time(self):
        pass

my_first_pizza = Pizza()
print(my_first_pizza)