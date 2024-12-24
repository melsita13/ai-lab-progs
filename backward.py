database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary"]
color = ["Green", "Yellow"]

def main():
    print("*-----Backward Chaining*")
    print("\nX is \n1. Frog \n2. Canary")
    x = int(input("Select One: "))

    if x == 1:
        animal, behavior, color_options = knowbase[0], database[1], ["Green", "Yellow"]
    elif x == 2:
        animal, behavior, color_options = knowbase[1], database[2], ["Yellow", "Green"]
    else:
        print("Invalid Option Selected")
        return

    print(f"\nChance of {behavior}")
    print(f"\nX is {animal}")
    print("Color is \n1. Green \n2. Yellow")
    k = int(input("Select Color: "))

    if (animal == "Frog" and k == 1) or (animal == "Canary" and k == 2):
        print(f"Yes, it is {color_options[0]} and will {behavior}")
    else:
        print("Invalid Knowledge Database")

if __name__ == "__main__":
    main()
