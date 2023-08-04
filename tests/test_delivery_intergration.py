import pytest
from lib.menu import Menu
from lib.dish import Dish
from lib.order import Order
from lib.customer_info import CustomerInfo
from lib.order_formatter import OrderFormatter
from lib.order_confirmation import OrderConfirmation

"""
when I add dishes to the menu
list all returns a list of them all
"""
def test_add_dishes():
    menu = Menu()
    dish_1 = Dish('Chips', 0.99)
    dish_2 = Dish('Rice', 1.50)
    dish_3 = Dish('Pasta', 1.20)
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    assert menu.list_all() == ['Chips: £0.99', 'Rice: £1.50', 'Pasta: £1.20']


"""
Add dishes to the menu
remove one 
list all will return the ones not removed
"""
def test_remove_dish():
    menu = Menu()
    dish_1 = Dish('Chips', 0.99)
    dish_2 = Dish('Rice', 1.50)
    dish_3 = Dish('Pasta', 1.20)
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    menu.remove(dish_2)
    assert menu.list_all() == ['Chips: £0.99', 'Pasta: £1.20']

"""
Add dishes to the menu
select returns the one selected
"""
def test_select_dish():
    menu = Menu()
    dish_1 = Dish('Chips', 0.99)
    dish_2 = Dish('Rice', 1.50)
    dish_3 = Dish('Pasta', 1.20)
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    assert menu.select(dish_1) == dish_1


"""
select dishes for order
use list order
returns added dishes
"""
def test_list_order():
    menu = Menu()
    my_order = Order(menu)
    dish_1 = Dish('Chips', 0.99)
    dish_2 = Dish('Rice', 1.50)
    dish_3 = Dish('Pasta', 1.20)
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    my_order.select_dish(dish_1)
    my_order.select_dish(dish_2)
    assert my_order.list_order() == [dish_1, dish_2]


"""
create menu
select dishes for order
call total
returns cost of all dishes so far
"""
def test_order_total():
    menu = Menu()
    my_order = Order(menu)
    dish_1 = Dish('Chips', 0.99)
    dish_2 = Dish('Rice', 1.50)
    dish_3 = Dish('Pasta', 1.20)
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    my_order.select_dish(dish_2)
    my_order.select_dish(dish_1)
    assert my_order.order_total() == 2.49



"""
select dishes for order
add dishes
remove dish
use list order
returns order so far
"""
def test_remove_order_dish():
    menu = Menu()
    my_order = Order(menu)
    dish_1 = Dish('Chips', 0.99)
    dish_2 = Dish('Rice', 1.50)
    dish_3 = Dish('Pasta', 1.20)
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    my_order.select_dish(dish_2)
    my_order.select_dish(dish_1)
    my_order.remove_dish(dish_1)
    assert my_order.list_order() == [dish_2]

"""
selct same dish multiple times
Returns list with same dishes on it
"""


def test_select_same_dish_mutiple_times():
    menu = Menu()
    my_order = Order(menu)
    dish_1 = Dish('Chips', 0.99)
    dish_2 = Dish('Rice', 1.50)
    dish_3 = Dish('Pasta', 1.20)
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    my_order.select_dish(dish_1, 3)
    assert my_order.list_order() == [dish_1, dish_1, dish_1]


"""
Make order 
add items to order
return itemised reciept
"""

def test_select_get_reciept():
    menu = Menu()
    my_order = Order(menu)
    dish_1 = Dish('Chips', 0.99)
    dish_2 = Dish('Rice', 1.50)
    dish_3 = Dish('Pasta', 1.20)
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    my_order.select_dish(dish_1, 3)
    my_order.select_dish(dish_2, 4)
    my_order.select_dish(dish_3)
    assert my_order.get_order_reciept() == "Order: \nChips: £0.99 \nChips: £0.99 \nChips: £0.99 \nRice: £1.50 \nRice: £1.50 \nRice: £1.50 \nRice: £1.50 \nPasta: £1.20 \nTotal: £10.17 \n"



# """
# select dishes for order
# create customer order info
# make order
# """
def test_formater_get_order_info():
    menu = Menu()
    my_order = Order(menu)
    dish_1 = Dish('Chips', 0.99)
    dish_2 = Dish('Rice', 1.50)
    dish_3 = Dish('Pasta', 1.20)
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    my_order.select_dish(dish_2)
    my_order.select_dish(dish_1)
    my_order_confirmation = OrderConfirmation(my_order)
    my_order_confirmation.send_order_confirmation()
    my_order.make_order()
    assert my_order.complete == True
