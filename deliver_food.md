# Deliver_food Design Recipe

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

Use the twilio-python package to implement this next one. You will need to use mocks too.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.


## 2. Design the Class System

```python

# Have makeorder call order confirmation
# Add quantity option to add
# Possibly oreder list , Itemise???
# Time api for order confirmation

# Nouns
Dishes
Prices
Meal
Itemized reciept
Total
Time
Text

# Verbs
Order
Select
Verify
Reassured
Recieve
See List
Add

                                                            ┌────────────────────┐
                                                            │                    │
                                                  ┌─────────►       Order        │
                                                  │         │   Confirmation     │
 ┌────────────────────┐       ┌───────────────────┴┐        │                    │
 │                    │       │                    │        │                    │
 │                    │       │                    │        └────────────────────┘
 │       Menu        ◄├───────┼─      Order        │
 │                    │       │                    │
 │         │          │       │         │          │        ┌────────────────────┐
 └─────────┼──────────┘       └─────────┼──────────┴────────┤►                   │
           │                            │                   │       Order        │
 ┌─────────┴──────────┐       ┌─────────┴──────────┐        │     Formatter      │
 │         ▼          │       │         ▼          │        │                    │
 │                    │       │                    │        │                    │
 │        Dish        │       │      Customer      │        └────────────────────┘
 │                    │       │       Info         │
 │                    │       │                    │
 └────────────────────┘       └────────────────────┘


class Menu():
    # Stores dishes in list
    def __init__(self):
        pass

    def list_all(self):
        # returns menu
        pass

    def add(self, dish):
        # dish: instance of Dish class
        # Side effect: adds dish to list
        # returns nothing
        pass

    def remove(self, dish):
        # dish: instance of Dish class
        # Side effect: removes dish from list
        # returns nothing
        pass

    def select(self, dish):
        # dish: instance of Dish class
        # returns selected dish
        # raise error for incorrect dish
        pass

class Dish():
    def __init__(self, name, price):
        # Name: is a string representing name of dish
        # Price: a float represent cost of dish in pounds (£)
        pass

    def format(self):
        # returns formatted string of name and price of dish
        pass


class Order():
    # A list of dishes to be ordered
    # Black space possible for note
    def __init__(self):
        pass

    def list_order(self):
        # returns a list of order

    def select_dish(self, dish):
        # dish: an instance of Dish Class
        # Side affect: Adds dish to order list
        # returns nothing
        pass

    def remove_dish(self, dish):
        # dish: an instance of Dish Class
        # Side affect: removes dish from order list
        # returns nothing
        pass

    def order_total(self):
        # returns total order cost so far
        pass

    def add_note(self, note):
        # Note: a string representing a message for service
        # adds note on the order
        pass


    def make_order(self, customer_info):
        # Side effects: 
        #   Calls order formatter
        #   calls order confirmation
        pass




class CustomerInfo():
    def __init__(self, name, address, number):
        #name: string for customers name
        #address: string representing address
        #number: 11 digit string representing customers phone numbers
        pass

    def format(self):
        # returns formatted name, address and number  
        pass

    def get_number(self):
        # returns number
        pass


class OrderFormatter():
    def get_order_info(self, order):
        # Returns order info in formatted layout includes note, total, order list, customer
        pass

    def make_receipt(self):
        # returns receipt to customer
        pass


class OrderConfirmation():
    def __init__(self, requester, order):
        # requester: a varaible to store requests from twillo
        pass

    def get_order_info(self):
        # Gets order info
        pass

    def send_order_confirmation(self):
        # Side effect: Uses API to send text message to customer 
        pass


```

_Also design the interface of each class in more detail._


## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
"""
when I add dishes to the menu
list all returns a list of them all
"""

menu = Menu()
dish_1 = Dish('Chips', 0.99)
dish_2 = Dish('Rice', 1.50)
dish_3 = Dish('Pasta' 1.20)
menu.add(dish_1)
menu.add(dish_2)
menu.add(dish_3)
menu.list_all() # => [dish_1, dish_2, dish_3]


"""
Add dishes to the menu
remove one 
list all will return the ones not removed
"""
menu = Menu()
dish_1 = Dish('Chips', 0.99)
dish_2 = Dish('Rice', 1.50)
dish_3 = Dish('Pasta' 1.20)
menu.add(dish_1)
menu.add(dish_2)
menu.add(dish_3)
menu.remove(dish_2)
menu.list_all() # => [dish_1, dish_3]

"""
Add dishes to the menu
select returns the one selected
"""

