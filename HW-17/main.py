# 1.
id_i: dict = {
    "name": "Israel",
    "birth": 1948,
    "population_millions": 9.3,
    "capital": "Jerusalem",
    "language": "Hebrew",
    "cities": ["Jerusalem", "Tel Aviv", "Rishon LeZion", "Petah Tikva", "Ashdod"],
    "currency": "ILS",
    "area_Kilometer": 22_145 ,
    "gdp_billion": 450
}

# a.
print(f"Capital of Israel: {id_i.get("capital")}")

# b.
print(f"All keys: {id_i.keys()}")

# c.
print(f"All values: {id_i.values()}")

# d.
for key, value in id_i.items():
    print(f"{key}: {value}")

# e.
id_i_2 = id_i.copy()
print(id_i_2)

# f.
gdp_i = id_i_2.pop("gdp_billion")
print(f"Deleted value of gdp: {gdp_i}")
print(id_i_2)

# g.
id_i_v_emp = id_i.fromkeys(id_i, None).copy()
print(id_i_v_emp)

for key in id_i_v_emp.keys():
    if key == "cities":
        cities: list[str] = []
        for i in range(3):
            user_input: str = input(f"City {i + 1}:")
            cities.append(user_input)
        id_i_v_emp[key] = cities
    else:
        try:
            user_input: str = input(f"{key}: ")
        except ValueError:
            user_input: int = int(user_input)
        id_i_v_emp[key] = user_input

print(id_i_v_emp)

# 2.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])
solution = Solution()

word: str = input("Words: ")

print(f"The length of the last word is: {solution.lengthOfLastWord(word)}")