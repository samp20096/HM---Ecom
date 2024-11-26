# def tup_multi(tup1: tuple, tup2: tuple) -> tuple:
#     new_tup: tuple = tup1 + tup2
#     tup_mult: tuple = ()
#     for n in new_tup:
#         if new_tup.count(n) > 1:
#             if n not in tup_mult:
#                 tup_mult = tup_mult + (n,)
#     return tup_mult
#
# print(tup_multi((1, 2, 3, 4), (3, 4, 5, 6)))

tup: tuple = (10 ,8 ,5 ,5 ,3 ,2 ,5, 10, 30, 40)
l1 = []

for i in tup:
    l1.append(tup.index(i))
print(l1)