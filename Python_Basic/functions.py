# 1.

def print_12_24() -> None:
    """
    printing the numbers from 12 to 24
    :return: None
    """
    for i in range(12, 24 + 1):
        print(i, end=" ")

# 2.
def print_odd_7_31() -> None:
    """
    printing the numbers from 7 to 31
    jumps of 2
    :return: None
    """
    for i in range(7, 31 + 1, 2):
        print(i, end=" ")

# 3.
def print_even_10_min20() -> None:
    """
    printing all even numbers between -20 to 10
    :return: None
    """
    for i in range(-20, 10 + 1, 2):
        print(i, end=" ")

# 4.
def fizz_buzz() -> None:
    """
    "fizz-buzz" game - (1 - 45)
    checking each number for % == 0 with 3, 5 or both
    :return: None
    """
    for i in range(1, 45 + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(f"FizzBuzz - {i}")
            continue
        if i % 3 == 0:
            print(f"Fizz - {i}")
        if i % 5 == 0:
            print(f"Buzz - {i}")

# 5.
def sum_array(l1: list[int]) -> int:
    """
    sum the numbers in given list
    :return: int
    """
    count: int = 0
    for i in l1:
        count += i
    return count

# 6.
"""
Didn't answer - didn't got the question right...
"""

# 7.
# a.
def print_cat_value(l1: list) -> None:
    """
    printing the values in key of "cat"
    :return: None
    """
    for i in l1:
        if i["animal_type"] == "cat":
            print(i["animal_type"])

# b.
def print_names(l1: list, type1: str) -> None:
    """
    printing the name of given animal_type of given list
    :return: None
    """
    for i in l1:
        if i["animal_type"] == type1:
            for value in i["names"]:
                print(i["animal_type"], ":", value)

# c.
def add_name(l1: list, pat_type1: str, name: str) -> None:
    """
    adding a name to the dict of given name in array
    :return: None
    """
    for i in l1:
        if i["animal_type"] == pat_type1:
            if name in i["names"]:
                print(f"'{name}' already exist in '{i["animal_type"]}' array")
            else:
                print(f"'{name}' added successfully to '{i["animal_type"]}' array")
                i["names"].append(name)

# 8.
# a.
def print_data_student(dict1: dict) -> None:
    """
    printing the data of given dict()
    :return: None
    """
    for key, value in dict1.items():
        print(f"{key}: {value}")

# b.
def add_hobby(dict1: dict) -> None:
    """
    adding a hobby to key
    :return: None
    """
    new_hobby: str = input("Add new hobby: ").lower()

    if new_hobby not in dict1["hobbies"]:
        dict1["hobbies"].append(new_hobby)
        print("Hobby added")
    else:
        print("Hobby exist in array ")

# c.
# BLANK - in main file

# d.
def delete_object_hobby(dict1: dict) -> None:
    """
    deleting value from array in hobby key
    :return: None
    """
    user_input: str = input(f"What hobby of array you want to delete{dict1["hobbies"]}?").lower()
    if user_input not in dict1["hobbies"]:
        print("The hobby not in array")
    else:
        dict1["hobbies"].remove(user_input)
        print("Deleted from array")

# e.
# BLANK - in main file

# f.
def add_family_name(dict1: dict) -> None:
    """
    adding a key "family_name" with given value
    :return: None
    """
    user_family: str = input("What is your family name? ")
    dict1.setdefault("family_name", user_family)
    print("Family name added")


# 9.
def print_2d_data(list1: list) -> None:
    """
    printing al the numbers side by side
    :return: None
    """
    for i in list1:
        for j in i:
            print(j, end = " ")

# 10.
def zero_count(list1: list) -> int:
    """
    counting how many times does zero repeating in array's of given array
    :return: int
    """
    count: int = 0
    for i in list1:
        for j in i:
            if j == 0:
                count += 1
    return count

# 11.
def find_duplicate(list1: list) -> list:
    """
    checking for duplicated and returning a list with the founded duplicates
    :return: list
    """
    found: list[int] = []
    for i in list1:
        number: int = list1.count(i)
        if number > 1 and i not in found:
            found.append(i)
    return found

# 12.
def reversing_array(list1: list) -> list:
    """
    reversing the given array without using reversed() method
    :return: list
    """
    reversed1 = []
    for i in range(len(list1) - 1, -1, -1):
        reversed1.append(list1[i])
    return reversed1

# 13.
def sum_two_arr(list1: list, list2: list) -> list:
    """
    getting 2 arrays and sum each value of index
    :return: list
    """
    sum_lists: list[int] = []
    for i in range(len(list1)):
        sum_num = list1[i] + list2[i]
        sum_lists.append(sum_num)
    return sum_lists

# 14.
def palin_find(word1: str) -> bool:
    """
    checking for palindrome words
    :return: bool
    """
    word_splited = []
    for l in word1:
        word_splited.append(l)
    if word_splited == reversing_array(word_splited):
        return True
    else:
        return False

# 15.
# BLANK - in main file

# 16.
# BLANK - in main file

# 17.
def dupli_str(list1:list) -> list:
    """
    checking for duplicated objects in array
    :return: list
    """
    duplicated: list[str] = []
    inx: int = 0
    while not inx == len(list1):
        if list1.count(list1[inx]) > 1 and list1[inx] not in duplicated:
            duplicated.append(list1[inx])
        inx += 1
    return duplicated

# 18.
def arr_no_dupli(list1: list) -> list:
    """
    returning a new array without duplications
    :return: list
    """
    not_duplicated: list[str] = []
    inx: int = 0
    while not inx == len(list1):
        if list1[inx] not in not_duplicated:
            not_duplicated.append(list1[inx])
        inx += 1
    return not_duplicated

# 19.
def without_pete(list1: list) -> list:
    """
    returning array without duplications and without the str 'pete'
    :return: list
    """
    not_pete_not_dupli: list[str] = arr_no_dupli(list1)
    if 'Pete' in not_pete_not_dupli:
        not_pete_not_dupli.remove('Pete')
    return not_pete_not_dupli

# 20.
def similar_last1(l_bool: list[bool]) -> int:
    """
    checking for the same value as the one that was before him
    retuning the index of the second same word
    :return: int
    """
    last_bool = None
    value = -1
    for i in range(len(l_bool)):
        if l_bool[i] == last_bool:
            value = i
            break
        last_bool = l_bool[i]
    return value

# 21.
def data_from_user() -> dict:
    """
    gathering data from the user to a new dict
    :return: dict
    """
    user: dict = {
        "full_name": None,
        "age": 0,
        "email": None
    }
    while True:
        while True:
            full_name: str = input("What is you full name? ")
            if len(full_name.split()) == 2:
                user["full_name"] = full_name
                break
            else:
                print("Invalid input, try again")
        while True:
            try:
                age: int = int(input("What's your age? "))
                if age >= 1 and age <= 130:
                    user["age"] = age
                    break
                else:
                    print("Age must be between 1 to 130")
            except ValueError:
                print("Invalid input, try again")
        while True:
            email: str = input("What's your Email? ")
            if "@" in email:
                user["email"] = email
                break
            else:
                print("Invalid input, try again")
        break
    return user