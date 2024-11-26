# a.

tup1: tuple[int] = (99,)


# b.

tup2: tuple[int, int, int] = (77, 88, 99)


# c.

def len_tup(tup_in: tuple) -> int:
    len_tup1 = len(tup_in)
    return len_tup1

print(len_tup(tup2))


# d.

def tup_added(tup1: tuple, tup2: tuple) -> tuple:
    tup_added1 = tup1 + tup2
    return tup_added1

print(tup_added(tup1, tup2))


# e.
def tup_multi(tup1: tuple, tup2: tuple) -> tuple:
    new_tup: tuple = tup1 + tup2
    tup_mult: tuple = ()
    for n in new_tup:
        if new_tup.count(n) > 1:
            if n not in tup_mult:
                tup_mult = tup_mult + (n,)
    return tup_mult

print(tup_multi((1, 2, 3, 4), (3, 4, 5, 6)))


# f.
def tup_not_multi(tup1: tuple, tup2: tuple) -> tuple:
    new_tup: tuple = tup1 + tup2
    tup_not_mult: tuple = ()
    for n in new_tup:
        if new_tup.count(n) == 1:
            if n not in tup_not_mult:
                tup_not_mult = tup_not_mult + (n,)
    return tup_not_mult

print(tup_not_multi((1, 2, 3, 4), (3, 4, 5, 6)))


# g.
def inx_in_tup(tup1: tuple, inx: int) -> any:
    try:
        value_inx = tup1[inx]
    except IndexError:
        print(f"Index Not in Range, The range is(0 - {len(tup1) - 1})")
        return None
    return value_inx

print(inx_in_tup((1, 2, 3, 4), 2))


# h.
def backwords_tup(tup1: tuple) -> tuple:
    reverse: tuple = tuple(sorted(tup1, reverse = True))
    return reverse

print(backwords_tup((1, 2, 3, 4)))


# i.
def dupli_value(tup1: tuple, n: int) -> tuple:
    duplicated: tuple = tup1 * n
    return duplicated

print(dupli_value((1, 2, 3, 4), 3))


# j.
def without_num(tup1: tuple, n: int) -> tuple:
    hold_new: list = []
    for i in tup1:
        if i != n:
            hold_new.append(i)
        else:
            continue
    return tuple(hold_new)
print(without_num((10 ,8 ,5 ,5 ,3 ,2 ,50, 10, 30, 40), 10))


# k.
def not_dupli(tup1: tuple) -> tuple:
    new_hold: list = []
    for i in tup1:
        if i not in new_hold:
            new_hold.append(i)
        else:
            continue
    return tuple(new_hold)

print(not_dupli((10 ,8 ,5 ,5 ,3 ,2 ,50, 10, 30, 40)))


# l.
def inx_find(tup1: tuple, n: int) -> any:
    new_hold: list = []
    if n in tup1:
        for i in range(len(tup1)):
            i -= 1
            if tup1[i] == n:
                new_hold.append(i)
    else:
        print("Not in tuple")
    return tuple(new_hold)

print(inx_find((10 ,8 ,5 ,5 ,3 ,2 ,5, 10, 30, 40), 5))


# m.
SENTINEL: str = "done"
names: list[str] = []

while True:
    try:
        name: str = input("Name: ")
    except ValueError:
        print("Input is not str, try again")
        continue
    if name == SENTINEL:
        print("Done")
        break
    names.append(name)

sentinel_n: int = -999
grades: list[int] = []

while True:
    try:
        grade: int = int(input("Grade: "))
    except ValueError:
        print("Input is not int, try again")
        continue
    if grade == sentinel_n:
        print("Done")
        break
    if 0 <= grade <= 100:
        grades.append(grade)
    else:
        print("Not between 0 - 100, try again")
        continue

paired_by_zip: tuple = tuple(zip(names, grades))

print(tuple(sorted(paired_by_zip)))

# 2.
# list - Can be changed
# use cases: good to make manipulations and changes but works slow compare to tuple
# tuple - Can't be changed
# use cases: good for faster operations because the memory now's the exact place that tuple holds

# 3.
# the code does not give an error because dictionary is changeable
# because dictionary is changeable you can make changes to a dict that sits in a tuple.