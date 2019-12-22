from menu import Menu

class DrinkMenu(Menu): 
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

    def info(self):
        return self.name + ":¥" + str(self.price) + "(" + str(self.amount) + "mL)"
