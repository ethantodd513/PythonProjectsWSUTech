import RefreshingPython
from RefreshingPython import MakeDrink, MakeOrder
import unittest

#Done By: Ethan Todd
#Done On: 04/23/2025
#Using: Youtube (for testing setup) and ChatGPT (for flavors test logic troubleshooting)

#WHAT IT DOES: It runs two different tests that have a different amount of flavors and makes sure they work

class Test_RefreshingPython(unittest.TestCase):
    #tests a drink with two flavors
    def test_drink_one(self):
        drink = MakeDrink("Sbrite")
        flavor1 = "Lemon"
        flavor2 = "Lime"
        size1 = "Small"

        drink.addFlavors(flavor1)
        drink.addFlavors(flavor2)
        drink.addSize(size1)

        #tests base, size, and flavors
        self.assertEqual(drink.getBase(), "Sbrite", "incorrect base")
        self.assertEqual(drink.getSize(), "Small", "incorrect size")
        self.assertListEqual(sorted(drink.getFlavors()), sorted(["Lemon", "Lime"]), "incorrect flavor(s)")

    #tests a drink with four flavors
    def test_drink_two(self):
        drink = MakeDrink("Water")
        flavor1 = "Strawberry"
        flavor2 = "Mint"
        flavor3 = "Blueberry"
        flavor4 = "Lime"

        drink.addFlavors(flavor1)
        drink.addFlavors(flavor2)
        drink.addFlavors(flavor3)
        drink.addFlavors(flavor4)

        #tests base and flavors
        self.assertEqual(drink.getBase(), "Water", "incorrect base")
        self.assertListEqual(sorted(drink.getFlavors()), sorted(["Strawberry", "Mint", "Blueberry", "Lime"]), "incorrect flavor(s)")

    #tests a drink and the total price, as well as making sure each price variable works
    def test_drink_three(self):
        drink = MakeDrink("Water")
        flavor1 = "Strawberry"
        flavor2 = "Mint"
        flavor3 = "Blueberry"
        flavor4 = "Lime"
        flavor5 = "Lemon"
        size1 = "Large"

        drink.addFlavors(flavor1)
        drink.addFlavors(flavor2)
        drink.addFlavors(flavor3)
        drink.addFlavors(flavor4)
        drink.addFlavors(flavor5)
        drink.addSize(size1)

        #tests drink size
        self.assertEqual(drink.getSize(), "Large", "Incorrect Size")

        order = MakeOrder()
        order.addItem(drink)
        price = drink.getPrice()
        tax = drink.getTax()

        #tests price and tax
        self.assertEqual(f"{tax:.2f}", "0.19")
        self.assertEqual(f"{price:.2f}", "2.84")


        
        
if __name__ == "__main__":
    unittest.main()