# Start
from math import floor

floors: int = int(input("Put a random number: "))
width: int = floors * 2 - 1

for i in range(1, floors + 1):
    print(" " * (width - i), end="")
    print("*" * (i * 2 - 1))

# End
