class Veterinarian:
    def __init__(self):
        self.name = "TBD"
        self.health = 100
        self.money = 1000

    def checkup(self, pet):
        print(f"File: Name: {pet.name}. Health: {pet.health}%. Species: {pet.species}. Symptom: {pet.symptom}")

    def treat(self, pet, amount):
        if pet.name == "Max":
            if amount == 0:
                print(f"{self.name} healed {pet.name} and it turns out he was faking his illness to get attention. Gained 200 dollars.")
                self.money += 200
                pet.symptom = "none"
                print(f"Your health: {self.health}, your money: {self.money}")
                print(f"File: Name: {pet.name}. Health: {pet.health}%. Species: {pet.species}. Symptom: {pet.symptom}")

            else:
                print("Wrong treatment.")
        if pet.name == "Fluffy":
            if amount == 50:
                print(f"{self.name} healed {pet.name} by giving it a shot. Lost 20 health from scratches but gained 300 dollars")
                self.health -= 20
                self.money += 300
                pet.symptom = "none"
                pet.health += amount
                print(f"Your health: {self.health}, your money: {self.money}")
                print(f"File: Name: {pet.name}. Health: {pet.health}%. Species: {pet.species}. Symptom: {pet.symptom}")
            else:
                print("Wrong treatment.")
        if pet.name == "Buck":
            if amount == 25:
                print(f"{self.name} healed {pet.name} by passing some kidney stones. Gained 500 dollars")
                self.money += 500
                pet.symptom = "none"
                pet.health += amount
                print(f"Your health: {self.health}, your money: {self.money}")
                print(f"File: Name: {pet.name}. Health: {pet.health}%. Species: {pet.species}. Symptom: {pet.symptom}")
            else:
                print("Wrong treatment.")