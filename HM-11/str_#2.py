# a.

word: str = " fun-day "
print(f"With no spaces: {word.strip(" ")}")

# b.
word2: str = "hello"
print(f"Only letters? {word2.isalpha()}")

# c.
number: str = "777"
print(f"Only numbers? {number.isdigit()}")

# d.
spaces: str = "   "
print(f"Only spaces? {spaces.isspace()}")

# e.
list1: list[str] = ['N', 'I', 'N', 'J', 'A']
print(f"from list to str: {''.join(list1)}")

# f.
print(f"from list to str with * between: {"*".join(list1)}")

# g.
word3: str = "hELLo"
print(f"Is 'e' in hELLo? {'e' in word3.lower()}")

# h.
word_user: str = input("Put a random word: ")
user_word_list: list[str] = [word_user for word_user in word_user.upper() if word_user.isalpha()]
print(user_word_list)