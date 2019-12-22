class Menu:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def total_price(self,count):
        total_price = self.price * count
        
        if count >= 3:
            total_price =total_price* 0.9
        return round(total_price)

  