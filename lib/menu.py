class Menu():
    def __init__(self):
        self.dish_list = []

    def list_all(self):
        return [dish.format() for dish in self.dish_list]
        

    def add(self, dish):
        self.dish_list.append(dish)

    def remove(self, dish):
        self.dish_list.remove(dish)

    def select(self, dish):
        if dish in self.dish_list:
            return dish
        else:
            raise Exception("We do not have this on the menu")