import unittest
from script_cake_factory import CakeFactory  # Adjust the import according to your project structure

class TestCakeFactory(unittest.TestCase):
    def test_create_cake(self):
        cake = CakeFactory("vanilla", "small")
        self.assertEqual(cake.cake_type, "vanilla")
        self.assertEqual(cake.size, "small")
        self.assertEqual(cake.price, 8)  # Vanilla cake, small size

    def test_add_topping(self):
        cake = CakeFactory("chocolate", "large")
        cake.add_topping("sprinkles")
        self.assertIn("sprinkles", cake.toppings)

    def test_check_ingredients(self):
        cake = CakeFactory("chocolate", "medium")
        cake.add_topping("cherries")
        ingredients = cake.check_ingredients()
        self.assertIn("cocoa", ingredients)
        self.assertIn("cherries", ingredients)
        self.assertNotIn("vanilla extract", ingredients)

    def test_check_price(self):
        cake = CakeFactory("vanilla", "large")
        cake.add_topping("sprinkles")
        cake.add_topping("cherries")
        price = cake.check_price()
        self.assertEqual(price, 14)  # Adjusted to match the expected price

# Running the unittests
if __name__ == "__main__":
    unittest.main()