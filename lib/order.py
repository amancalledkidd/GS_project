class Order():
    def __init__(self, menu):
        self.order_list = []
        self.note = ""
        self.menu = menu

    def list_order(self):
        return self.order_list

    def select_dish(self, dish):
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


    def make_order(self, customer_info):
        # Side effects: 
        #   Calls order formatter
        #   calls order confirmation
        pass
