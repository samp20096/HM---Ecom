import func_without_return, func_with_return

# Start

# 1.
help(func_without_return)

# a.
func_without_return.my_acsending(7, -12)

# b.
func_without_return.my_details("AI is the best")

# c.
func_without_return.say_bool(True)
func_without_return.say_bool(False)

# d.
func_without_return.print_zugi([5, 3, 2, 10, 15, 14, 14])

# e.
SENTINEL: int = -99
grades: list[int] = []

while True:
    try:
        grade: int = int(input("Grade: "))
        if grade == SENTINEL:
            print("Done")
            break
        if 0 <= grade <= 100:
            grades.append(grade)
            print("Added")
        else:
            print("Not in range.")
    except ValueError:
        print("Invalid Input, try again.")

func_without_return.my_statistics(grades)

# 2.
help(func_with_return)

# a.
ave1: float = func_with_return.my_ave(90, 99)

print(f"{ave1:.2f}")

# b.
head1: str = func_with_return.my_headline("python has concurred the world")
print(head1)
print(head1)

# c.
res_con: list[int] = func_with_return.concat_list(
    [1, 2],
    [3, 4, 5, 6],
    [7, 8, 9])
print(f"New list: {res_con}\n"
      f"Length of list: {len(res_con)}")

# End