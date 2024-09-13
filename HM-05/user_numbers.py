# Start

first_num: int = int(input("First number: "))
second_num: int = int(input("Second number: "))

if first_num < second_num:
    for i in range(first_num, second_num + 1):
        print(i, end=" ")
else:
    for i in range(first_num, second_num - 1, -1):
        print(i, end=" ")

# End
