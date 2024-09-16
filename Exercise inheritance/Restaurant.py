class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

class Beverage(Product):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self._milliliters = milliliters

    @property
    def milliliters(self):
        return self._milliliters

class Food(Product):
    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self._grams = grams

    @property
    def grams(self):
        return self._grams

class HotBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)

class ColdBeverage(Beverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)

class Coffee(HotBeverage):
    MILLILITERS = 50
    PRICE = 3.50
    CAFFEINE = 0.0

    def __init__(self, name, caffeine):
        super().__init__(name, self.PRICE, self.MILLILITERS)
        self._caffeine = caffeine

    @property
    def caffeine(self):
        return self._caffeine

class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)

class MainDish(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)

class Dessert(Food):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        self._calories = calories

    @property
    def calories(self):
        return self._calories

class Starter(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)

class Salmon(MainDish):
    GRAMS = 22
    PRICE = 15.0

    def __init__(self, name):
        super().__init__(name, self.PRICE, self.GRAMS)

class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5.0

    def __init__(self, name):
        super().__init__(name, self.PRICE, self.GRAMS, self.CALORIES)

class Soup(Starter):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)

product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)