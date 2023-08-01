class OrderFormatter():
    def __init__(self, order, customer_info):
        self.order = order
        self.customer_info = customer_info

    def get_order_info(self):
        order_info = "Order: \n"
        for dish in self.order.list_order():
            order_info += f"{dish.format()} \n"
        order_info += f"Total: £{self.order.order_total()} \n"
        order_info += f'{self.customer_info.format()} \n'
        order_info += f'Note: {self.order.note} \n'
        return order_info
