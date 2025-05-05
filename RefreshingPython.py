"""Made By: Ethan Todd
Done On: 5/5/2025
References/Help: Google searches (finding information), ChatGPT (finding information and fixing bugs),
peers/online personal help (finding information)

WHAT THE PROGRAM DOES -- adds bases and drinks to make an order
class MakeDrink sets the bases and flavors that can be used and creates the structure for a drink
class MakeOrder creates the order and applies the recieved input/data to the order"""

class MakeDrink:
    AVAILABLE_BASES = {"Water", "Sbrite", "Pokeacola", "Mr. Salt", "Hill Fog", "Leaf Wine"}
    AVAILABLE_FLAVORS = {"Lemon", "Cherry", "Strawberry", "Mint", "Blueberry", "Lime"}
    AVAILABLE_SIZES = {"Small", "Medium", "Large", "Mega"}
    AVAILABLE_FOODS = {"Hotdog", "Corndog", "Ice Cream", "Onion Rings", "French Fries", "Tater Tots", "Nacho Chips"}
    FOOD_PRICES = {
        "Hotdog": 2.30,
        "Corndog": 2.00,
        "Ice Cream": 3.00,
        "Onion Rings": 1.75,
        "French Fries": 1.50,
        "Tater Tots": 1.70,
        "Nacho Chips": 1.90
    }
    FOOD_TOPPINGS = {
        "Cherry": 0.00,
        "Whipped Cream": 0.00,
        "Caramel Sauce": 0.50,
        "Chocolate Sauce": 0.50,
        "Nacho Cheese": 0.30,
        "Chili": 0.60,
        "Bacon Bits": 0.30,
        "Ketchup": 0.00,
        "Mustard": 0.00
    }
    SIZE_PRICES = {
        "Small": 1.50,
        "Medium": 1.75,
        "Large": 2.05,
        "Mega": 2.15
    }
    ADDITIONAL_PRICE_PER_FLAVOR = 0.15
    TAX_RATE = 7.25

    def __init__(self, base=None, size=None):
        self._base = None
        self._flavors = set()
        self._food = set()
        self._toppings = set()
        self._size = None

        if base:
            self._base = base

        if size:
            self._size = size

    def getBase(self):
        return self._base
    
    def getFlavors(self):
        return list(self._flavors)
    
    def getToppings(self):
        return list(self._toppings)
    
    def getFood(self):
        return list(self._food)
    
    def getNumOfFlavors(self):
        return len(self._flavors)
    
    def getNumOfToppings(self):
        return len(self._toppings)
    
    def getNumOfFood(self):
        return len(self._food)
    
    def getSize(self):
        return self._size
    
    def getPrice(self):
        base_price = self.SIZE_PRICES.get(self._size, 0)
        food_cost = sum(self.FOOD_PRICES.get(food, 0) for food in self._food)
        toppings_cost = sum(self.FOOD_TOPPINGS.get(topping, 0) for topping in self._toppings)
        additional_flavor_cost = max((len(self._flavors) - 1), 0) * self.ADDITIONAL_PRICE_PER_FLAVOR
        tax = (base_price + additional_flavor_cost + food_cost + toppings_cost) * (self.TAX_RATE / 100)
        total = base_price + additional_flavor_cost + food_cost + toppings_cost + tax
        return total

    def getTax(self):
        base_price = self.SIZE_PRICES.get(self._size, 0)
        food_cost = sum(self.FOOD_PRICES.get(food, 0) for food in self._food)
        toppings_cost = sum(self.FOOD_TOPPINGS.get(topping, 0) for topping in self._toppings)
        additional_flavor_cost = max((len(self._flavors) - 1), 0) * self.ADDITIONAL_PRICE_PER_FLAVOR
        tax = (base_price + additional_flavor_cost + food_cost + toppings_cost) * (self.TAX_RATE / 100)
        return tax
    
    def setBase(self, base):
        if base not in MakeDrink.AVAILABLE_BASES:
            raise ValueError(f"{base} is not a correct option")
        self._base = base

    def setFlavors(self, flavors):
        if flavors not in MakeDrink.AVAILABLE_FLAVORS:
            raise ValueError(f"{flavors} is not a correct option(s)")
        
    def setFood(self, food):
        if food not in MakeDrink.AVAILABLE_FOODS:
            raise ValueError(f"{food} is not a correct option")
        self._food.add(food)
    
    def setToppings(self, toppings):
        if toppings not in MakeDrink.FOOD_TOPPINGS:
            raise ValueError(f"{toppings} is not a correct option")
        self._toppings.add(toppings)
        
    def setSize(self, size):
        if size not in MakeDrink.AVAILABLE_SIZES:
            raise ValueError(f"{size} is not a correct size")
        self._size = size
        
    def addFlavors(self, flavor):
        if flavor in MakeDrink.AVAILABLE_FLAVORS:
            self._flavors.add(flavor)

    def addSize(self, size):
        if size in MakeDrink.AVAILABLE_SIZES:
            self._size = size
    
    def addFood(self, food):
        food = food.strip().title()
        if food in MakeDrink.AVAILABLE_FOODS:
            self._food.add(food)

    def addToppings(self, topping):
        topping = topping.strip().title()
        if topping in MakeDrink.FOOD_TOPPINGS:
            self._toppings.add(topping)

