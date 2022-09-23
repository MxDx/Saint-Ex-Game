class Batiment:
    def __init__(self, name, price, index, level=1):
        self.name = name 
        self.price = price
        self.level = level
        self.index = index

    def get_price(self):
        return self.price
        

class CCM_Class(Batiment):
    def __init__(self):
        super().__init__("CCM", 220, 0)
    