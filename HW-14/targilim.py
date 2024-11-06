# 3.

# a.
# x: int = int(input("Number: "))
# x_str: str = str(x)
#
# print(*[all(n == x_str[0] for n in x_str)])

# b.
# amount: int = int(input("Amount: "))
# total_cost: int = 0
#
# if amount > 0:
#     t1: int = min(amount, 100)
#     total_cost += t1 * 0.9
#     amount -= t1
# if amount > 0:
#     t2: int = min(amount, 100)
#     total_cost += t2 * 0.8
#     amount -= t2
# if amount > 0:
#     t3: int = min(amount, 300)
#     total_cost += t3 * 0.7
#     amount -= t3
# if amount > 0:
#     t4: int = min(amount, 300)
#     total_cost += t4 * 0.6
#     amount -= t4
# if amount > 0:
#     total_cost += amount * 0.95
#
# print(f"The total cost after reducing is: {total_cost:.2f}")

# c.
# numbers: list[float] = [float(input("Float number: ")) for _ in range(3)]
#
# if numbers[0] + numbers[1] == numbers[2]:
#     print(True)
# elif numbers[1] + numbers[2] == numbers[0]:
#     print(True)
# elif numbers[0] + numbers[2] == numbers[1]:
#     print(True)
# else:
#     print(False)

# d.
# word: str = input("Word: ")
#
# SENTINEL: str = "*"
#
# letter_list: list[str] = []
#
# while True:
#     letter: str = input("Letter: ")
#     if letter == SENTINEL:
#         break
#     letter_list.append(letter)
#
# is_match = all(letter in word for letter in letter_list)
#
# print(True if is_match else False)