from re import L


class Batiment:
    def __init__(self, name, price, earnings, level=0):
        self.name = name 
        self.price = price
        self.earnings = earnings
        self.level = level
        self.owner = None
        # self.collect = None
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
        super().__init__("CCM", 220, 20)
        self.level_price = [220, 200, 280, 360, 380, 560]
        self.earnings_price = [20, 60, 95, 145, 215, 315]

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


class eglise_Class(Batiment):
    def __init__(self):
        super().__init__("eglise", 180, 10)
        self.level_price = [180, 140, 200, 270, 340, 500]
        self.earnings_price = [10, 35, 65, 110, 165, 235]

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


class rich_Class(Batiment):
    def __init__(self):
        super().__init__("rich", 220, 30)
        self.level_price = [220, 250, 400,500, 700, 900]
        self.earnings_price = [30, 55, 105, 175, 295,455]

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

class HM_Class(Batiment):
    def __init__(self):
        super().__init__("H&M", 230, 10)
        self.level_price = [230, 200, 300,400, 500, 600]
        self.earnings_price = [10, 40, 90, 160, 260,380]

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


class parking_Class(Batiment):
    def __init__(self):
        super().__init__("parking", 230, 25)
        self.level_price = [230, 280, 330,380, 480, 600]
        self.earnings_price = [25, 65, 125, 195, 275,375]

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


class skatepark_Class(Batiment):
    def __init__(self):
        super().__init__("skatepark", 120, 10)
        self.level_price = [120, 120,180,240,300,335]
        self.earnings_price = [10,25,50, 90,140,200]

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


class parc_Class(Batiment):
    def __init__(self):
        super().__init__("parc", 300, 30)
        self.level_price = [300, 360,400,475,600,750]
        self.earnings_price = [30,80,155,255,370,500]

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

class pharmacie_Class(Batiment):
    def __init__(self):
        super().__init__("pharmacie", 200, 25)
        self.level_price = [200,160,200,285,345,450]
        self.earnings_price = [25,55,95,150,225,320]

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

class gare_Class(Batiment):
    def __init__(self):
        super().__init__("gare", 230, 25)
        self.level_price = [230,300,350,430,540,640]
        self.earnings_price = [25,60,120,205,305,440]

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

class local_Class(Batiment):
    def __init__(self):
        super().__init__("local", 100, 10)
        self.level_price = [100,160,200,240,320,450]
        self.earnings_price = [10,25,60,105,165,255]

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

class RRCW_Class(Batiment):
    def __init__(self):
        super().__init__("RRCW", 200, 35)
        self.level_price = [200,210,300,360,400,500]
        self.earnings_price = [35,80,125,170,240,340]

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

class parcbourdon_Class(Batiment):
    def __init__(self):
        super().__init__("parcbourdon", 120, 10)
        self.level_price = [120,150,170,180,200,250]
        self.earnings_price = [10,25,50,75,100,125]

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

class pétanque_Class(Batiment):
    def __init__(self):
        super().__init__("pétanque", 70, 10)
        self.level_price = [70,100,120,150,170,190]
        self.earnings_price = [10,25,40,60,85,115]

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


class bellavita_Class(Batiment):
    def __init__(self):
        super().__init__("bellavita", 200, 30)
        self.level_price = [200,260,300,380,450,530]
        self.earnings_price = [30,65,110,170,145,245]

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

class bois_Class(Batiment):
    def __init__(self):
        super().__init__("bois", 70, 10)
        self.level_price = [70,90,110,130,140,160]
        self.earnings_price = [10,25,40,60,85,115]

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

class bois_Class(Batiment):
    def __init__(self):
        super().__init__("bois", 70, 10)
        self.level_price = [70,90,110,130,140,160]
        self.earnings_price = [10,25,40,60,85,115]

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


class mediamarkt_Class(Batiment):
    def __init__(self):
        super().__init__("mediamarkt", 200, 25)
        self.level_price = [200,210,250,300,450,600]
        self.earnings_price = [25,50,85,140,220,325]

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
eglise = eglise_Class()
rich = rich_Class()
HM= HM_Class()
parking=parking_Class()
skatepark = skatepark_Class()
parc = parc_Class()
pharmacie = pharmacie_Class()
gare = gare_Class()
local = local_Class()
RRCW = RRCW_Class()
parcbourdon = parcbourdon_Class()
pétanque = pétanque_Class()
bellavita = bellavita_Class()
boisdesbruyeres = bois_Class()
boisberlaymont= bois_Class()
mediamarkt = mediamarkt_Class()


dico_of_bat = {}
dico_of_bat['CCM'] = CCM
dico_of_bat['eglise'] = eglise
dico_of_bat['rich'] = rich
dico_of_bat['H&M'] = HM
dico_of_bat['parking'] = parking
dico_of_bat['skatepark'] = skatepark
dico_of_bat['parc']= parc
dico_of_bat['pharmacie']= pharmacie
dico_of_bat['gare']= gare
dico_of_bat['local']= local
dico_of_bat['RRCW']= RRCW
dico_of_bat['parcbourdon']= parcbourdon
dico_of_bat['pétanque']= pétanque
dico_of_bat['bellavita']= bellavita
dico_of_bat['boisdesbruyeres']= boisdesbruyeres
dico_of_bat['boisberlaymont']= boisberlaymont
dico_of_bat['mediamarkt']= mediamarkt







