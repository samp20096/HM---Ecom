# Start

# a.
temp: list[float] = []

# b.
SENTINEL: int = -999
while True:
    user_temp: float = float(input("Temperature: "))
    if user_temp == SENTINEL:
        print("Done")
        break
    if not -51 >= user_temp <= 50:
        print("Value registered.")
        temp.append(user_temp)

# c.
temp.extend([-20.0, 39.1, 18.5])
print(f"Extended to temp list: {temp}")

# d.
x: list[float] = [1, 2, 3]
list1: list[float] = temp + [1, 2, 3]
print(f"Concatenating to make a new list with the results: {list1}")
# when using + you must use a variable to where you save the data
# when using (extend) you putting a value in a existing variable without feedback

# e.
min_temp: float = min(temp)
max_temp: float = max(temp)
print(f"Minimum temperature: {min_temp:.2f}\n"
      f"Max temperature: {max_temp:.2f}")

# f.
print(f"Is 18.5 in the list? {18.5 in temp}")

# g.
print(f"How many -20 in the list? {temp.count(-20)}\n{temp}")

# h.
ave_temp: float = sum(temp) / len(temp)
print(f"The average is: {ave_temp:.2f}")

# i.
for each_temp in temp:
    print(each_temp)

# j.
print(f"The index of 39.1 is: {temp.index(39.1)}")

# k.
print(f"Before del: {temp}")
del temp[0]
print(f"After del: {temp}")

# l.
del temp[2::2]
print(temp)

# m.
# need to check if index/value is available
# if there is no index/value and remove is executed, the program will crash
print(f"Before remove: {temp}")
if 18.5 in temp:
    temp.remove(18.5)
print(f"After remove: {temp}")

# n.
temp_last: float = temp.pop()  # pop() removing from the end by default
print(f"Last temperature: {temp_last}")

# o.
copy_list: list[float] = temp.copy()
copy_list.sort()
print(f"temp: {temp}\n"
      f"copy_list and sorted: {copy_list}")

# p.
copy_list2: list[float] = temp.copy()
copy_list2.sort(reverse=True)
print(f"temp:{" " * 26} {temp}\n"
      f"copy_list and sorted backwards: {copy_list2}")

# End
