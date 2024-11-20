sentence: str = ("This chocolate cake is rich, moist, and full of delicious chocolate flavor."
                 "To make the cake, you will need chocolate, flour, sugar, eggs, and butter."
                 "After baking the chocolate cake, let the cake cool before adding the chocolate frosting.")

# sentence_split: list[str] = sentence.split()

words_count: dict[str | int] = dict()

for word in sentence.split():
    words_count[word] = words_count.get(word, 0) + 1

print(words_count)