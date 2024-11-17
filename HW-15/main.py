import random, statistics

# 1.
numbers: list[int] = [random.randint(1, 100) for _ in range(50)]
print(numbers)

# a.
print("1. a.: ", list(filter(lambda num: num >= 50, numbers)))

# b.
print("1. b.: ", list(filter(lambda num: num % 7 == 0, numbers)))

# c.
print("1. c.: ", list(filter(lambda num: num >= 10, numbers)))

# d.
print("1. d.: ", list(filter(lambda num: (num % 10) == (num // 10), numbers)))

# e.
print("1. e.: ", list(filter(lambda num: (num % 10) + (num // 10) == 9, numbers)))

# f.
print("1. f.: ", list(filter(lambda num: num >= statistics.mean(numbers), numbers)))

# g.
print("1. g.: ", list(filter(lambda num: num >= (max(numbers) // 2), numbers)))

print()

# 2.
words: list[str] = [
    "Fortnite",
    "Grand Theft Auto V",
    "The Elder Scrolls V: Skyrim",
    "Dark Souls",
    "Overwatch"
]

# a.
print("2. a.: ", list(filter(lambda word: len(word) >= 8, words)))

# b.
print("2. b.: ", list(filter(lambda word: word.upper().startswith("F"), words)))

# c.
print("2. c.: ", list(filter(lambda word: len(word.split()) == 2, words)))

# d.
print("2. d.: ", list(filter(lambda word: "V" in word.upper(), words)))

print()

# 3.
numbers: list[int] = [random.randint(-50, 50) for _ in range(20)]

# a.
print("3. a.: ", list(map(lambda num : num ** 3, numbers)))

# b.
print("3. b.: ", list(map(lambda num : num % 10, numbers)))

# c.
print("3. c.: ", list(map(lambda num : num * (9/5) + 32, numbers)))

# d.
print("3. d.: ", list(map(lambda num : "Positive" if num >= 0 else "Negative", numbers)))

print()

# 4.
words: list[str] = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Strawberry",
    "Pineapple",
    "Grapes",
    "Watermelon"
]

# a.
print("4. a.: ", list(map(lambda word: word[::-1], words)))

# b.
print("4. b.: ", list(map(lambda word: word[0], words)))

# c.
print("4. c.: ", list(map(lambda word: word.upper(), words)))

# d.
print("4. d.: ", list(map(lambda word: word[len(word) // 2] , words)))

# e.
print("4. e.: ", list(map(lambda word: word + "!" if word[-1].upper() == "S" else word, words)))

# 5.
# בעזרת Global בתוך פונקציה ניתן לצאת לתאי זיכרון חיצוניים ולהשתמש מ ה- Scope של הפונקציה

# החסרון בשימוש Global בפונקציה היא שהיא משפיעה על התא זיכרון שעליו משתמשים ב Global
# וזה ידרוש צומת לב לפרט זה מכיוון שבמקרה ואין כזה תא זיכרון התכנית יכול לקרוס

# בקוד:
# x: int = 1
# def foo():
#     print(x)
#     x = 4
# foo()

# נקבל שגיאה מכיוון שב-Scope של הפונקציה ביקשנו להדפיס X שעדיין לא הוגדר בתא זיכרון
# אלא רק לאחר מכן הוסף תא זזיכרון בשם X

