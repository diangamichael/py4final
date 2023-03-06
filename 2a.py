def ticketValidator(numbers):
    # Check if all numbers are within 1 to 49
    for num in numbers:
        if num < 1 or num > 49:
            return False
    
    # Check if all numbers are unique
    if len(numbers) != len(set(numbers)):
        return False
    
    return True


# Test cases
print(ticketValidator([5, 47, 6, 32, 49]))  # True
print(ticketValidator([5, 6, 7, 6, 45, 31]))  # False
print(ticketValidator([51, 6, 7]))  # False