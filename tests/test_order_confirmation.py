from lib.order_confirmation import *
from unittest.mock import Mock

"""
Check order confirmation init
returns instance of order_formatter
"""
# def test_order_formatter_in_confirmation():
#     my_order = Mock()
#     ord_confirm = OrderConfirmation(my_order)
#     assert ord_confirm == my_order

"""
Check order confirmation time has init correctly
returns instance of order_formatter
"""

def test_time_of_confirmation():
    my_order = Mock()
    ord_confirm = OrderConfirmation(my_order)
    assert ord_confirm.time == datetime.now().strftime('%H:%M:%S')

"""
Get Delivery info 
returns formatted string with infomation for customer
"""

def test_get_delivery_info():
    my_order = Mock()
    ord_confirm = OrderConfirmation(my_order)
    assert ord_confirm.get_customer_message() == f'Thank you! Your order was placed at {ord_confirm.time} and will be delivered before {(datetime.now() + timedelta(hours=1)).strftime("%H:%M:%S")}'


"""
Tes
t order confirmation is working
"""
