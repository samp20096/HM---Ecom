# x = 345 % 100
# print(x)

# x: int = 6789
# y: int = 6
#
# ahadot = x % 10
# asarot = (x % 100) // 10
# meot = (x % 1000) // 100
# alafim = x // 1000
#
# if ahadot == y or asarot == y or meot == y or alafim == y:
#     print(True)
# else:
#     print(False)

# print(alafim)


num1: int = 72
num2: int = 60
div_big = None

if num1 > num2:
    while True:
        for i in range(num1, 0, -1):
            if num1 % i == 0:
                if num2 % i == 0:
                    if div_big is None or div_big < i:
                        div_big = i
        else:
            print(div_big)
            break
else:
    while True:
        for i in range(num2, 0, -1):
            if num2 % i == 0:
                if num1 % i == 0:
                    if div_big is None or div_big < i:
                        div_big = i
        else:
            print(div_big)
            break




# for i in range(1, num1):
#     if num1 % i == 0:
#         big = num1 - i
#         for j in range(num2, i):
#             if j % num2 == 0:
#                 print(f"Div == {j}")
#         print(i)
# for i in range(1, num2):
#     if num2 % i == 0:
#         big = num2 - i
#         print(i)
# if num1 > num2:
#     biggest_div: int = num1 % num2
# else:
#     biggest_div: int = num2 % num1

# check = num1 // num2
#
# print(check)