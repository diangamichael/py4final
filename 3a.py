import math

# Function to read pricing data from a file and store it in a dictionary
def readPricing(filename, pricing):
    with open(filename, "r") as file:
        for line in file:
            char, price = line.strip().split()
            pricing[char] = int(price)

# Function to display pricing table according to font size
def showPricing(charPricing, fontPricing, fontSize):
    # Calculate the factor by which the pricing needs to be multiplied based on font size
    factor = 1
    if fontSize == 36:
        factor = 1.5
    elif fontSize == 48:
        factor = 2

    # Round the prices to the nearest integer and display the pricing table
    print("Pricing for font size {}pts".format(fontSize))
    print("="*27)
    row = ""
    for char, price in charPricing.items():
        # Calculate the new price based on the factor and round it to the nearest integer
        newPrice = round(price * factor)
        # Add the character and its price to the current row
        row += "{} {} ".format(char, newPrice)
        # If the row has 10 characters, display it and start a new row
        if len(row) >= 20:
            print(row)
            row = ""
    # If there are any characters left in the last row, display it
    if row != "":
        print(row)

# Main function to tie everything together
def main():
    # Create empty dictionaries for character pricing and font pricing
    charPricing = {}
    fontPricing = {}

    # Read character pricing and font pricing from files and store them in the dictionaries
    readPricing("char-pricing.txt", charPricing)
    readPricing("font-pricing.txt", fontPricing)

    # Display the pricing table for font size 24pts
    showPricing(charPricing, fontPricing, 24)

    # Display the pricing table for font size 36pts
    showPricing(charPricing, fontPricing, 36)

    # Display the pricing table for font size 48pts
    showPricing(charPricing, fontPricing, 48)

# Call the main function to run the program
main()