count: int = 0
total: float = 0
highest: float = 0
new_record: float = None
highest_name: str = None
country_name: str = None

for count in range(7):
    score: float = float(input("What's your score? "))
    country: str = input("Country: ")
    name: str = input("Participant name? ")
    if score < 5.8 or score > 7.4:
        print("Low score, not registered.")
        continue
    if score > 5.7:
        print("Good score, registered.")
        count += 1
        total += score
    if score > highest:
        highest += score
    if score > 6.23:
        highest_name = name
        country_name = country
        new_record = score

else:
    print(f"Total best scores: {count}  average: {total / count:.2f}\n"
          f"Highest score: {highest:.2f} \n"
          f"New world record: {highest_name}, {new_record}, {country_name}")

# End
