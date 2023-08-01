from lib.menu import Menu
from unittest.mock import Mock
import pytest

"""
Intially Menu list will be empty
"""
def test_menu_init():
    menu = Menu()
    assert menu.dish_list == [] 

"""
when I add dishes to the menu
list all returns a list of them all
with prices
"""
def test_list_dishes():
    menu = Menu()
    dish_1 = Mock()
    dish_2 = Mock()
    dish_3 = Mock()
    dish_1.format.return_value = 'Rice: £2.50'
    dish_2.format.return_value = 'Chips: £0.99'
    dish_3.format.return_value = 'Pasta: £1.20'
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    assert menu.list_all() == ['Rice: £2.50', 'Chips: £0.99', 'Pasta: £1.20']


"""
Add dishes to the menu
remove one 
list all will return the ones not removed
"""
def test_remove_dishes():
    menu = Menu()
    dish_1 = Mock()
    dish_2 = Mock()
    dish_3 = Mock()
    dish_1.format.return_value = 'Rice: £2.50'
    dish_2.format.return_value = 'Chips: £0.99'
    dish_3.format.return_value = 'Pasta: £1.20'
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    menu.remove(dish_2)
    assert menu.list_all() == ['Rice: £2.50', 'Pasta: £1.20']

"""
Add dishes to the menu
select returns the one selected
"""
def test_select_dish():
    menu = Menu()
    dish_1 = Mock()
    dish_2 = Mock()
    dish_3 = Mock()
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    assert menu.select(dish_1) == dish_1

"""
add dish 
then remove
select dish returns exception
"""

def test_select_exception():
    menu = Menu()
    dish_1 = Mock()
    menu.add(dish_1)
    menu.remove(dish_1)
    with pytest.raises(Exception) as error:
        menu.select(dish_1)
    assert str(error.value) == "We do not have this on the menu"