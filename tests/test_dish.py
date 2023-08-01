from lib.dish import Dish
from unittest.mock import Mock

"""
When intialised Dish will have two class variables
"""
def test_dish_init():
    dish = Dish("food", 2.00)
    assert dish.name == 'food'
    assert dish.price == 2.00

"""
Format returns dish like so {name}: £{price}
"""
def test_dish_format():
    dish = Dish("food", 2.00)
    assert dish.format() == 'food: £2.00'