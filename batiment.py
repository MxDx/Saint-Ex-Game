class Batiment:
    def __init__(self, name, price, earnings, level=0):
        self.name = name 
        self.price = price
        self.earnings = earnings
        self.level = level
        self.owner = None
        self.level_price = []
        self.earnings_price = []

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
        self.earnings_price[20, 60, 95, 145, 215, 315]

    def buy(self, buyer):
        if self.owner != None:
            del self.owner.batiments[self.name]
        self.owner = buyer

    def upgrade(self):
        if (self.level==5):
            print("Plus de upgrade possible")
        else:
            self.level += 1

    def __str__(self):
        return super().__str__()





CCM = CCM_Class()


dico_of_bat = {}
dico_of_bat['CCM'] = CCM