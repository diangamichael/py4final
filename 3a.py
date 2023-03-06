import math

def readPricing(filename: str, pricing: dict):
    """
    This function reads the pricing file and store the keys and values into the given dictionary.
    The keys are the characters, and the values are the pricings.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split()
            pricing[parts[0]] = int(parts[1])

def showPricing(charPricing: dict, fontPricing: dict, fontSize: int):
    """
    This function displays the characters' pricing according to the given fontSize and pricing dictionaries.
    """
    print(f"Pricing for font size {fontSize}pts")
    print("=" * 27)
    for char in charPricing:
        price = charPricing[char]
        if char in fontPricing:
            price *= fontPricing[char][fontSize]
        print(f"{char} {round(price)}", end=" ")
        if ord(char) % 8 == 7:
            print()