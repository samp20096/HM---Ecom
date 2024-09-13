# Start

while True:
    height: float = float(input("What your height? "))
    if 0.4 > height or 2.4 < height:
        print("Wrong input")
    else:
        print(f"Your height is: {height}")
        break

# End
