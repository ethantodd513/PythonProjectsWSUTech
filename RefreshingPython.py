"""Made By: Ethan Todd
Done On: 4/28/2025
References/Help: Google searches (finding information), ChatGPT (finding information and fixing bugs),
peers/online personal help (finding information)

WHAT THE PROGRAM DOES -- adds bases and drinks to make an order
class MakeDrink sets the bases and flavors that can be used and creates the structure for a drink
class MakeOrder creates the order and applies the recieved input/data to the order"""

class MakeDrink:
    AVAILABLE_BASES = {"Water", "Sbrite", "Pokeacola", "Mr. Salt", "Hill Fog", "Leaf Wine"}
    AVAILABLE_FLAVORS = {"Lemon", "Cherry", "Strawberry", "Mint", "Blueberry", "Lime"}
    AVAILABLE_SIZES = {"Small", "Medium", "Large", "Mega"}
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
        self._size = None

        if base:
            self._base = base

        if size:
            self._size = size

    def getBase(self):
        return self._base
    
    def getFlavors(self):
        return list(self._flavors)
    
    def getNumOfFlavors(self):
        return len(self._flavors)
    
    def getSize(self):
        return self._size
    
    def getPrice(self):
        base_price = self.SIZE_PRICES.get(self._size, 0)
        additional_flavor_cost = max((len(self._flavors) - 1), 0) * self.ADDITIONAL_PRICE_PER_FLAVOR
        tax = (base_price + additional_flavor_cost) * (self.TAX_RATE / 100)
        total = base_price + additional_flavor_cost + tax
        return total

    def getTax(self):
        base_price = self.SIZE_PRICES.get(self._size, 0)
        additional_flavor_cost = max((len(self._flavors) - 1), 0) * self.ADDITIONAL_PRICE_PER_FLAVOR
        tax = (base_price + additional_flavor_cost) * (self.TAX_RATE / 100)
        return tax
    
    def setBase(self, base):
        if base not in MakeDrink.AVAILABLE_BASES:
            raise ValueError(f"{base} is not a correct option")
        self._base = base

    def setFlavors(self, flavors):
        if flavors not in MakeDrink.AVAILABLE_FLAVORS:
            raise ValueError(f"{flavors} is not a correct option(s)")
        
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
            flavors = ", ".join(drink.getFlavors()) or "Invalid Flavor(s)"
            size = drink.getSize() or "Invalid Size"
            price = drink.getPrice()
            tax = drink.getTax()

            """used to test the order"""
            total.append(f"Drink: {i + 1} | Base: {base}\nFlavor(s): {flavors}\nSize: {size}\nTax: {tax:.2f}\nTotal: {price:.2f}\n--------")
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

    drink2.addFlavors(flavor2_1)
    drink2.addFlavors(flavor2_2)
    drink2.addSize(size2)

    order = MakeOrder()
    order.addItem(drink1)
    order.addItem(drink2)

    print(order.get_total())