from pet import Pet

class Veterinarian():
    def __init__(self):
        self.name = "TBD"
        self.health = 100
        self.money = 1000

    def checkup(self, Pet):
        print(f"File: Name: {Pet.name}. Health: {Pet.health}%. Species: {Pet.species}. Symptom: {Pet.symptom}")

    def treat(self, Pet, amount):
        pass