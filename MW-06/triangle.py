# Start

max_width: int = int(input("Put a random number: "))

for i in range(1, max_width + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
for i in range(max_width - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# End
