import functions

print("# 1. --------------------------")
# 1.
functions.print_12_24()
print()

print("# 2. --------------------------")

# 2.
functions.print_odd_7_31()
print()

print("# 3. --------------------------")

# 3.
functions.print_even_10_min20()
print()

print("# 4. --------------------------")

# 4.
functions.fizz_buzz()

print("# 5. --------------------------")

# 5.
print(f"The sum of the given array is: {functions.sum_array([1, 13, 22, 123, 49, 34, 5, 24, 57, 45])}")

print("# 6. --------------------------")

# 6.
students = [
    {
        "id": 1,
        "first_name": "John",
        "last_name": "Doe",
        "age": 25,
        "country": "USA",
        "city": "New York"
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 30,
        "country": "Canada",
        "city": "Toronto"
    },
    {
        "id": 3,
        "first_name": "Ali",
        "last_name": "Khan",
        "age": 22,
        "country": "Pakistan",
        "city": "Karachi"
    }
]

print("# 7. --------------------------")

# 7.
our_pats = [
    {
        "animal_type": "cat",
        "names": [
            "Meowzer",
            "Fluffy",
            "Kit-Cat"
        ]
    },
    {
      "animal_type": "dog",
        "names": [
            "Spot",
            "Bowser",
            "Frankie"
        ]
    }
]

print("# 7a. --------------------------")
# a.
functions.print_cat_value(our_pats)

print("# 7b. --------------------------")

# b.
functions.print_names(our_pats, "cat")

print("# 7c. --------------------------")

# c.
functions.add_name(our_pats, "cat", "Kit-Cat")
functions.add_name(our_pats, "cat", "Meowtow")
print(our_pats)

print("# 8. --------------------------")

# 8.
student = {
    "name": "John",
    "age": 20,
    "hobbies": ["reading", "games", "coding"]
}

print("# 8a. --------------------------")

# a.
functions.print_data_student(student)

print("# 8b. --------------------------")

# b.
functions.add_hobby(student)

print("# 8c. --------------------------")

# c.
functions.print_data_student(student)

print("# 8d. --------------------------")

# d.
functions.delete_object_hobby(student)

print("# 8e. --------------------------")

# e.
functions.print_data_student(student)

print("# 8f. --------------------------")

# f.
functions.add_family_name(student)
functions.print_data_student(student)

print("# 9. --------------------------")

# 9.
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

functions.print_2d_data(matrix)

print("# 10. --------------------------")

# 10.
matrix2 = [
    [0, 1, 1],
    [0, 1, 0],
    [1, 0, 0]
]

print(functions.zero_count(matrix2))

print("# 11. --------------------------")

# 11.
print(functions.find_duplicate([4, 2, 34, 4, 1, 12, 1, 4]))

print("# 12. --------------------------")

# 12.
arr = [43, "what", 9, True, "cannot", False, "be", 3, True]

print(functions.reversing_array(arr))

print("# 13. --------------------------")

# 13.
first_array = [4, 6, 7]
second_array = [8, 1, 9]

print(functions.sum_two_arr(first_array, second_array))

print("# 14. --------------------------")

# 14.
first_str = "racecar"
second_str = "Java"

print(functions.palin_find(first_str))
print(functions.palin_find(second_str))

print("# 15. --------------------------")

# 15.
counter: int = 1
while counter < 100:
    counter += 2
print(counter)

print("# 16. --------------------------")

# 16.
counter2: int = 900_000
while counter2 > 50:
    counter2 /= 2
print(counter2)

print("# 17. --------------------------")

# 17.
names: list[str] = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']

print(functions.dupli_str(names))

print("# 18. --------------------------")

# 18.
print(functions.arr_no_dupli(names))

print("# 19. --------------------------")

# 19.
print(functions.without_pete(names))

print("# 20. --------------------------")

# 20.
print(functions.similar_last1([True, False, False, True, True, False]))
print(functions.similar_last1([True, False, True, False, True, True]))
print(functions.similar_last1([True, False, True, False, True, False]))

print("# 21. --------------------------")

# 21.
print(functions.data_from_user())