import random
# Start

number: int = random.randint(1, 100)
count: int = 0

while True:
    user_try: int = int(input("Put your guess here: "))
    count += 1
    if user_try < number:
        print("Your number is too small, try again!")
    elif user_try > number:
        print("Your number is too big, try again!")
    else:
        print(f"You correct! The number is {number} \nYour tries are: {count}")
        break

# End