# Start
number_list: list[int] = [] # list of all numbers
statistic: list[int] = [0] * 101 # list to count
SENTINEL: int = -999 # exit of loop

while True:
    number: int = int(input("Number: "))
    if number == SENTINEL:
        print("Finish")
        break
    if number < 0 or number > 100:
        print("Not in range")
        continue
    number_list.append(number) # append to number_list
    statistic[number] += 1 # adding 1 to the right index
    # looping to print the numbers we got right away
    for n in range(101):
        count = number_list.count(n)
        if count > 0:
            print(f"Statistics: [{n}]: {count}")
# looping to check what numbers we got and printing those statistics
for i in range(101):
    if statistic[i] > 0:
        print(f"Statistics: [{i}]: {statistic[i]}")

# End
