import ast

# Load characters' and font sizes' pricings from files
with open("characters.txt", "r") as f:
    characters_pricing = ast.literal_eval(f.read())

with open("font_sizes.txt", "r") as f:
    font_sizes_pricing = ast.literal_eval(f.read())

def display_pricing_table():
    font_size = int(input("Enter font size: "))
    if font_size in font_sizes_pricing:
        print("Character\tPrice")
        for char, price in characters_pricing.items():
            print(char + "\t\t$" + "{:.2f}".format(price * font_sizes_pricing[font_size]))
    else:
        print("Invalid font size")

def request_for_quote():
    characters = input("Enter characters: ")
    font_size = int(input("Enter font size: "))
    if font_size in font_sizes_pricing:
        total_price = 0
        for char in characters:
            if char not in characters_pricing:
                print("Invalid character: " + char)
                return
            total_price += characters_pricing[char] * font_sizes_pricing[font_size]
        print("Pricing: $" + "{:.2f}".format(total_price))
        if total_price >= 8:
            discount_price = total_price * 0.95
            lowest_price = min(characters_pricing.values()) * font_sizes_pricing[font_size]
            if lowest_price <= discount_price:
                discount_price -= lowest_price
                print("After 5% discount and lowest priced character free: $" + "{:.2f}".format(discount_price))
            else:
                print("After 5% discount: $" + "{:.2f}".format(discount_price))
    else:
        print("Invalid font size")

def add_update_characters_pricing():
    char = input("Enter character: ")
    if char not in characters_pricing:
        price = float(input("Enter pricing: "))
        characters_pricing[char] = price
    else:
        print("Current pricing: $" + "{:.2f}".format(characters_pricing[char]))
        price = float(input("Enter new pricing: "))
        characters_pricing[char] = price
    with open("characters.txt", "w") as f:
        f.write(str(characters_pricing))

def add_update_font_sizes_pricing():
    font_size = int(input("Enter font size: "))
    if font_size not in font_sizes_pricing:
        ratio = float(input("Enter pricing ratio: "))
        font_sizes_pricing[font_size] = ratio
    else:
        print("Current pricing ratio: " + str(font_sizes_pricing[font_size]))
        ratio = float(input("Enter new pricing ratio: "))
        font_sizes_pricing[font_size] = ratio
    with open("font_sizes.txt", "w") as f:
        f.write(str(font_sizes_pricing))

# Main menu
while True:
    print("MonkeyPrint Embroidery Services")
    print("===============================")
    print("1. Display Pricing Table")
    print("2. Request for Quote")
    print("3. Add/Update Characters' Pricings")
    print("4. Add/Update Font Sizes' Pricings")
    print("0. Exit")
    selection = input("Enter selection: ")
    if selection == "1":
        display_pricing_table()
    elif selection == "2":
        request_for_quote()
    elif selection == "3":
        add_update_characters_pricing()
    elif selection == "4":
        add_update_font_sizes_pricing()
    elif selection == "0":
        break