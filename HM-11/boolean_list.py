import random

# a.
rand_list: list[bool] = [random.choice([True, False]) for _ in range(3)]
print(f"Random True/False: {rand_list}")

# b.
print(f"All True? {all(rand_list)}")

# c.
print(f"At least one True? {any(rand_list)}")

# d.
print(f"All False? {any(rand_list)}")
# if all == False print will be False - if there's 1 True print will be True

# e.
print(f"At least one False? {any(rand_list)}")

# f.
rand_num: list[int] = [random.randint(-2, 2) for _ in range(5)]
print(rand_num)

# g.
print(f"All != 0? {all(rand_num)}")

# h.
print(f"At least one != 0? {any(rand_num)}")

# i.
print(f"All == 0? {any(rand_num)}")
# if at least one != 0 print will be True - if all == 0 print will be False

# j.
print(f"At least one == 0? {all(rand_num)}")
# if at least one 0 in list print will be False - if no 0 in list print will be True