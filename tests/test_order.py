from lib.order import Order
from unittest.mock import Mock


"""
order intialises with empty note and list
"""
def test_list_order():
    menu = Mock()
    my_order = Order(menu)
    assert my_order.list_order() == []


"""
add note to order
"""
def test_add_note():
    menu = Mock()
    my_order = Order(menu)
    my_order.add_note('Extra chips please')
    assert my_order.note == 'Extra chips please'


"""
select dishes for order
use list order
returns added dishes
"""
# my_order = Order()
# menu = Mock()
# dish_1 = Mock()
# dish_2 = Mock()
# dish_3 = Mock()
# menu.menu_list.return_value = [dish_1, dish_2, dish_3]
# my_order.select_dish(dish_2)
# my_order.select_dish(dish_1)
# my_order.list_order # => [dish_2, dish_1]
