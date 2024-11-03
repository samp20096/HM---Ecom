# 2.
# a.
#students: int = 103
# students: int = int(input("How many students in total? "))
#
# students_left: int = students % 30
# full_class: int = students // 30
#
# print(f"Total full classes: {full_class}\n"
#       f"Total last class amount of students left: {students_left}")

# b.
# while True:
#     try:
#         number: int = int(input("Number (10 - 99): "))
#         if 10 <= number <= 99:
#             if number % 10 > number // 10:
#                 number = (number % 10 * 10) + (number // 10)
#                 print(f"ahadot > asarot, reversed = {number}")
#             else:
#                 print(f"Your number is: {number}")
#             break
#         else:
#             print(f"{number} is not in range, try again.")
#     except ValueError:
#         print("Invalid input, need input an integer.")

# c.
# prime_num: list[int] = [i for i in range(2 ,200 + 1) if all(i % x != 0 for x in range(2, i))]
# for number in prime_num:
#     print(number, end=", ")

# d.
# question: str = "What region you live in? "
# #                            0              1              2            3
# question_list: list[str] = ["A. Northern", "B. Southern", "C. Middle", "D. Else"]
# #                        0  1  2  3
# count_list: list[int] = [0, 0, 0, 0]
# SENTINEL: str = "X"
#
# while True:
#     print(f"{question}\n"
#           f"{question_list[0]}\n"
#           f"{question_list[1]}\n"
#           f"{question_list[2]}\n"
#           f"{question_list[3]}")
#     answer: str = input("What's your answer (a/b/c/d or x)? ")
#     answer = answer.upper()
#     if answer == SENTINEL:
#         break
#     if answer == "A":
#         count_list[0] += 1
#     if answer == "B":
#         count_list[1] += 1
#     if answer == "C":
#         count_list[2] += 1
#     if answer == "D":
#         count_list[3] += 1
#     if answer != "A" and answer != "B" and answer != "C" and answer != "D":
#         print("Invalid input, try again.")
#
# print(f"Total answers: A. {count_list[0]}, B. {count_list[1]}, C. {count_list[2]}, D. {count_list[3]}\n"
#       f"The most answered: {question_list[count_list.index(max(count_list))]}\n"
#       f"The least answered: {question_list[count_list.index(min(count_list))]}")
