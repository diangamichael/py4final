
def main():
    characters = load_characters_pricings()
    font_sizes = load_font_sizes_pricings()
    while True:
        print("MonkeyPrint Embroidery Services")
        print("===============================")
        print("1. Display Pricing Table")
        print("2. Request for Quote")
        print("3. Add/Update Characters’ Pricings")
        print("4. Add/Update Font Sizes’ Pricings")
        print("0. Exit")
        selection = input("Enter selection: ")
        if selection == "1":
            font_size = int(input("Enter font size: "))
            if font_size in font_sizes:
                display_characters_pricings(characters, font_sizes[font_size])
            else:
                print("Invalid font size!")
        elif selection == "2":
            quote = input("Enter characters: ")
            font_size = int(input("Enter font size: "))
            if all(c in characters for c in quote) and font_size in font_sizes:
                pricing = compute_pricing(quote, characters, font_sizes[font_size])
                if pricing > 8:
                    discounted_pricing = min(pricing, pricing - min(characters.values()))
                    print(f"Pricing: ${pricing:.2f}")
                    print(f"After 5% discount: ${discounted_pricing:.2f}")
                else:
                    lowest_priced_char = min(characters, key=characters.get)
                    if lowest_priced_char in quote:
                        print(f"Pricing: ${pricing:.2f}")
                        print(f"After 1 free character: ${pricing - characters[lowest_priced_char]:.2f}")
                    else:
                        print(f"Pricing: ${pricing:.2f}")
            else:
                print("Invalid characters or font size!")
        elif selection == "3":
            add_update_characters_pricings(characters)
        elif selection == "4":
            add_update_font_sizes_pricings(font_sizes)
        elif selection == "0":
            break
        else:
            print("Invalid selection!")