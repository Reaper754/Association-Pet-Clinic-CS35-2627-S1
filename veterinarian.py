class Veterinarian:
    def __init__(self):
        self.name = "TBD"
        self.health = 100
        self.money = 1000

    def checkup(self, pet):
        print(f"File: Name: {pet.name}. Health: {pet.health}%. Species: {pet.species}. Symptom: {pet.symptom}")

    def treat(self, pet, amount):
        if pet.name == "Max":
            print(f"{self.name} healed Max and it turns out he was faking his illness to get attention. Gained 200 dollars.")
            self.money += 200
            print(f"Your health: {self.health}, your money: {self.money}")
        if pet.name == "Fluffy":
            pass