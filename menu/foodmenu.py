from menu import Menu

class FoodMenu(Menu):
    def __init__(self,name,price,colorie):
        super().__init__(name, price)
        self.colorie = colorie

    def info(self):
        return self.name + ":¥" + str(self.price) + "(" + str(self.colorie) + "kcal)"
