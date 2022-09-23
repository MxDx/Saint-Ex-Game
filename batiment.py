class Batiment:
    def __init__(self, name, price, index, level=0):
        self.name = name 
        self.price = price
        self.level = level
        self.index = index
        self.owner = None
        self.level_price = []

    def get_price(self):
        return self.price

    def upgrade(self): 
         self.level +=1; 

    def __str__(self):
        return self.name

class CCM_Class(Batiment):
    def __init__(self):
        super().__init__("CCM", 220, 0)
        self.level_price = [220, 200, 280, 360, 380, 560]

    def buy(self, buyer):
        if self.owner != None:
            self.owner.batiments.remove(self)
        self.owner = buyer

    def upgrade(self):
        if (self.level==5):
            print("Plus de upgrade possible")
        else:
            self.level += 1

    def __str__(self):
        return super().__str__()





CCM = CCM_Class()