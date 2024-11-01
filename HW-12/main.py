import random, statistics

# random is in use from question 11

# 1.
# number: int = int(input("Number (esroni): "))
# print(f"{f"The diff is: {number - 10}" if number >= 10 else f"Number * 10: {number * 10}"}")

# 2.
# count: int = 0
# for _ in range(3):
#     number: int = int(input("Number: "))
#     count += number
# print(f"{f"Total: {count}" if count > 100 else "Total is under 100"}")

# 3.
# need to check ###############33

# 4.
# age: int = int(input("Age: "))
# print(f"{f"Age is: {age}" if 0 <= age <= 120 else "Age not in range"}")

# 5.
# number: int = int(input("Number (100 - 999): "))
# print(f"The middle number is: {(number // 10) % 10}")

# 6.
# number: int = int(input("Number: "))
# for i in range(number, 1 - 1, -1):
#     print(f"Number: {i}")

# 7.
# numbers: list[int] = [int(input("Number: ")) for _ in range(2)]
# for i in range(numbers[0], numbers[-1] + 1):
#     if i % 2 == 0:
#         print(f"Even numbers: {i}")

# 8.
# number: int = int(input("Even number: "))
# print(*(i for i in range(1, number + 1) if i % 3 == 0 or i % 5 == 0))
# had to search for that way to put all the code in one line and managed to get the answer for

# 9.
# number: int = int(input("Even number: "))
# print(*(i for i in range(1, number + 1) if i % 7 == 0))

# 10.
# There is no question for that number...

# 11.
# count: int = 0
# SENTINEL: int = 0
# while True:
#     number: int = random.randint(-10, 10)
#     print(number) # the print is to check that we're actually getting random numbers in our range
#     if number == SENTINEL:
#         break
#     if number < 0:
#         count += number
# print(f"Total negative numbers: {count}")

# 12.
# sort - just to remember for that question
# numbers: list[int] = [random.randint(1, 100) for _ in range(10)]
# numbers.sort(reverse=True)
# print(numbers)

# 13. That took me a while to find a way to answer with a lot of checking about prime numbers
# count: int = 0
# SENTINEL: int = 0
# numbers: list[int] = [] # just for visual to check if right
# while True:
#     number: int = random.randint(0, 100)
#     numbers.append(number)
#     if number == SENTINEL:
#         break
#     if number > 1:
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 break
#         else:
#             count += 1
#
# print(numbers)
# print(f"{count} Prime numbers are found from total "
#       f"{len(numbers)} numbers in the list")

# 14.
# numbers: list[int] = [random.randint(1, 100) for _ in range(5)]
#
# ave_numbers: int = statistics.mean(numbers)
# bigger_num: list[int] = [number for number in numbers if number > ave_numbers]
#
# print(f"The average of numbers is: {ave_numbers}\n"
#       f"The greatest numbers above average are: {bigger_num}\n"
#       f"List of given numbers: {numbers}")

# 15.
# numbers: list[int] = [random.randint(1, 50) for _ in range(2)]
# high_num: int = max(numbers)
# count: int = 0
#
# while high_num >= min(numbers):
#     high_num -= min(numbers)
#     count += 1
#
# print(f"{max(numbers)} / {min(numbers)} = {count}")

# Bonuses:
# 16.
# try:
#     number: int = int(input("Number (100 - 999): "))
#
#     meot: int = number // 100
#     asarot: int = number // 10 % 10
#     ahadot: int = number % 10
#
#     added: int = meot + asarot + ahadot
#     if added % 3 == 0:
#         print("Dividing by 3")
#     else:
#         print("Not dividing by 3")
# except:
#     print("Not a digit")

# 17.
# word: str = input("Word: ")
#
# if word[0] == word[-1]:
#     print("Reversible")
# else:
#     print("Not Reversible")