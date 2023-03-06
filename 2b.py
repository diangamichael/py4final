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