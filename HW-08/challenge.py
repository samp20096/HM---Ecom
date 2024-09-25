# Start

numbers: list[int] = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

while True:
    value: int = int(input("What number? "))
    if value == -999:
        print("Out.")
        break

    index: int = 0
    while index < len(numbers) and numbers[index] < value:
        index += 1

    numbers.insert(index, value)

print(numbers)

# End
