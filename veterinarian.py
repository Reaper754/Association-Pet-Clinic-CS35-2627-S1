class Veterinarian:
    def __init__(self):
        self.name = "TBD"
        self.health = 100
        self.money = 1000

    def checkup(self, pet):
        print(f"File: Name: {pet.name}. Health: {pet.health}%. Species: {pet.species}. Symptom: {pet.symptom}")

    def treat(self, Pet, amount):
        pass