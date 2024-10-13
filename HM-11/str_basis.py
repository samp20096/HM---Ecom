data_person: str = "Tal mojaev afula"

# a.
print(f"The length: {len(data_person)}")

# b.
print(f"All upper: {data_person.upper()}")

# c.
print(f"All lower: {data_person.lower()}")

# d.
print(f"Starts with first name? {data_person.startswith("Tal")}")

# e.
print(f"Ends with city? {data_person.endswith("Afula")}")

# f.
data_list: list[str] = data_person.split()
print(f"List of data str: {data_list}")

# g.
star_data: str = data_person.replace(" ", "*")
print(f"Star replacing spaces: {star_data}")

# h.
centered: str = data_person.center(50, "=")
print(f"Centered with '=': {centered}")

# i.
print(f"From 4 char: {data_person[3::]}")

# j.
print(f"From start to 4 with: {data_person[:4:]}")

# k.
print(f"All even chars: {data_person[::2]}")

# l.
print(f"All capital: {data_person.title()}")