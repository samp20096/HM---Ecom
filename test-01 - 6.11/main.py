# תנאים:
# 1.
# numbers: list[float] = [float(input("Float numbers: ")) for _ in range(3)]
# print(min(numbers))
# print(min(numbers))
# print(min(numbers))

# 2.
# numbers: list[int] = [int(input("Numbers: ")) for _ in range(2)]
# print(f"Ave: {(numbers[0] + numbers[1]) / len(numbers)}")

# 3.
# numbers: list[int] = [int(input("Float numbers: ")) for _ in range(3)]
# print(f"Biggest number: {max(numbers)}")

# 4.
# time: int = int(input("Time of movie in minutes: "))
# print(f"Hours: {time // 60}, Minutes: {time % 60}")

# 5.
# while True:
#     try:
#         number: int = int(input("Number (4 Digits): "))
#         if 1000 <= number <= 9999:
#             print(f"The rightest number is: {number % 10}")
#             break
#         else:
#             print("Not 4 digits, try again.")
#     except ValueError:
#         print("Input in not int, try again.")

# 6.
# while True:
#     try:
#         number: int = int(input("Number (4 Digits): "))
#         if 1000 <= number <= 9999:
#             print(f"The rightest number is: {(number % 100) // 10}")
#             break
#         else:
#             print("Not 4 digits, try again.")
#     except ValueError:
#         print("Input in not int, try again.")

# 7.
# while True:
#     try:
#         number: int = int(input("Number (2 Digits): "))
#         if 10 <= number <= 99:
#             print(f"The asarot + ahadot = {(number % 10) + (number // 10)}")
#             break
#         else:
#             print("Number not 2 digits, try again.")
#     except ValueError:
#         print("Input not int, try again.")

# 8.
# while True:
#     try:
#         number: int = int(input("Number (2 Digits): "))
#         if 10 <= number <= 99:
#             print(f"Reversed number for {number}: {(number % 10 * 10) + (number // 10)}")
#             break
#         else:
#             print("Number not 2 digits, try again.")
#     except ValueError:
#         print("Input not int, try again.")

# 9.
# while True:
#     try:
#         number: int = int(input("Number: "))
#     except ValueError:
#         print("Input is not int, try again.")
#         continue
#     print("Even" if number % 2 == 0 else "Odd")
#     break

# 10.
# salary: float = float(input("Salary: "))
# salary_total: float = 0
# if salary > 0:
#     salary_total += 6000
#     salary -= 6000
# if salary > 0:
#     step1: float = min(salary, 6000)
#     salary_total += step1 * 0.9
#     salary -= step1
# if salary > 0:
#     step2: float = min(salary, 6000)
#     salary_total += step2 * 0.8
#     salary -= step2
# if salary > 0:
#     step3: float = min(salary, 7000)
#     salary_total += step3 * 0.7
#     salary -= step3
# if salary > 0:
#     step4: float = min(salary, 10_000)
#     salary_total += step4 * 0.6
#     salary -= step4
# if salary > 0:
#     step5: float = min(salary, 15_000)
#     salary_total += step5 * 0.55
#     salary -= step5
# if salary > 0:
#     salary_total += salary * 0.49
#
# print(salary_total)


# 11.
# age: int = int(input("Age: "))
# height: float = float(input("Height: "))
#
# if age > 18 and height > 100:
#     print("Accepted")
# elif 8 <= age <= 18 and height > 115:
#     print("Accepted")
# else:
#     print("Not accepted")


# לולאות:
# 1.
# while True:
#     try:
#         top_num: int = int(input("Number(Positive): "))
#     except ValueError:
#         print("Input is not int, try again.")
#         continue
#     if top_num <= 0:
#         print("Number is not positive")
#         continue
#     for i in range(1, top_num + 1):
#         print(i)
#     break

# 2.
# while True:
#     try:
#         num_list: list[int] = [int(input("Number(Positive): ")) for _ in range(2)]
#     except ValueError:
#         print("Input is not int, try again.")
#         continue
#     for i in range(min(num_list), max(num_list) + 1):
#         print(i)
#     break

# 3.
# while True:
#     try:
#         number: int = int(input("Number: "))
#     except ValueError:
#         print("Input not int, try again.")
#         continue
#     if number % 2 == 0:
#         for i in range(0, number + 1, 2):
#             print(i)
#         break
#     else:
#         for i in range(0, number, 2):
#             print(i)
#         break

# 4.
# while True:
#     try:
#         number: int = int(input("Number: "))
#         den: int = int(input("Den: "))
#     except ValueError:
#         print("Input not int, try again.")
#         continue
#     if number % den == 0:
#         for i in range(0, number + 1, den):
#             print(i)
#         break
#     else:
#         for i in range(0, number, den):
#             print(i)
#         break


