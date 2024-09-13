# Start

friends: int = 4
slices: int = int(input("How much pizza slices are? "))

slices_each: int = slices // friends
slices_left: int = slices % friends

print(f"Every friend will get: {slices_each} slices \n"
      f"There will left: {slices_left} slices")

# End
