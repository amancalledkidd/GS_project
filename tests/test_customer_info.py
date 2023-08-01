from lib.customer_info import CustomerInfo

"""
create instance customer info
test format
returns formatted name, address, number
"""
def test_customer_format():
    my_info = CustomerInfo('Kumani', '123 Road', '07946464836')
    assert my_info.format() == "Name: Kumani \nAddress: 123 Road \nPhone Number: 07946464836"

"""
create instance of customer info
check get number returns phone number
"""
def test_get_number():
    my_info = CustomerInfo('Kumani', '123 Road', '07946464836')
    assert my_info.get_number() == '07946464836'
