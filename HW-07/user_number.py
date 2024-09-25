# Start

# number: int = 0
positive: int = 0
negative: int = 0
zero_count: int = 0
seven_zero: int = 0
last_positive: int = None
last_negative: int = None
count: int = 0

while count != 10:
    number = int(input("Put a number: "))
    if number > 1000 or number < -1000:
        print("Not in range")
        continue
    if 1000 >= number >= -1000:
        count += 1
    if 0 < number <= 1000:
        positive += 1
    if -1000 <= number < 0:
        negative += 1
    if number == 0:
        zero_count += 1
    if number != 0 and number % 7 == 0:
        seven_zero += 1
    if last_positive is None and number > 0:
        last_positive = number
    if last_negative is None and number < 0:
        last_negative = number
    if number == -9999:
        print("Finish")
        break
else:
    print(f"Positive: {positive} Negative: {negative} \n"
          f"Zero's: {zero_count} \n% 7 == 0: {seven_zero} \n"
          f"Last positive: {last_positive} Last negative: {last_negative}")

# End
