import random
# Start


player1: str = input("First player name: ")
player2: str = input("Second player name: ")
player3: str = input("Third player name: ")
player4: str = input("Fourth player name: ")

winner = random.choice([player1, player2, player3, player4])

print(f"The winner is: {winner}")

# End