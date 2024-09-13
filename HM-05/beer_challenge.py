# Start

count: int = 10

while count != 0:
    age: int = int(input("What's your age? "))
    if age >= 18:
        print("Here is your free beer! :)")
        count -= 1
    else:
        print("You're not old enough.")

if count == 0:
    print("Sorry, we're out of free beer for today.")

# End
