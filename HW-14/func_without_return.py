import statistics

# 1.

# a.
def my_acsending(x: int, y: int):
    """Sorting a given numbers"""
    print(*(sorted((x ,y))))


# b.
def my_details(x: str):
    """printing the first, middle and last letters
    **The middle letters will print 2 of them because for given str have even letters"""
    print(x[0], x[len(x) // 2 - 1: len(x) //2 + 1], x[-1])


# c.
def say_bool(x: bool):
    """printing "Yes" or "No" for given True or False"""
    print("Yes" if x == True else "No")


# d.
def print_zugi(x: list[int]):
    """Checking a list for Even or Odd numbers and printing the result"""
    print(*["Even" if number % 2 == 0 else "Odd" for number in x])


# e.
def my_statistics(x: list[int]):
    """checking a list of grades and returning statistics of grades"""
    try:
        print(f"Min grade: {min(x)}\n"
              f"Max grade: {max(x)}\n"
              f"Total grades: {len(x)}\n"
              f"Mean grades: {statistics.mean(x):.2f}")
    except ValueError:
        print("No data, skip.")
        pass