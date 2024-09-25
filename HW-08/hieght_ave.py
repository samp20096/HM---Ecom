import statistics

# Start

# List:
height_l: list[float] = []
# Count:
heighest_2: int = 0
above_ave: int = 0
# Input check loop
while True:
    height: float = float(input("Height: "))
    if height >= 1.6 and height <= 3:
        height_l.append(height)
    if height > 2:
        heighest_2 += 1
    if height != -999 and height < 1.6 or height > 3:
        print("Not in range, didn't registered.")
        continue
    if height == -999:
        print("Finish")
        break

# calculation
min_h = min(height_l)
max_h = max(height_l)
ave: float = statistics.mean(height_l)
high_ave: int = 0

for i in height_l:
    if i > ave:
        high_ave += 1

# Data
print(f"Players amount: {len(height_l)}\n"
      f"Highest Player: {max_h}\n"
      f"Lowest PLayer: {min_h}\n"
      f"All players average: {ave:.2f}\n"
      f"Higher then average: {high_ave}")

# End
