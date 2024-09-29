# Start
number_list: list[int] = []
statistic: list[int] = [0] * 101
SENTINEL: int = -999

while True:
    number: int = int(input("Number: "))
    if number == SENTINEL:
        print("Finish")
        break
    if number < 0 or number > 100:
        print("Not in range")
        continue
    number_list.append(number)
    statistic[number] += 1
    for n in range(101):
        count = number_list.count(n)
        if count > 0:
            print(f"Statistics: [{n}]: {count}")

for i in range(101):
    if statistic[i] > 0:
        print(f"Statistics: [{i}]: {statistic[i]}")

# End