class MakeOrder:
    def __init__(self):
        self._drinks = []

    def getDrinks(self):
        return self._drinks
    
    def getNumOfItems(self):
        return len(self._drinks)
    
    def addItem(self, drink):
        if isinstance(drink, MakeDrink):
            self._drinks.append(drink)

    def removeItem(self, index):
        if 0 <= index < len(self._drinks):
            self._drinks.pop()
    
    def get_total(self):
        total = []

        for i, drink in enumerate(self._drinks):
            base = drink.getBase() or "Invalid Base"
            flavors = ", ".join(drink.getFlavors()) if drink.getNumOfFlavors() > 0 else "None"
            size = drink.getSize() or "Invalid Size"
            food = ", ".join(drink.getFood()) if drink.getNumOfFood() > 0 else "None"
            toppings = ", ".join(drink.getToppings()) if drink.getNumOfToppings() > 0 else "None"
            price = drink.getPrice()
            tax = drink.getTax()

            """used to test the order"""
            total.append(f"Drink: {i + 1} | Base: {base}\nFlavor(s): {flavors}\nSize: {size}\nFood: {food}\nTopping(s): {toppings}\nTax: {tax:.2f}\nTotal: {price:.2f}\n--------")
        return "\n".join(total)

"""test function (lacks front-end so this has to do)"""
if __name__ == "__main__":
    drink1 = MakeDrink("Water")
    flavor1_1 = "Strawberry"
    flavor1_2 = "Mint"
    flavor1_3 = "Blueberry"
    flavor1_4 = "Lime"
    flavor1_5 = "Lemon"
    size1 = "Large"
    food_1 = "Hotdog"
    topping_1 = "Mustard"
    topping_2 = "Ketchup"

    drink2 = MakeDrink("Sbrite")
    flavor2_1 = "Lime"
    flavor2_2 = "Blueberry"
    size2 = "Mega"

    drink1.addFlavors(flavor1_1)
    drink1.addFlavors(flavor1_2)
    drink1.addFlavors(flavor1_3)
    drink1.addFlavors(flavor1_4)
    drink1.addFlavors(flavor1_5)
    drink1.addSize(size1)
    drink1.addFood(food_1)
    drink1.addToppings(topping_1)

    drink2.addFlavors(flavor2_1)
    drink2.addFlavors(flavor2_2)
    drink2.addSize(size2)

    order = MakeOrder()
    order.addItem(drink1)
    order.addItem(drink2)

    print(order.get_total())