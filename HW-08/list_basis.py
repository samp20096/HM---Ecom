# Start

# a.

numbers: list[int] = []

for i in range(1, 100 + 1):
    numbers.append(i)

print(numbers)

# b.

print(numbers[0])

# c.

print(numbers[-1])

# d.

print(len(numbers))

# e.

print(numbers[2:12])

# f.

print(numbers[80::])

# g.

print(numbers[:17])

# h.

print(numbers[::-1])

# i.

print(numbers[1: 100: 2])

# j.

print(numbers[2::3])

# k.

print(numbers[6::7])

# l.

print(numbers[9::10])

# m.

print(numbers[98:64:-3])

# n.

numbers.insert(50, 999)
print(numbers[50])

# o.

numbers.pop(100)
print(numbers[90::])

# End
