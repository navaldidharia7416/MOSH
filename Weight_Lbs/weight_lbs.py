weight = int(input("Enter weight:"))
choice = input("Enter (L)bs or (K)g:")
if choice.upper() == "L":
    converted = weight * 0.45
    print(f"You are {converted} Lbs")
else:
    converted = weight // 0.45
    print(f"You are {converted} Kg")

