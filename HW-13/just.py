# x: int = 23
#
# division: int = x // 10
# moduls: int = x % 10
# print(division, moduls)
from itertools import count

# x = 13 ** 0.5
# print(x)
#
# prime_num: list[int] = [i for i in range(2, 200 + 1) if all(i % x != 0 for x in range(2, i))]
#
# # for i in range(2, 100 + 1):
# #     if i > i ** 0.5:
# #         for n in range(2, i + 1):
# #             prime_num.append(i)
#
# print(prime_num)

question: str = "What region you live in? "
#                            0              1              2            3
question_list: list[str] = ["A. Northern", "B. Southern", "C. Middle", "D. Else"]
#                        0  1  2  3
count_list: list[int] = [3, 0, 0, 0]
SENTINEL: str = "x"

max(count_list)

# while True:
#     print(f"{question}\n"
#           f"{question_list[0]}\n"
#           f"{question_list[1]}\n"
#           f"{question_list[2]}\n"
#           f"{question_list[3]}")
#     answer: str = input("What's your answer (a/b/c/d or x)? ")
#     answer.upper()
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
#
# print(f"Total answers: A. {count_list[0]}, B. {count_list[1]}, C. {count_list[2]}, D. {count_list[3]}\n"
#       f"The most answered: {max(count_list)}\n"
#       f"The least answered: {min(count_list)}")