# עיבוד נתונים:
# 1.
# SENTINEL: int = -99
# count: int = 0
#
# while True:
#     try:
#         number: int = int(input("Number: "))
#     except ValueError:
#         print("Input is not int, try again.")
#         continue
#     if number != SENTINEL:
#         count += number
#     if number == SENTINEL:
#         if number == SENTINEL and count == 0:
#             print(None)
#             break
#         print(f"Total number = {count}")
#         break

# 2.
# SENTINEL: int = -99
# min_num: int = None
# max_num: int = None
#
# while True:
#     try:
#         number: int = int(input("Number: "))
#     except ValueError:
#         print("Input is not int, try again.")
#         continue
#     if number == SENTINEL or number <= 0:
#         if number == SENTINEL and min_num == None:
#             print(None)
#             break
#         print(f"Min number = {min_num}, Max num = {max_num}")
#         break
#     if min_num is None or number < min_num:
#         min_num = number
#     if max_num is None or number > max_num:
#         max_num = number

# 3.
# high_num: int = None
# count: int = 0
# high_num_count: int = 0
#
# while True:
#     try:
#         number: int = int(input("Number: "))
#     except ValueError:
#         print("Input not int, try again.")
#         continue
#     count += 1
#     if high_num is None or number > high_num:
#         high_num = number
#         high_num_count += 1
#     if count == 5:
#         print(f"Serial number of highest number is: {high_num_count}")
#         break

# 4.
# num1: int = int(input("Number: "))
# num2: int = int(input("Number: "))
# count: int = 0
# for _ in range(num2):
#     count += num1
# print(count)

# 5.
# num1: int = int(input("Number: "))
# num2: int = int(input("Number: "))
# count: int = 1
# for _ in range(num2):
#     count *= num1
# print(count)

# 6.
# x: int = int(input("Number (0 - 9999): "))
# y: int = int(input("Number in number? "))
#
# ahadot: int = x % 10
# asarot: int = (x % 100) // 10
# meot: int = (x % 1000) // 100
# alafim: int = x // 1000
#
# if ahadot == y or asarot == y or meot == y or alafim == y:
#     print(True)
# else:
#     print(False)

#7.
# num1: int = int(input("Number: "))
# num2: int = int(input("Number2: "))
# div_big = None
#
# if num1 > num2:
#     while True:
#         for i in range(num1, 0, -1):
#             if num1 % i == 0:
#                 if num2 % i == 0:
#                     if div_big is None or div_big < i:
#                         div_big = i
#         else:
#             print(div_big)
#             break
# else:
#     while True:
#         for i in range(num2, 0, -1):
#             if num2 % i == 0:
#                 if num1 % i == 0:
#                     if div_big is None or div_big < i:
#                         div_big = i
#         else:
#             print(div_big)
#             break


# 8.
# number: int = int(input("Number: "))
# print("Prime" if all(number % i != 0 for i in range(2, number)) else "Not prime")



# לולאות מורכבות:
# 1.
# temp: list[int] = []
# count: int = 0
# zero_added: bool = False
#
# while count < 12:
#     try:
#         user_temp: int = int(input("Temperature: "))
#     except ValueError:
#         print("Input is not int, try again.")
#         continue
#     if user_temp == 0:
#         if zero_added:
#             continue
#         zero_added = True
#     if not -5 <= user_temp <= 40:
#         print("Wrong data")
#         break
#     print("Correct data")
#     temp.append(user_temp)
#     count += 1
# else:
#     print(f"Ave temp: {sum(temp) / len(temp):.2f}\n"
#           f"Min temp: {min(temp)}\n"
#           f"Max temp: {max(temp)}")

# 2. need to finish
# country: list[int] = [] # saving to get up to 44 country's
# vote_count: list[int] = [0] * 4
# list_options: list[str] = ["For", "Against", "Avoid", "Veto"]
# vote_object: str = input("What object we discuss today? ")
#
# while vote_count[3] < 1:
#     print(f"{vote_object}\n"
#           f"Your vote: \n"
#           f"1. {list_options[0]}\n"
#           f"2. {list_options[1]}\n"
#           f"3. {list_options[2]}\n"
#           f"4. {list_options[3]}")
#     try:
#         vote: int = int(input("Your vote: "))
#     except ValueError:
#         print("Input is not int, try again.")
#         continue
#     if 0 >= vote >= 5:
#         continue
#     country.append(vote)
#     if vote == 1:
#         vote_count[0] += 1
#     if vote == 2:
#         vote_count[1] += 1
#     if vote == 3:
#         vote_count[2] += 1
#     if vote == 4:
#         print(f"Veto country serial number: {country.index(4)}")
#         break
#     if len(country) == 44:
#         print(f"Total for: {vote_count[0]}\n"
#               f"Total against: {vote_count[1]}\n"
#               f"Total avoid: {vote_count[2]}\n"
#               f"{f"First vote for: {country.index(1)}" if vote_count[0] > 0 else ""}\n"
#               f"{f"Last vote against: {country.index(2, country[-1])}" if vote_count[1] > 0 else ""}")
#         break


























