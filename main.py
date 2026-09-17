from pet import Pet
from veterinarian import Veterinarian

dog = Pet("Max", 100, "Dog", "Slugish")
cat = Pet("Fluffy", 50, "Cat", "Worms")
ferret = Pet("Buck", 75, "Ferret", "Won't eat")
vet = Veterinarian()

select = """Choose your patient:
1 for Max | 2 for Fluffy | 3 for Buck | 4 for exit\n"""

message = """Enter an input: 
| Checkup | Treat | Exit |\n"""

recover = "How much health should be recovered"

commands = [
    "checkup",
    "treat",
]

actions1 = [
    vet.checkup,
    vet.treat,
]

actions2 = [
    vet.checkup,
    vet.treat,
]

actions3 = [
    vet.checkup,
    vet.treat,
]

while True:
    try:
        patient = int(input(select))
        if patient == 1:
            user_input = input(message).strip().lower()
            if user_input == "treat":
                amount = int(input(recover))
                vet.treat(dog, amount)
            elif user_input == "checkup":
                vet.checkup(dog)
            else:
                if user_input == "exit":
                    break
                print("Invalid command.")
        elif patient == 2:
            user_input = input(message).strip().lower()
            if user_input == "treat":
                amount = int(input(recover))
                vet.treat(cat, amount)
            elif user_input == "checkup":
                vet.checkup(cat)
            else:
                if user_input == "exit":
                    break
                print("Invalid command.")
        elif patient == 3:
            user_input = input(message).strip().lower()
            if user_input == "treat":
                amount = int(input(recover))
                vet.treat(ferret, amount)
            elif user_input == "checkup":
                vet.checkup(ferret)
            else:
                if user_input  == "exit":
                    break
                print("Invalid command.")
        else:
            if patient == 4:
                break
            print("Invalid command.")
    except ValueError:
        print("Invalid input")

