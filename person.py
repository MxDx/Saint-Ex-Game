from batiment import *
import json

class Person:
    def __init__(self, name, money=0, batiments={}):
        self.name = name
        self.money = money
        self.batiments = {}
        for bat in batiments:
            self.batiments[bat] = dico_of_bat[bat]
        print("{} initialisé, avec {}$ et {} batiments".format(name, money, len(batiments)))

    def find(self, batiment):
            found = None
            for i in self.batiments:
                if str(self.batiments[i]) == batiment:
                    found = i
            return found

    def buyBatiment(self, batiment):
        if batiment in self.batiments:
            print("Tu l'as déjà saucisse")
        else:
            if batiment.price > self.money:
                print("Pas assez de thunes")
            else:
                self.batiments[batiment.name] = batiment
                self.money -= batiment.price
                batiment.buy(self)
                print("Transaction de {}$ effectué, il reste {}$ sur votre compte".format(batiment.price,self.money))

    def upgrade_batiment(self, batiment):
        found_batiment = self.find(batiment)
        if(found_batiment != None):
            if found_batiment.level_price[found_batiment.level+1] > self.money:
                print("Pas assez de thunes")
            else: 
                found_batiment.upgrade()
                self.money -= found_batiment.level_price[found_batiment.level]
                print("Upgrade de {}$ effectué level({} -> {}), il reste {}$ sur votre compte".format(found_batiment.level_price[found_batiment.level],found_batiment.level-1, found_batiment.level,self.money))
        else:
            print("T'as pas le batiment gros debilus !")        

    def addMoney(self, money):
        self.money += money
        print("Ajout de {}$ effectué".format(money))

    def toJSON(self):
        personData = {}
        personData["name"] = self.name
        personData["money"] = self.money
        personData["batiments"] = {}
        for bat in self.batiments:
            personData["batiments"][bat] = self.batiments[bat].__dict__
            personData["batiments"][bat]['owner'] = self.name
        return personData

    def __str__(self):
        return "Il reste {} sur ton comtpe, et tu as {} batiments".format(self.money, len(self.batiments))

def write_JSON(filename, dico_persons):
    with open(filename, 'w') as output_file:
        data = {}
        for person in dico_persons:
            data[dico_persons[person].name] = dico_persons[person].toJSON()
        json.dump(data, output_file)

def load_JSON(filename):
    with open(filename, 'r') as inputfile:
        data = json.load(inputfile)
        output_data = {}
        for person in data:
            print(data[person]['name'])
            output_data[person] = Person(data[person]['name'], data[person]['money'], data[person]['batiments'])
            for batiment in output_data[person].batiments:
                print(output_data[person].batiments[batiment].owner)
                output_data[person].batiments[batiment].owner = output_data[person]
    return output_data

persons = load_JSON('PersonData.json')

##################################################



persons['Maxime'].buyBatiment(CCM)



##################################################

write_JSON('PersonData.json', persons)





# Maxime = Person("Maxime", 200)

