menu = {
    "Burger": 12,
    "Fries": 5,
    "Drinks": 5
}

for item in menu:
    print(item, ": $", menu[item])

choice = input("Enter an item: ")

found = False

for item in menu:
    if choice == item:
        print(item, ": $", menu[item])
        found = True

if found == False:
    print("Item is not on the menu.")