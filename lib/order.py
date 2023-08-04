
class Order():
    def __init__(self, menu):
        self.order_list = []
        self.note = ""
        self.menu = menu
        self.complete = False

    def list_order(self):
        return self.order_list

    def select_dish(self, dish, quantity=1):
        for _ in range(quantity):
            self.order_list.append(self.menu.select(dish))

    def remove_dish(self, dish):
        self.order_list.remove(self.menu.select(dish))

    def order_total(self):
        total = 0
        for dish in self.order_list:
            total += dish.price
        return total

    def add_note(self, note):
        self.note = note

    def get_order_reciept(self):
        order_info = "Order: \n"
        for dish in self.list_order():
            order_info += f"{dish.format()} \n"
        order_info += f"Total: £{self.order_total():.2f} \n"
        return order_info


    def make_order(self):
        self.complete = True
