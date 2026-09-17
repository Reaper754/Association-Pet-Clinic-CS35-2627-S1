from pet import Pet
from veterinarian import Veterinarian

dog = Pet("Max", 100, "Dog", "Slugish")
cat = Pet("Fluffy", 50, "Cat", "Worms")
ferret = Pet("Buck", 75, "Ferret", "Won't eat")
vet = Veterinarian()

select = """Choose your patient:
1 for Max | 2 for Fluffy | 3 for Buck | 4 for exit\n"""

message = """Enter an input: 
| Checkup | Treat |\n"""

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
        print("type exit to exit.")
        if patient == 1:
            user_input = input(message).strip().lower()
            for command, action in zip(commands, actions1):
                if user_input == command:
                    if command == "treat":
                        action()
                    action()
                    break
                else:
                    if user_input == "exit":
                        break
                    print("Invalid command.")
        elif patient == 2:
            user_input = input(message).strip().lower()
            for command, action2 in zip(commands, actions2):
                if user_input == command:
                    action2(cat)
                    break
                else:
                    if user_input == "exit":
                        break
                    print("Invalid command.")
        elif patient == 3:
            user_input = input(message).strip().lower()
            for command, action3 in zip(commands, actions3):
                if user_input == command:
                    action3(ferret)
                    break
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

