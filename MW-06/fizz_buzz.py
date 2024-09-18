# Start

number: int = int(input("Put a number: "))

while number % 5 == 0 or number % 3 == 0:
    if number % 5 == 0 and number % 3 == 0:
        print("Fizz Buzz")
        break
    if number % 3 == 0:
        print("Buzz")
        break
    if number % 5 == 0:
        print("Fizz")
        break
else:
    print("Number is not % 5 == 0 or % 3 == 0!")

# End
