# Start

number: int = int(input("Number: "))
width: int = number * 2 - 1

for i in range(1, number - 1):
    print(" " * (width - i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()

for i in range(number - 1, 0, -2):
    print(" " * (width - i + 2), end="")
    for j in range(1, i):
        print(j, end="")
    print()

# End
