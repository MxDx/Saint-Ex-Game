from batiment import *
import json

class Person:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money
        self.batiments = []

    def buyBatiment(self, batiment):
        if batiment.price > self.money:
            print("Pas assez de thunes")
        else:
            self.batiments.append(batiment)
            self.money -= batiment.price
            print("Transaction de {} effectué, il reste {} sur votre compte".format(batiment.price,self.money))

    def addMoney(self, money):
        self.money += money

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def __str__(self):
        return "Il reste {} sur ton comtpe, et tu as {} batiments".format(self.money, len(self.batiments))


Maxime = Person("Maxime", 200)
CCM = CCM_Class()

personData = {}
personData["Maxime"] = json.dumps(Maxime.__dict__)

print(Maxime)

with open('PersonData.json', 'w') as outfile:
    json.dump(personData, outfile)
