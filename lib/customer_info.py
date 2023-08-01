class CustomerInfo():
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number

    def format(self):
        return f'Name: {self.name} \nAddress: {self.address} \nPhone Number: {self.number}'

    def get_number(self):
        return self.number