menu = Menu()
dish_1 = Dish('Chips', 0.99)
dish_2 = Dish('Rice', 1.50)
dish_3 = Dish('Pasta' 1.20)
menu.add(dish_1)
menu.add(dish_2)
menu.add(dish_3)
menu.list_select(dish_1) # => dish_1

"""
select dishes for order
use list order
returns added dishes
"""
my_order = Order()
menu = Menu()
dish_1 = Dish('Chips', 0.99)
dish_2 = Dish('Rice', 1.50)
dish_3 = Dish('Pasta' 1.20)
menu.add(dish_1)
menu.add(dish_2)
menu.add(dish_3)
my_order.select_dish(dish_2)
my_order.select_dish(dish_1)
my_order.list_order # => [dish_2, dish_1]


"""
create menu
select dishes for order
call total
returns cost of all dishes so far
"""

my_order = Order()
menu = Menu()
dish_1 = Dish('Chips', 0.99)
dish_2 = Dish('Rice', 1.50)
dish_3 = Dish('Pasta' 1.20)
menu.add(dish_1)
menu.add(dish_2)
menu.add(dish_3)
my_order.select_dish(dish_2)
my_order.select_dish(dish_1)
my_order.total() # => 2.49




"""
select dishes for order
add dishes
remove dish
use list order
returns order so far
"""

my_order = Order()
menu = Menu()
dish_1 = Dish('Chips', 0.99)
dish_2 = Dish('Rice', 1.50)
dish_3 = Dish('Pasta' 1.20)
menu.add(dish_1)
menu.add(dish_2)
menu.add(dish_3)
my_order.select_dish(dish_2)
my_order.select_dish(dish_1)
my_order.remove_dish(dish_1)
my_order.list_order # => [dish_2, dish_1]

"""
select dishes for order
create customer order info
make order
"""

my_order = Order()
menu = Menu()
dish_1 = Dish('Chips', 0.99)
dish_2 = Dish('Rice', 1.50)
dish_3 = Dish('Pasta' 1.20)
menu.add(dish_1)
menu.add(dish_2)
menu.add(dish_3)
my_order.select_dish(dish_2)
my_order.select_dish(dish_1)
my_info = CustomerInfo('Kumani', "123 road", '07946464836')
formatter = OrderFormatter(my_order)
order_confirm = OrderConfirmation(my_order)
my_order.make_order(my_info) # => receipt with total

"""

"""



```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
"""
Intially Menu list will be empty
"""
menu = Menu()
menu.menu_list => [] 

"""
when I add dishes to the menu
list all returns a list of them all
"""

menu = Menu()
dish_1 = Mock()
dish_2 = Mock()
dish_3 = Mock()
menu.add(dish_1)
menu.add(dish_2)
menu.add(dish_3)
menu.list_all() # => [dish_1, dish_2, dish_3]


"""
Add dishes to the menu
remove one 
list all will return the ones not removed
"""
menu = Menu()
dish_1 = Mock()
dish_2 = Mock()
dish_3 = Mock()
menu.add(dish_1)
menu.add(dish_2)
menu.add(dish_3)
menu.remove(dish_2)
menu.list_all() # => [dish_1, dish_3]

"""
Add dishes to the menu
select returns the one selected
"""

menu = Menu()
dish_1 = Mock()
dish_2 = Mock()
dish_3 = Mock()
menu.add(dish_1)
menu.add(dish_2)
menu.add(dish_3)
menu.list_select(dish_1) # => dish_1


"""
When intialised Dish will have two class variables
"""

dish = Dish("food", 2.00)
dish.name # => 'food'
dish.price # => 2.00

"""
Format returns dish like so  {name} is £{price}
"""

dish = Dish("food", 2.00)
dish.format() # => 'food is £2.00'


"""
order intialises with empty note and list
"""

my_order = Order()
my_order.list_order() # => []

"""
add note to order
"""
my_order = Order()
my_order.add_note('Extra chips please')
my_order.note # => 'Extra chips please'


"""
select dishes for order
use list order
returns added dishes
"""
my_order = Order()
menu = Mock()
dish_1 = Mock()
dish_2 = Mock()
dish_3 = Mock()
menu.menu_list.return_value = [dish_1, dish_2, dish_3]
my_order.select_dish(dish_2)
my_order.select_dish(dish_1)
my_order.list_order # => [dish_2, dish_1]

"""
create instance customer info
test format
returns formatted name, address, number
"""

my_info = CustomerInfo('Kumani', '123 Road' '07946464836')
my_info.format() # => "Name: Kumani \nAddress: 123 Road \nPhone Number: 07946464836"

"""
create instance of customer info
check get number returns phone number
"""

my_info = CustomerInfo('Kumani', '123 Road' '07946464836')
my_info.get_number() # => '07946464836'


```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
