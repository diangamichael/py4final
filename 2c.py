import random

def ticketValidator(numbers):
    # Check if all numbers are unique and within 1 to 49
    if len(numbers) != len(set(numbers)):
        return False
    for number in numbers:
        if number < 1 or number > 49:
            return False
    return True

def quickPick():
    # Generate 6 unique random numbers from 1 to 49
    numbers = []
    while len(numbers) < 6:
        number = random.randint(1, 49)
        if number not in numbers:
            numbers.append(number)
    return numbers

while True:
    print("TOTO Menu")
    print("1. Ticket Entry")
    print("2. Quick Pick")
    print("0. Exit")

    option = int(input("Enter option: "))
    if option == 0:
        print("Good luck to you!!")
        break

    if option == 1:
        numbers = []
        for i in range(1, 7):
            number = int(input(f"Enter pick {i}: "))
            numbers.append(number)
        if ticketValidator(numbers):
            print(f"Your TOTO ticket {numbers} is valid")
        else:
            print(f"{numbers} is an Invalid TOTO ticket")

    elif option == 2:
        numbers = quickPick()
        print(f"This is your lucky ticket: {numbers}")