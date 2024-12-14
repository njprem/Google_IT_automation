import pytest

class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False  # Attribute to track if the fruit is cubed

    def cube(self):  # Renamed method to avoid conflict
        self.cubed = True  # Set cubed to True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl  # Store the fruits
        self._cube_fruit()  # Call the method to cube the fruits

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()  # Call the cube method to change the state


@pytest.fixture
def fruitbowl():
    return [Fruit("apple"), Fruit("banana")]  # Create a bowl of fruits


def test_Fruit_Salad(fruitbowl):
    # Act
    fruit_salad = FruitSalad(*fruitbowl)  # Create a FruitSalad instance

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)  # Verify all fruits are cubed