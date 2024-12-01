
oscar_winners = {"Leonardo DiCaprio", "Meryl Streep", "Denzel Washington", "Emma Stone", "Tom Hanks", "Natalie Portman", "Robert De Niro", "Al Pacino"}
titanic_actors = {"Leonardo DiCaprio", "Kate Winslet", "Billy Zane", "Kathy Bates"}
dark_knight_actors = {"Christian Bale", "Heath Ledger", "Michael Caine", "Gary Oldman", "Aaron Eckhart"}
avengers_actors = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Mark Ruffalo", "Chris Hemsworth", "Jeremy Renner"}
iron_man_actors = {"Robert Downey Jr.", "Gwyneth Paltrow", "Terrence Howard"}
legendary_actors = {"Al Pacino", "Robert De Niro", "Marlon Brando", "Jack Nicholson", "Dustin Hoffman"}
actor_list = {"Robert Downey Jr.", "Chris Evans", "Scarlett Johansson", "Leonardo DiCaprio", "Tom Hanks"}
movie_cast = {"Tom Hanks", "Tom Cruise", "Will Smith", "Matt Damon", "Brad Pitt"}


# a.
oscar_winners.add("Emma Watson")

# b.
oscar_copy = oscar_winners.copy()
oscar_copy.remove("Meryl Streep")
print(oscar_copy)
oscar_copy.clear()
print(oscar_copy)

# c.
print(titanic_actors & dark_knight_actors)

# d.
print(iron_man_actors & avengers_actors)

# e.
print(actor_list.issubset(oscar_winners))

# f.
print(actor_list.issuperset(avengers_actors))

# g.
poped = movie_cast.pop()
print(poped)

# h.
try:
    movie_cast.remove("Matt Damon")
except ValueError:
    print("Not Found")

# i.
print(titanic_actors - oscar_winners)

# j.
print(titanic_actors ^ dark_knight_actors)

# k.
oscar_winners.add("Cate Blanchett")
oscar_winners.add("Daniel Day-Lewis")
print(oscar_winners)

# l.
print(titanic_actors | dark_knight_actors)