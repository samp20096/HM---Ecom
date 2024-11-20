import random, statistics

# # 1.
#
# countries: list[str] = [
#     "Tokyo",
#     "New York",
#     "Paris",
#     "London",
#     "Dubai",
#     "Shanghai"
# ]
#
# # a.
# print(sorted(countries, key = lambda country: len(country)))
#
# # b.
# print(sorted(countries, key = lambda country: len(country.split())))
#
# # c.
# print(sorted(countries, key = lambda country: country[::-1]))
#
# # d.
# print(sorted(countries, key = lambda country: country, reverse = True))
#
# # e.
# print(sorted(countries, key = lambda country: country.upper().count("A"), reverse = True))
#
# # f.
# country_range: dict[str, list[int | str]] = {
#     "Tokyo": [5760, "Asia"],
#     "New York": [5690, "North America"],
#     "Paris": [2050, "Europe"],
#     "London": [2240, "Europe"],
#     "Sydney": [8780, "Australia"],
#     "Dubai": [1300, "Asia"],
#     "Shanghai": [4920, "Asia"]
# }
#
# countries_data: list[[str | int | str]] = [[countries[countries.index(country)], country_range[country][0], country_range[country][1]] for country in countries if country in country_range]
# print(countries_data)
#
# # a.
# print(sorted(countries_data, key = lambda dis: dis[1]))
#
# # b.
# print(sorted(countries_data, key = lambda dis: dis[1], reverse = True))
#
# # c.
# print(sorted(countries_data, key = lambda name: name[2]))
#
# # d.
# print(sorted(countries_data, key = lambda name: (name[2], name[1])))
#
# numbers: list[int] = [random.randint(1, 100) for _ in range(50)]
#
# # 1,
# print(sorted(numbers, key = lambda number: number))
#
# # 2.
# print(sorted(numbers, key = lambda number: (statistics.mean(numbers) - number if number < statistics.mean(numbers) else number - statistics.mean(numbers))))


# sentence: str = ("This chocolate cake is rich, moist, and full of delicious chocolate flavor."
#                  "To make the cake, you will need chocolate, flour, sugar, eggs, and butter."
#                  "After baking the chocolate cake, let the cake cool before adding the chocolate frosting.")
#
# words: dict[str | int] = dict()
#
# for word in sentence.lower().replace(",", "").split():
#     words[word] = words.get(word, 0) + 1
#
# print(words)
# print("Highest repeated word:", sorted(words.items(), key =  lambda item: item[1], reverse=True)[0])
#
# letters: dict[str | int] = dict()
# for char in sentence.lower().replace(",", "").replace(".", "").replace(" ", ""):
#     for lett in char:
#         letters[lett] = letters.get(lett, 0) + 1
#
# print(letters)
# print("Highest repeated letter:", sorted(letters.items(), key =  lambda item: item[1], reverse=True)[0])
#
# # 3.
# numbers: list[int] = [_ for _ in range(1, 20 + 1)]
#
# numbers_powered: dict[int | int] = dict()
# for num in numbers:
#     numbers_powered[num] = numbers_powered.get(num, num ** 3)
#
# print(numbers_powered)
#
# user_n: int = int(input("Number: "))
#
# print(f"{user_n} powered by 3 = {numbers_powered[user_n] if user_n in numbers_powered else "Not found"}")