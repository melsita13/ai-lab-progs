database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary", "Green", "Yellow"]

def main():
    print("*-----Forward Chaining*")
    print("\n X is \n1. Croaks \n2. Eat Flies \n 3. Shrimps \n 4. Sings")
    x = int(input("Select One: "))

    if x in [1, 2]:
        animal, color_options = knowbase[0], ["Green", "Yellow"]
    elif x in [3, 4]:
        animal, color_options = knowbase[1], ["Yellow", "Green"]
    else:
        print("Invalid Option Selected")
        return

    print(f"\nChance of {animal}")
    print(f"\nX is {database[x-1]}")
    print("Color is 1. Green 2. Yellow")
    k = int(input("Select Color: "))

    if (animal == "Frog" and k == 1) or (animal == "Canary" and k == 2):
        print(f"Yes, it is {animal} and Color is {color_options[0]}")
    else:
        print("Invalid Knowledge Database")

if __name__ == "__main__":
    main()
