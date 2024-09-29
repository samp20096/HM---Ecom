# Start
numbers: list[int] = []
SENTINEL: int = -999

while True:
    number1: int = int(input("Number: "))
    if number1 == SENTINEL:
        print("Finish")
        break
    if not number1 >= 0 or number1 > 10:
        print("Not in range.")
        continue
    numbers.append(number1)
    for number in range(11):
        count = numbers.count(number)
        if count > 0:
            print(f"Statistics: [{number}]: {count}")

# End
