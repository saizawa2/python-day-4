menu = {
    "Drinks": 4,
    "Burger": 12,
    "Fries": 5
}

print("Drinks: $4")
print("Burger: $12")
print("Fries: $5")

choice = input("Enter an item: ").lower()

if choice == "drinks":
    print("Drinks: $4")

elif choice == "burger":
    print("Burger: $12")

elif choice == "fries":
    print("Fries: $5")

else:
    print("Item is not on the menu.")