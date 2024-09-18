# Start

number: int = int(input("Put a number: "))
count: int = 0

while number % 7 == 0 or number % 11 == 0:
    if number % 11 == 0:
        print("Your number is not in sequence of % 7 == 0")
        break
    else:
        count += 1
        number = int(input("Put another number: "))

else:
    print(f"Your number is not % 7 == 0 \nYou tried for {count} times")

# End
